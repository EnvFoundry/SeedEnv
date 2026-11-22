import { spawn } from "node:child_process";

export interface ModuleSummary {
  id: string;
  title: string;
  summary: string;
  summary_en?: string;
  kind?: "module" | "resource";
  tags: string[];
  components: string[];
  includes: string[];
  paths: { field: string; field_title: string; direction: string; direction_title: string }[];
  software: { id: string; title: string; kind: string }[];
}
export interface Navigation {
  fields: { id: string; title: string; module_count: number; direction_count?: number; resource_count?: number; kind?: "research" | "shared" }[];
  field: string | null;
  directions: { id: string; title: string; module_count: number }[];
  resources?: ModuleSummary[];
  totals?: { fields: number; directions: number; modules: number; resources: number };
}
export interface SearchScope { field?: string; direction?: string }
export interface PlanAction {
  component: string;
  title: string;
  /** Selected tasks using this shared software or host connection. */
  modules?: string[];
  kind: "python" | "environment" | "command" | "plugin" | "connector";
  action: "reuse" | "share" | "install" | "connect" | "setup" | "choose-host" | "add-plugin" | "configure-connector";
  provided_by?: string;
  command?: string[] | null;
  requirements?: string[];
  packages?: string[];
  installer?: string | null;
  channel?: string;
  location?: string;
  instructions?: string;
  url?: string;
  connection?: Record<string, unknown>;
}
export interface Plan {
  modules: string[];
  target: "linux" | "darwin" | "windows";
  actions: PlanAction[];
  guides: { module: string; title: string }[];
  storage: { root: string; new_environments: number; reused_environments: number;
    download_bytes: number | null; additional_disk_bytes: number | null; free_bytes: number | null };
}
export interface Preparation {
  id: string;
  state: "queued" | "running" | "ready" | "partial" | "cancelled" | "failed";
  selection: string[];
  result: { ready: unknown[]; pending: PlanAction[]; failed: { component: string; error: string }[] } | null;
  error: string | null;
  output?: string;
}
export interface PreparationStart {
  job: string | null;
  state: "queued" | "ready";
  result?: Preparation["result"];
}
export interface ResearchExample {
  module: string;
  component: string;
  file: string;
  args?: string[];
  uri: string;
  content: string;
}
export interface ResearchContext {
  modules: { id: string; title: string; guide: string; example: Omit<ResearchExample, "content" | "module"> | null; paths: ModuleSummary["paths"] }[];
  software: PlanAction[];
  storage: Plan["storage"];
  ready: boolean;
}
export interface OrigoPreparation {
  component: string;
  request: {
    execution_id: string;
    id: string;
    version: string;
    destination: string;
    requirements?: string[];
    preset?: "research-tex";
  };
}

/** A local Python command. Remote products provide their own transport bridge. */
export class SeedEnv {
  constructor(readonly options: {
    command: string[];
    home?: string;
    researchSpace?: string;
    catalog?: string;
    env?: NodeJS.ProcessEnv;
  }) {
    if (!options.command.length) throw new Error("Provide the Python command on the execution host");
  }

  private request<T>(args: string[], signal?: AbortSignal, text = false): Promise<T> {
    const [program, ...prefix] = this.options.command;
    const common = ["-m", "seedenv"];
    if (this.options.home) common.push("--home", this.options.home);
    else if (this.options.researchSpace) common.push("--research-space", this.options.researchSpace);
    if (this.options.catalog) common.push("--catalog", this.options.catalog);
    return new Promise((resolve, reject) => {
      const child = spawn(program, [...prefix, ...common, ...args], {
        stdio: ["ignore", "pipe", "pipe"], shell: false,
        env: this.options.env ?? process.env, signal,
      });
      let stdout = "", stderr = "", size = 0;
      child.stdout.setEncoding("utf8");
      child.stderr.setEncoding("utf8");
      child.stdout.on("data", (chunk: string) => {
        size += Buffer.byteLength(chunk);
        if (size > 1024 * 1024) {
          child.kill();
          reject(new Error("SeedEnv response exceeded 1 MiB; request a smaller page"));
        } else stdout += chunk;
      });
      child.stderr.on("data", (chunk: string) => { stderr = (stderr + chunk).slice(-6000); });
      child.on("error", reject);
      child.on("close", (code) => {
        if (code !== 0) return reject(new Error(stderr || `SeedEnv exited with status ${code}`));
        try { resolve((text ? stdout : JSON.parse(stdout)) as T); }
        catch (error) { reject(error); }
      });
    });
  }

  browse(field?: string, signal?: AbortSignal) {
    return this.request<Navigation>(["browse", ...(field ? ["--field", field] : [])], signal);
  }
  search(query = "", offset = 0, limit = 20, signal?: AbortSignal, scope: SearchScope = {}) {
    return this.request<{items: ModuleSummary[]; total: number; next_offset: number | null}>(
      ["search", "--offset", String(offset), "--limit", String(limit),
       ...(scope.field ? ["--field", scope.field] : []), ...(scope.direction ? ["--direction", scope.direction] : []), "--", query], signal);
  }
  show(name: string, signal?: AbortSignal) { return this.request<Record<string, unknown>>(["show", name], signal); }
  guide(name: string, signal?: AbortSignal) { return this.request<string>(["guide", name], signal, true); }
  example(name: string, signal?: AbortSignal) { return this.request<ResearchExample>(["example", name], signal); }
  context(selections: string[], signal?: AbortSignal) { return this.request<ResearchContext>(["context", ...selections], signal); }
  discover(selections: string[], python?: string, signal?: AbortSignal) {
    return this.request<{found: {component: string; command: string[]; action: "bind"}[]}>(
      ["discover", ...selections, ...(python ? ["--python", python] : [])], signal);
  }
  plan(selections: string[], target?: Plan["target"], signal?: AbortSignal) {
    return this.request<Plan>(["plan", ...selections, ...(target ? ["--target", target] : [])], signal);
  }
  prepare(selections: string[], signal?: AbortSignal) {
    return this.request<PreparationStart>(["prepare", ...selections, "--background"], signal);
  }
  status(job: string, signal?: AbortSignal) { return this.request<Preparation>(["status", job], signal); }
  cancel(job: string, signal?: AbortSignal) { return this.request<{job: string; state: string}>(["cancel", job], signal); }
  installed(signal?: AbortSignal) { return this.request<unknown[]>(["installed"], signal); }
  bind(component: string, command: string[], signal?: AbortSignal) {
    return this.request<Record<string, unknown>>(["bind", component, "--", ...command], signal);
  }
  entry(component: string, signal?: AbortSignal) {
    return this.request<{component: string; command: string[]; location: string}>(["entry", component], signal);
  }
  connect(host: "origo" | "mcp", output: string, selections?: string[], signal?: AbortSignal) {
    return this.request<{host: string; path: string; modules: string[]; installed: false; next: string}>(
      ["connect", host, "--output", output, ...(selections ? ["--modules", ...selections] : [])], signal);
  }
  origoPlan(selections: string[], signal?: AbortSignal) {
    return this.request<{modules: string[]; installation_root: string; preparations: OrigoPreparation[]; connections: PlanAction[]}>(
      ["plan", ...selections, "--host", "origo"], signal);
  }
}
