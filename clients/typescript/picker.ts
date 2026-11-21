import type { ModuleSummary, Navigation, Plan, Preparation, SearchScope } from "./index.js";

/** Implement this bridge in the product. No credentials or shell live in the UI. */
export interface ResearchEnvironmentAPI {
  browse(field?: string): Promise<Navigation>;
  search(query?: string, offset?: number, limit?: number, signal?: AbortSignal, scope?: SearchScope): Promise<{ items: ModuleSummary[]; total: number; next_offset: number | null }>;
  plan(selections: string[]): Promise<Plan>;
  prepare(selections: string[]): Promise<{ job: string; state: string }>;
  status(job: string): Promise<Preparation>;
  cancel(job: string): Promise<{ job: string; state: string }>;
}

const words = {
  en: { title: "Research environments", intro: "Choose what you need now. You can add more later.", search: "Search by task, field or software", selected: "selected", plan: "Review selection", prepare: "Prepare environments", skip: "Set up later", cancel: "Cancel preparation", loading: "Loading modules…", empty: "No matching modules", error: "Unable to complete this step", ready: "Ready to use", partial: "Some tools need another step", cancelled: "Preparation cancelled", failed: "Preparation failed", running: "Preparing environments…", install: "Install", reuse: "Use existing", connect: "Connect existing", setup: "Setup needed", "choose-host": "Choose a supported host", "add-plugin": "Add plugin", more: "Show more", guide: "Preparation details" },
  zh: { title: "研究环境", intro: "选择现在需要的模块，以后可以随时补充。", search: "搜索研究任务、领域或软件", selected: "项已选", plan: "查看准备内容", prepare: "准备研究环境", skip: "以后再准备", cancel: "取消准备", loading: "正在读取模块…", empty: "没有找到相关模块", error: "这一步未能完成", ready: "可以开始使用", partial: "部分工具需要继续配置", cancelled: "已取消准备", failed: "准备未完成", running: "正在准备研究环境…", install: "安装", reuse: "复用已有环境", connect: "连接已有软件", setup: "需要配置", "choose-host": "选择可用的运行位置", "add-plugin": "添加插件", more: "显示更多", guide: "准备内容" },
};
const navigationWords = {
  en: { field: "Research field", direction: "Research direction", allFields: "Choose a field or search", allDirections: "All directions in this field", choose: "Choose a field, then select only the modules needed for your work.", software: "Software", remove: "Remove", location: "Software location", new: "new environments", reused: "existing environments reused", size: "Download and additional disk size depend on the selected host and dependency resolution; no size estimate is available yet." },
  zh: { field: "研究领域", direction: "研究方向", allFields: "选择领域，或直接搜索", allDirections: "本领域全部方向", choose: "先选择领域，再勾选研究任务需要的模块。浏览领域不会下载安装。", software: "软件", remove: "移除", location: "软件保存位置", new: "个新环境", reused: "个已有环境可复用", size: "下载量和新增空间取决于运行位置及依赖解析，目前尚无体积估计。" },
};

/** Embeddable in onboarding and settings; the same component serves both. */
export class SeedEnvPicker extends HTMLElement {
  private bridge?: ResearchEnvironmentAPI;
  private selected = new Set<string>();
  private selectedTitles = new Map<string, string>();
  private scope: SearchScope = {};
  private fields!: HTMLSelectElement;
  private directions!: HTMLSelectElement;
  private basket!: HTMLElement;
  private items: ModuleSummary[] = [];
  private query = "";
  private offset: number | null = 0;
  private revision = 0;
  private navigationRevision = 0;
  private poll?: ReturnType<typeof setTimeout>;
  private job?: string;
  private busy = false;
  private currentPlan?: Plan;
  private message = "";
  private list!: HTMLElement;
  private summary!: HTMLElement;
  private detail!: HTMLElement;
  private live!: HTMLElement;
  private review!: HTMLButtonElement;
  private prepareButton!: HTMLButtonElement;
  private more!: HTMLButtonElement;
  private cancelButton!: HTMLButtonElement;

