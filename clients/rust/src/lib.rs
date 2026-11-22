//! Thin invocation client for native hosts. The Python implementation owns
//! catalogue composition and preparation; hosts retain their job scheduler.
use std::ffi::{OsStr, OsString};
use std::io;
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
        let mut command = Command::new(&self.program);
        command.args(&self.prefix).args(["-m", "seedenv"]);
        if let Some(home) = &self.home { command.arg("--home").arg(home); }
        else if let Some(space) = &self.research_space { command.arg("--research-space").arg(space); }
        if let Some(catalog) = &self.catalog { command.arg("--catalog").arg(catalog); }
        let output = command.args(arguments).stdin(Stdio::null()).output()?;
        if !output.status.success() {
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
    }
}
