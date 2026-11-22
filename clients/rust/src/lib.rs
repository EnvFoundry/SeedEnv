//! Thin invocation client for native hosts. The Python implementation owns
//! catalogue composition and preparation; hosts retain their job scheduler.
use std::ffi::{OsStr, OsString};
use std::io::{self, Write};
use std::path::PathBuf;
use std::process::{Command, Stdio};

#[derive(Clone, Debug, Default)]
pub struct SearchOptions<'a> {
    pub field: Option<&'a str>,
    pub direction: Option<&'a str>,
    pub offset: usize,
    pub limit: Option<usize>,
}

#[derive(Clone, Debug)]
pub struct Client {
    pub program: OsString,
    pub prefix: Vec<OsString>,
    pub home: Option<PathBuf>,
    pub research_space: Option<PathBuf>,
    pub catalog: Option<PathBuf>,
}

impl Client {
    pub fn new(python: impl Into<OsString>) -> Self {
        Self { program: python.into(), prefix: Vec::new(), home: None, research_space: None, catalog: None }
    }

    /// Return JSON, except for `guide`, which returns Markdown. Arguments never
    /// pass through a shell. Run from the native host's blocking worker pool.
    pub fn request<I, S>(&self, arguments: I) -> io::Result<String>
    where I: IntoIterator<Item = S>, S: AsRef<OsStr> {
        self.request_input(arguments, None)
    }

    fn request_input<I, S>(&self, arguments: I, input: Option<&str>) -> io::Result<String>
    where I: IntoIterator<Item = S>, S: AsRef<OsStr> {
        let arguments: Vec<OsString> = arguments.into_iter().map(|s| s.as_ref().to_owned()).collect();
        let partial = arguments.first().is_some_and(|s| s == "prepare-request" || s == "build");
        let mut command = Command::new(&self.program);
        command.args(&self.prefix).args(["-m", "seedenv"]);
        if let Some(home) = &self.home { command.arg("--home").arg(home); }
        else if let Some(space) = &self.research_space { command.arg("--research-space").arg(space); }
        if let Some(catalog) = &self.catalog { command.arg("--catalog").arg(catalog); }
        let mut child = command.args(arguments).stdin(Stdio::piped()).stdout(Stdio::piped()).stderr(Stdio::piped()).spawn()?;
        if let Some(mut stdin) = child.stdin.take() {
            if let Some(input) = input { stdin.write_all(input.as_bytes())?; }
        }
        let output = child.wait_with_output()?;
        if !output.status.success() && !(partial && output.status.code() == Some(2)) {
            return Err(io::Error::other(String::from_utf8_lossy(&output.stderr).into_owned()));
        }
        String::from_utf8(output.stdout).map_err(|error| io::Error::new(io::ErrorKind::InvalidData, error))
    }