  constructor() { super(); this.attachShadow({ mode: "open" }); }
  set api(value: ResearchEnvironmentAPI | undefined) { this.bridge = value; if (this.isConnected) void this.navigate(); }
  get api(): ResearchEnvironmentAPI | undefined { return this.bridge; }
  private get t() { return words[this.getAttribute("lang")?.startsWith("zh") ? "zh" : "en"]; }
  private get n() { return navigationWords[this.getAttribute("lang")?.startsWith("zh") ? "zh" : "en"]; }
  private label(title: string) {
    const [en, zh] = title.split(" · ");
    return this.getAttribute("lang")?.startsWith("zh") ? (zh ?? en) : en;
  }

  connectedCallback() {
    this.renderShell();
    if (this.bridge) void this.navigate();
    if (this.job) void this.checkProgress();
  }
  disconnectedCallback() { this.revision++; this.navigationRevision++; clearTimeout(this.poll); }

  private element<K extends keyof HTMLElementTagNameMap>(tag: K, text = "") {
    const element = document.createElement(tag); element.textContent = text; return element;
  }
  private button(text: string, action: () => void) {
    const button = this.element("button", text); button.type = "button";
    button.addEventListener("click", action); return button;
  }
  private renderShell() {
    const root = this.shadowRoot!;
    root.replaceChildren();
    const style = this.element("style", `
      :host{display:block;color:inherit;font:inherit;max-width:52rem}*{box-sizing:border-box}
      h2{font-size:1.35rem;margin:0 0 .5rem}p{line-height:1.6}input,button,select{font:inherit}
      .navigation{display:flex;gap:.75rem;flex-wrap:wrap;margin:1rem 0}.navigation select{padding:.65rem;max-width:100%;background:transparent;color:inherit;border:1px solid #a5afb8;border-radius:.4rem}
      .basket{display:flex;gap:.4rem;flex-wrap:wrap}.basket button{font-size:.85rem;padding:.4rem}.storage{overflow-wrap:anywhere}
      input[type=search]{width:100%;padding:.75rem;border:1px solid #a5afb8;border-radius:.5rem;margin:.5rem 0 1rem}
      .modules{display:grid;grid-template-columns:repeat(auto-fit,minmax(16rem,1fr));gap:.65rem}
      label{display:flex;gap:.7rem;align-items:flex-start;border:1px solid #a5afb8;border-radius:.5rem;padding:.85rem;cursor:pointer}
      label:has(input:checked){border-color:#267b78;background:#267b7810}label small{display:block;line-height:1.5;margin-top:.3rem;opacity:.8}
      input[type=checkbox]{margin-top:.3rem;accent-color:#267b78}button{padding:.65rem .9rem;border:1px solid #a5afb8;border-radius:.4rem;background:transparent;color:inherit;cursor:pointer}
      button:disabled{opacity:.5;cursor:default}button.primary{background:#246f6c;color:#fff;border-color:#246f6c}
      .actions{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:1rem}.details{margin:1rem 0}.row{padding:.5rem 0;border-bottom:1px solid #a5afb840}
      .row small{display:block;line-height:1.6;overflow-wrap:anywhere}a{color:#246f6c} [hidden]{display:none!important}
      :focus-visible{outline:2px solid #267b78;outline-offset:3px}`);
    const title = this.element("h2", this.t.title);
    const intro = this.element("p", this.t.intro);
    const navigation = this.element("div"); navigation.className = "navigation";
    this.fields = this.element("select"); this.fields.setAttribute("aria-label", this.n.field);
    this.directions = this.element("select"); this.directions.setAttribute("aria-label", this.n.direction);
    this.fields.addEventListener("change", () => { this.scope = this.fields.value ? { field: this.fields.value } : {}; void this.navigate(); });
    this.directions.addEventListener("change", () => { this.scope.direction = this.directions.value || undefined; void this.load(true); });
    navigation.append(this.fields, this.directions);
    const search = this.element("input"); search.type = "search"; search.value = this.query;
    search.placeholder = this.t.search; search.setAttribute("aria-label", this.t.search);
    search.addEventListener("input", () => { this.query = search.value; void this.load(true); });
    this.list = this.element("div"); this.list.className = "modules";
    this.more = this.button(this.t.more, () => void this.load(false));
    this.summary = this.element("p");
    this.basket = this.element("div"); this.basket.className = "basket";
    this.detail = this.element("div"); this.detail.className = "details";
    this.live = this.element("p"); this.live.setAttribute("role", "status"); this.live.setAttribute("aria-live", "polite");
    const actions = this.element("div"); actions.className = "actions";
    this.review = this.button(this.t.plan, () => void this.reviewPlan());
    this.prepareButton = this.button(this.t.prepare, () => void this.begin()); this.prepareButton.className = "primary";
    this.cancelButton = this.button(this.t.cancel, () => void this.cancel());
    actions.append(this.review, this.prepareButton, this.cancelButton,
      this.button(this.t.skip, () => this.dispatchEvent(new CustomEvent("seedenv-skip", { bubbles: true, composed: true }))));
    root.append(style, title, intro, navigation, search, this.list, this.more, this.summary, this.basket, this.detail, actions, this.live);
    this.update();
  }
  private update() {
    this.summary.textContent = `${this.selected.size} ${this.t.selected}`;
    this.basket.replaceChildren();
    for (const name of this.selected) {
      const remove = this.button(`${this.n.remove} · ${this.selectedTitles.get(name) ?? name}`, () => {
        this.selected.delete(name); this.invalidatePlan();
        for (const input of this.list.querySelectorAll<HTMLInputElement>("input[type=checkbox]")) input.checked = this.selected.has(input.value);
      });
      remove.disabled = this.busy; this.basket.append(remove);
    }
    this.review.disabled = !this.selected.size || this.busy;
    this.prepareButton.hidden = !this.currentPlan;
    this.prepareButton.disabled = this.busy;
    this.cancelButton.hidden = !this.job || !this.busy;
    this.more.hidden = this.offset === null;
    this.live.textContent = this.message;
    for (const input of this.list.querySelectorAll("input")) input.disabled = this.busy;
    this.fields.disabled = this.busy;
    this.directions.disabled = this.busy || !this.scope.field;
  }
  private invalidatePlan() { this.currentPlan = undefined; this.detail.replaceChildren(); this.message = ""; this.update(); }
  private async navigate() {
    if (!this.bridge) return;
    const revision = ++this.navigationRevision;
    this.revision++;
    try {
      const navigation = await this.bridge.browse(this.scope.field);
      if (revision !== this.navigationRevision || !this.isConnected) return;
      const fill = (select: HTMLSelectElement, title: string, items: Navigation["fields"], value?: string) => {
        const blank = this.element("option", title); blank.value = "";
        select.replaceChildren(blank);
        for (const item of items) { const option = this.element("option", `${this.label(item.title)} (${item.module_count})`); option.value = item.id; select.append(option); }
        select.value = value ?? "";
      };
      fill(this.fields, this.n.allFields, navigation.fields, this.scope.field);
      fill(this.directions, this.n.allDirections, navigation.directions, this.scope.direction);
      await this.load(true);
    } catch (error) { if (revision === this.navigationRevision) this.fail(error); }
  }
  private async load(reset: boolean) {
    if (!this.bridge) return;
    const revision = ++this.revision;
    if (reset) { this.items = []; this.offset = 0; }
    if (!this.scope.field && !this.query.trim()) {
      this.list.replaceChildren(this.element("p", this.n.choose)); this.offset = null; this.update(); return;
    }
    if (this.offset === null) return;
    try {
      const result = await this.bridge.search(this.query, this.offset, 30, undefined, { ...this.scope });
      if (revision !== this.revision || !this.isConnected) return;
      this.items.push(...result.items); this.offset = result.next_offset;
      this.list.replaceChildren();
      for (const item of this.items) {
        const label = this.element("label");
        const input = this.element("input"); input.type = "checkbox"; input.value = item.id; input.checked = this.selected.has(item.id);
        input.addEventListener("change", () => {
          if (input.checked) this.selected.add(item.id); else this.selected.delete(item.id);
          this.selectedTitles.set(item.id, this.label(item.title)); this.invalidatePlan();
        });
        const text = this.element("span", this.label(item.title));
        text.append(this.element("small", this.getAttribute("lang")?.startsWith("zh") ? item.summary : (item.summary_en ?? item.summary)));
        const path = item.paths?.find(p => p.field === this.scope.field) ?? item.paths?.[0];
        if (path) text.append(this.element("small", `${this.label(path.field_title)} › ${this.label(path.direction_title)}`));
        text.append(this.element("small", `${this.n.software}: ${item.software.map(s => this.label(s.title)).join(", ")}`));
        label.append(input, text); this.list.append(label);
      }
      if (!this.items.length) this.list.append(this.element("p", this.t.empty));
      this.update();
    } catch (error) { if (revision === this.revision) this.fail(error); }
  }
  private fail(error: unknown) { this.message = `${this.t.error}: ${error instanceof Error ? error.message : String(error)}`; this.update(); }
  private async reviewPlan() {
    if (!this.bridge || this.busy) return;
    this.busy = true; this.update();
    try {
      this.currentPlan = await this.bridge.plan([...this.selected]);
      this.showActions(this.currentPlan.actions);
      const storage = this.currentPlan.storage;
      const location = this.element("p", `${this.n.location}: ${storage.root}`); location.className = "storage";
      this.detail.append(location,
        this.element("p", `${storage.new_environments} ${this.n.new} · ${storage.reused_environments} ${this.n.reused}`),
        this.element("small", storage.download_bytes === 0 ? (this.getAttribute("lang")?.startsWith("zh") ? "已有软件可直接复用，无需下载。" : "Existing software is ready to reuse; no download is needed.") : this.n.size));
    } catch (error) { this.fail(error); }
    finally { this.busy = false; this.update(); }
  }
  private showActions(actions: Plan["actions"]) {
    this.detail.replaceChildren(this.element("h3", this.t.guide));
    for (const action of actions) {
      const label = action.action === "configure-connector" ? this.t.setup : this.t[action.action];
      const row = this.element("div", `${this.label(action.title)} · ${label}`); row.className = "row";
      if (action.requirements?.length) {
        const names = action.requirements.map(r => r.match(/^[A-Za-z0-9_.-]+(?:\[[^\]]+\])?/)?.[0] ?? r);
        row.append(this.element("small", [...new Set(names)].join(", ")));
      }
      if (action.instructions) row.append(this.element("small", action.instructions));
      this.detail.append(row);
    }
  }
  private async begin() {
    if (!this.bridge || !this.currentPlan || this.busy) return;
    this.busy = true; this.message = this.t.running; this.update();
    try {
      const job = await this.bridge.prepare([...this.selected]); this.job = job.job; this.update();
      this.dispatchEvent(new CustomEvent("seedenv-started", { detail: job, bubbles: true, composed: true }));
      await this.checkProgress();
    } catch (error) { this.busy = false; this.fail(error); }
  }
  private async checkProgress() {
    if (!this.job || !this.bridge || !this.isConnected) return;
    try {
      const status = await this.bridge.status(this.job);
      if (["queued", "running"].includes(status.state)) {
        this.poll = setTimeout(() => void this.checkProgress(), 1000); return;
      }
      this.busy = false;
      this.message = this.t[status.state as "ready" | "partial" | "cancelled" | "failed"];
      if (status.error) this.message += `: ${status.error}`;
      if (status.result?.pending.length) this.showActions(status.result.pending);
      for (const failure of status.result?.failed ?? []) this.detail.append(this.element("p", `${failure.component}: ${failure.error}`));
      this.dispatchEvent(new CustomEvent("seedenv-finished", { detail: status, bubbles: true, composed: true }));
      this.update();
    } catch (error) { this.busy = false; this.fail(error); }
  }
  private async cancel() {
    if (!this.bridge || !this.job) return;
    try { await this.bridge.cancel(this.job); }
    catch (error) { this.fail(error); }
  }
}

if (!customElements.get("seedenv-picker")) customElements.define("seedenv-picker", SeedEnvPicker);
