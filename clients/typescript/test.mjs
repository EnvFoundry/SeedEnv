import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve } from 'node:path';
import { SeedEnv } from './dist/index.js';
import { JSDOM } from 'jsdom';

test('TypeScript uses the real catalogue and host request format', async () => {
  const home = await mkdtemp(resolve(tmpdir(), 'seedenv-ts-'));
  try {
    const api = new SeedEnv({ command: [process.env.SEEDENV_TEST_PYTHON ?? 'python3'], home,
      env: { ...process.env, PYTHONPATH: resolve('../../src') } });
    assert.equal((await api.search('rdkit')).items[0].id, 'molecules');
    assert.equal((await api.plan(['optics', 'optics'])).actions.length, 1);
    const requests = (await api.origoPlan(['optics'])).preparations;
    assert.deepEqual(requests[0].request.requirements, ['tmm', 'miepython']);
    await assert.rejects(api.plan(['unknown-module']), /Unknown module/);
    assert.equal((await api.search('$(touch forbidden);')).items.length, 0);
  } finally { await rm(home, { recursive: true, force: true }); }
});

test('Picker reviews software before starting and reports completion', async () => {
  const dom = new JSDOM('<!doctype html><body></body>');
  for (const name of ['HTMLElement', 'customElements', 'document', 'CustomEvent']) globalThis[name] = dom.window[name];
  await import('./dist/picker.js');
  const picker = document.createElement('seedenv-picker'); picker.lang = 'zh';
  let starts = 0;
  picker.api = {
    search: async () => ({ items: [{ id: 'optics', title: '光学', summary: '薄膜与散射', components: ['python-optics'], includes: [], tags: [] }], total: 1, next_offset: null }),
    plan: async selections => ({ modules: selections, target: 'linux', guides: [], actions: [{ component: 'python-optics', title: 'tmm', kind: 'python', action: 'install', requirements: ['tmm'] }] }),
    prepare: async () => { starts++; return { job: 'demo', state: 'queued' }; },
    status: async () => ({ id: 'demo', state: 'ready', selection: ['optics'], result: { ready: [], pending: [], failed: [] }, error: null }),
    cancel: async () => ({ job: 'demo', state: 'cancelled' }),
  };
  document.body.append(picker);
  await new Promise(resolve => setImmediate(resolve));
  const root = picker.shadowRoot;
  const checkbox = root.querySelector('input[type=checkbox]'); checkbox.click();
  assert.equal(starts, 0);
  [...root.querySelectorAll('button')].find(x => x.textContent === '查看准备内容').click();
  await new Promise(resolve => setImmediate(resolve));
  assert.match(root.querySelector('.details').textContent, /tmm/);
  const finished = new Promise(resolve => picker.addEventListener('seedenv-finished', resolve, { once: true }));
  [...root.querySelectorAll('button')].find(x => x.textContent === '准备研究环境').click();
  await finished;
  assert.equal(starts, 1);
  assert.equal(root.querySelector('[role=status]').textContent, '可以开始使用');
  picker.remove(); dom.window.close();
});