    pub fn search(&self, query: &str) -> io::Result<String> { self.search_page(query, &SearchOptions::default()) }
    pub fn search_page(&self, query: &str, options: &SearchOptions<'_>) -> io::Result<String> {
        let mut args = vec!["search".to_owned(), "--offset".into(), options.offset.to_string(),
                            "--limit".into(), options.limit.unwrap_or(20).to_string()];
        if let Some(field) = options.field { args.extend(["--field".into(), field.into()]); }
        if let Some(direction) = options.direction { args.extend(["--direction".into(), direction.into()]); }
        args.extend(["--".into(), query.into()]);
        self.request(args)
    }
    pub fn browse(&self, field: Option<&str>) -> io::Result<String> {
        match field { Some(name) => self.request(["browse", "--field", name]), None => self.request(["browse"]) }
    }
    pub fn guide(&self, module: &str) -> io::Result<String> { self.request(["guide", module]) }
    pub fn example(&self, module: &str) -> io::Result<String> { self.request(["example", module]) }
    pub fn show(&self, name: &str) -> io::Result<String> { self.request(["show", name]) }
    pub fn context(&self, modules: &[&str]) -> io::Result<String> {
        self.request(std::iter::once("context").chain(modules.iter().copied()))
    }
    pub fn installed(&self) -> io::Result<String> { self.request(["installed"]) }
    pub fn discover(&self, modules: &[&str], python: Option<&OsStr>) -> io::Result<String> {
        let mut args: Vec<OsString> = std::iter::once("discover").chain(modules.iter().copied()).map(OsString::from).collect();
        if let Some(python) = python { args.push("--python".into()); args.push(python.into()); }
        self.request(args)
    }
    pub fn bind(&self, component: &str, command: &[OsString]) -> io::Result<String> {
        self.request([OsString::from("bind"), component.into(), "--".into()].iter().chain(command))
    }
    pub fn export_package(&self, host: &str, output: &OsStr, modules: Option<&[&str]>) -> io::Result<String> {
        let mut args: Vec<OsString> = vec!["connect".into(), host.into(), "--output".into(), output.into()];
        if let Some(modules) = modules { args.push("--modules".into()); args.extend(modules.iter().map(OsString::from)); }
        self.request(args)
    }
    pub fn plan(&self, modules: &[&str]) -> io::Result<String> {
        self.request(std::iter::once("plan").chain(modules.iter().copied()))
    }
    pub fn prepare(&self, modules: &[&str]) -> io::Result<String> {
        self.request(std::iter::once("prepare").chain(modules.iter().copied()).chain(["--background"]))
    }
    pub fn status(&self, job: &str) -> io::Result<String> { self.request(["status", job]) }
    pub fn cancel(&self, job: &str) -> io::Result<String> { self.request(["cancel", job]) }
    pub fn entry(&self, component: &str) -> io::Result<String> { self.request(["entry", component]) }
    pub fn templates(&self) -> io::Result<String> { self.request(["templates"]) }
    pub fn manuscript(&self, template: &str, output: &OsStr) -> io::Result<String> {
        self.request([OsStr::new("manuscript"), OsStr::new(template), OsStr::new("--output"), output])
    }
    pub fn build(&self, source: &OsStr, output: Option<&OsStr>) -> io::Result<String> {
        let mut args = vec![OsString::from("build"), source.into()];
        if let Some(path) = output { args.extend(["--output".into(), path.into()]); }
        self.request(args)
    }
    /// The product runs this on its selected worker and owns the job. JSON input
    /// supplies selections, existing command arrays and preparation options.
    pub fn prepare_on_host(&self, request: &str, cancel_file: Option<&OsStr>) -> io::Result<String> {
        let mut args = vec![OsString::from("prepare-request")];
        if let Some(path) = cancel_file { args.extend(["--cancel-file".into(), path.into()]); }
        self.request_input(args, Some(request))
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn catalogue_and_errors_cross_the_native_boundary() {
        let python = std::env::var("SEEDENV_TEST_PYTHON").unwrap_or_else(|_| "python3".into());
        let client = Client::new(python);
        let result = client.search("optics").expect("Python package installed or on PYTHONPATH");
        assert!(result.contains("optics"));
        assert!(client.plan(&["not-a-module"]).is_err());
        assert!(client.plan(&[]).unwrap().contains("\"actions\": []"));
        assert!(client.prepare(&[]).unwrap().contains("\"job\": null"));
        assert!(client.context(&["thin-films"]).unwrap().contains("python-tmm"));
        assert!(client.example("thin-films").unwrap().contains("coh_tmm"));
        let scope = SearchOptions { field: Some("optics"), direction: Some("optoelectronic-devices"), ..Default::default() };
        let devices = client.search_page("", &scope).unwrap();
        assert!(devices.contains("semiconductor-transport"));
        assert!(!devices.contains("fiber-pulses"));
        assert!(client.search("--a-search-term").unwrap().contains("\"total\": 0"));
        assert!(client.templates().unwrap().contains("standard-article-zh"));
        assert!(client.prepare_on_host("{\"selections\":[]}", None).unwrap().contains("\"ready\": []"));
    }
}
