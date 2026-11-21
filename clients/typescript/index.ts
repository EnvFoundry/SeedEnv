import { spawn } from "node:child_process";

export interface ModuleSummary {
  id: string;
  title: string;
  summary: string;
  tags: string[];
  components: string[];
  includes: string[];
}
export interface PlanAction {
  component: string;
  title: string;
  kind: "python" | "command" | "plugin" | "connector";
  action: "reuse" | "install" | "connect" | "setup" | "choose-host" | "add-plugin" | "configure-connector";
  command?: string[] | null;
  requirements?: string[];
  instructions?: string;
  url?: string;
  connection?: Record<string, unknown>;
}
export interface Plan {
  modules: string[];
  target: "linux" | "darwin" | "windows";
  actions: PlanAction[];
  guides: { module: string; title: string }[];
}
export interface Preparation {
  id: string;
  state: "queued" | "running" | "ready" | "partial" | "cancelled" | "failed";
  selection: string[];
  result: { ready: unknown[]; pending: PlanAction[]; failed: { component: string; error: string }[] } | null;
  error: string | null;
  output?: string;
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
    catalog?: string;
    env?: NodeJS.ProcessEnv;
  }) {
    if (!options.command.length) throw new Error("Provide the Python command on the execution host");
  }

  private request<T>(args: string[], signal?: AbortSignal, text = false): Promise<T> {
    const [program, ...prefix] = this.options.command;
    const common = ["-m", "seedenv"];
    if (this.options.home) common.push("--home", this.options.home);
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

  search(query = "", offset = 0, limit = 20, signal?: AbortSignal) {
    return this.request<{items: ModuleSummary[]; total: number; next_offset: number | null}>(
      ["search", query, "--offset", String(offset), "--limit", String(limit)], signal);
  }
  show(name: string, signal?: AbortSignal) { return this.request<Record<string, unknown>>(["show", name], signal); }
  guide(name: string, signal?: AbortSignal) { return this.request<string>(["guide", name], signal, true); }
  plan(selections: string[], target?: Plan["target"], signal?: AbortSignal) {
    return this.request<Plan>(["plan", ...selections, ...(target ? ["--target", target] : [])], signal);
  }
  prepare(selections: string[], signal?: AbortSignal) {
    return this.request<{job: string; state: "queued"}>(["prepare", ...selections, "--background"], signal);
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
  origoPlan(selections: string[], signal?: AbortSignal) {
    return this.request<{modules: string[]; preparations: OrigoPreparation[]; connections: PlanAction[]}>(
      ["plan", ...selections, "--host", "origo"], signal);
  }
}
