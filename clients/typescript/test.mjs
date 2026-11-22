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
    assert.equal((await api.browse('optics')).directions.some(d => d.id === 'optoelectronic-devices'), true);
    assert.equal((await api.plan(['thin-films', 'thin-films'])).actions.length, 1);
    const requests = (await api.origoPlan(['thin-films'])).preparations;
    assert.deepEqual(requests[0].request.requirements, ['tmm', 'numpy']);
    const devices = await api.search('', 0, 100, undefined, {field:'optics',direction:'optoelectronic-devices'});
    assert.ok(devices.items.some(m => m.id === 'semiconductor-transport'));
    assert.ok(!devices.items.some(m => m.id === 'fiber-pulses'));
    await assert.rejects(api.plan(['optics']), /is a field/);
    await assert.rejects(api.plan(['unknown-module']), /Unknown module/);
    assert.equal((await api.search('$(touch forbidden);')).items.length, 0);
    assert.equal((await api.search('--a-search-term')).items.length, 0);
    assert.deepEqual((await api.plan([])).actions, []);
    assert.equal((await api.prepare([])).job, null);
    assert.equal((await api.context(['thin-films'])).modules[0].id, 'thin-films');
    assert.match((await api.example('thin-films')).content, /coh_tmm/);
    assert.equal((await api.browse('optics')).resources.some(m => m.id === 'optical-lab'), true);
    const lab = await api.plan(['source-measure-sweeps', 'temperature-control']);
    assert.equal(lab.actions.filter(a => a.component === 'python-pymeasure').length, 1);
    const connection = lab.actions.find(a => a.connection?.type === 'laboratory');
    assert.equal(connection.action, 'configure-connector');
    assert.deepEqual(connection.modules, ['source-measure-sweeps', 'temperature-control']);
  } finally { await rm(home, { recursive: true, force: true }); }
});

test('Picker reviews software before starting and reports completion', async () => {
  const dom = new JSDOM('<!doctype html><body></body>');
  for (const name of ['HTMLElement', 'customElements', 'document', 'CustomEvent']) globalThis[name] = dom.window[name];
  await import('./dist/picker.js');
  const picker = document.createElement('seedenv-picker'); picker.lang = 'zh';
  let starts = 0, reviewed;
  const fields = [{id:'optics',title:'光学',module_count:2},{id:'physics',title:'物理',module_count:1}];
  const path = {field:'optics',field_title:'光学',direction:'films',direction_title:'薄膜'};
  const thin = {id:'thin-films',title:'薄膜',summary:'多层膜',components:['python-tmm'],includes:[],tags:[],paths:[path],software:[{id:'python-tmm',title:'tmm',kind:'python'}]};
  const quantum = {...thin,id:'quantum',title:'量子态',components:['python-quantum'],software:[{id:'python-quantum',title:'QuTiP',kind:'python'}]};
  picker.api = {
    browse: async field => ({fields,field,directions:field?[{id:'films',title:'薄膜',module_count:1},{id:'quantum',title:'量子',module_count:1}]:[]}),
    search: async (query,offset,limit,signal,scope) => ({ items: [scope?.field === 'physics' || scope?.direction === 'quantum' ? quantum : thin], total:1,next_offset:null }),
    plan: async selections => { reviewed=selections; return { modules:selections,target:'linux',guides:[],actions:[{component:'python-tmm',title:'tmm',kind:'python',action:'install',requirements:['tmm']}],storage:{root:'/user-space/system/seedenv',new_environments:1,reused_environments:0,download_bytes:null,additional_disk_bytes:null,free_bytes:1000} }; },
    prepare: async () => { starts++; return { job: 'demo', state: 'queued' }; },
    status: async () => ({ id: 'demo', state: 'ready', selection: ['thin-films'], result: { ready: [], pending: [], failed: [] }, error: null }),
    cancel: async () => ({ job: 'demo', state: 'cancelled' }),
  };
  document.body.append(picker);
  await new Promise(resolve => setImmediate(resolve));
  const root = picker.shadowRoot;
  assert.equal(root.querySelectorAll('input[type=checkbox]').length, 0);
  let skips = 0;
  picker.addEventListener('seedenv-skip', () => skips++);
  [...root.querySelectorAll('button')].find(x => x.textContent === '以后再准备').click();
  assert.equal(skips, 1);
  assert.equal(starts, 0);
  assert.equal([...root.querySelectorAll('button')].find(x => x.textContent === '查看准备内容').disabled, true);
  const field = root.querySelector('select[aria-label="研究领域"]');
  field.value='optics'; field.dispatchEvent(new dom.window.Event('change'));
  await new Promise(resolve => setImmediate(resolve));
  const checkbox = root.querySelector('input[type=checkbox]'); checkbox.click();
  assert.equal(starts, 0);
  field.value='physics'; field.dispatchEvent(new dom.window.Event('change'));
  await new Promise(resolve => setImmediate(resolve));
  root.querySelector('input[type=checkbox]').click();
  assert.match(root.querySelector('.basket').textContent, /薄膜/);
  assert.match(root.querySelector('.basket').textContent, /量子态/);
  // Selection survives navigation, and can be removed even while filtered out.
  [...root.querySelectorAll('.basket button')].find(x=>x.textContent.includes('量子态')).click();
  [...root.querySelectorAll('button')].find(x => x.textContent === '查看准备内容').click();
  await new Promise(resolve => setImmediate(resolve));
  assert.match(root.querySelector('.details').textContent, /tmm/);
  assert.deepEqual(reviewed,['thin-films']);
  assert.match(root.querySelector('.details').textContent, /system\/seedenv/);
  assert.match(root.querySelector('.details').textContent, /尚无体积估计/);
  const finished = new Promise(resolve => picker.addEventListener('seedenv-finished', resolve, { once: true }));
  [...root.querySelectorAll('button')].find(x => x.textContent === '准备研究环境').click();
  await finished;
  assert.equal(starts, 1);
  assert.equal(root.querySelector('[role=status]').textContent, '可以开始使用');
  let polls = 0;
  picker.api.status = async () => {
    if (++polls === 1) throw new Error('Temporary connection interruption');
    return {id:'persisted', state:'ready', selection:['thin-films'], result:{ready:[],pending:[],failed:[]},error:null};
  };
  picker.resume('persisted');
  await new Promise(resolve => setImmediate(resolve));
  const retry = [...root.querySelectorAll('button')].find(x => x.textContent === '重新读取进度');
  assert.equal(retry.hidden, false);
  retry.click();
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(root.querySelector('[role=status]').textContent, '可以开始使用');
  assert.equal(starts, 1); // Reopening and reading progress never reinstalls software.
  picker.remove(); dom.window.close();
});
