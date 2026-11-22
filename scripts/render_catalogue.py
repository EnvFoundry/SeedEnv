"""Render the public catalogue directly from the runtime's navigation data."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from seedenv.catalog import Catalog

catalog = Catalog()
overview = catalog.browse()
counts = overview['totals']
lines = ['# Research catalogue · 研究目录', '',
         'Fields and directions are navigation. Select individual tasks; shared software is prepared once.',
         '领域和方向用于导航。按任务选装，跨领域共享同一软件；关联资源单独展示。', '',
         f"{counts['modules']} distinct task modules · {counts['resources']} related resources / "
         f"{counts['modules']} 个不同任务模块 · {counts['resources']} 个关联资源", '',
         '| Entry / 入口 | Group / 类型 | Directions / 方向 | Distinct tasks / 不同任务 | Related resources / 关联资源 |',
         '| --- | --- | ---: | ---: | ---: |']
for field in overview['fields']:
    group = 'Shared / 公共能力' if field['kind'] == 'shared' else 'Research / 研究领域'
    lines.append(f"| {field['title']} | {group} | {field['direction_count']} | {field['module_count']} | {field['resource_count']} |")
lines += ['', 'Counts within a field deduplicate repeated tasks. A task can appear in several fields, so field counts do not sum to the global total.',
          '领域内按不同模块计数；同一模块可出现在多个领域，不能把各行相加作为全局模块数。', '',
          '“Prepare” identifies an installation route, not a claim that every platform has been exercised. '
          'Conda routes use an existing micromamba, mamba or conda. Native executables, accelerator runtimes and accounts retain their explicit connection steps.',
          '“安装”表示已有准备方式，不表示所有平台都已逐项运行。Conda 配方使用已有管理器；原生程序、加速运行环境与账户保留明确的连接步骤。']

def software_row(name):
    module = catalog.modules[name]
    _, ids = catalog.select([name])
    software = []
    for identity in ids:
        item = catalog.components[identity]
        mode = 'TinyTeX / bind' if item.get('preparer') == 'tex' else 'pip' if item['kind'] == 'python' else 'conda / bind' if item.get('conda') else {
            'environment': 'bind interpreter / 连接解释器', 'command': 'connect command / 连接程序',
            'connector': 'connect service / 连接服务', 'plugin': 'connect plugin / 连接插件'}[item['kind']]
        software.append(f"{item['title']} ({mode})")
    guide = '../src/seedenv/data/' + module['guide']
    return f"[{module['title']}]({guide}) · `{name}`", '; '.join(software)

for field in catalog.fields.values():
    lines += ['', '## ' + field['title'], '', '| Direction / 方向 | Task / 任务 | Software / 软件 |', '| --- | --- | --- |']
    for direction in field['directions']:
        for name in direction['modules']:
            if catalog.modules[name].get('hidden'): continue
            title, software = software_row(name)
            lines.append(f"| {direction['title']} | {title} | {software} |")
    if field.get('resources'):
        lines += ['', 'Related resources / 关联资源：', '']
        for name in field['resources']:
            title, software = software_row(name)
            lines.append(f'- {title} — {software}')
(ROOT / 'docs/catalogue.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
