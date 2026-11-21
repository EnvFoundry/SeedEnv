"""Run local research programs against software already prepared by SeedEnv."""
import argparse
import json
import subprocess
from seedenv import Manager

parser = argparse.ArgumentParser()
parser.add_argument('--home')
parser.add_argument('--include-network', action='store_true')
args = parser.parse_args()
manager = Manager(args.home)
failures = []
for name, module in manager.catalog.modules.items():
    example = module.get('example')
    if not example or not example['file'].endswith('.py'):
        continue
    if name == 'references' and not args.include_network:
        continue
    try:
        command = manager.entry(example['component'])['command']
        result = subprocess.run([*command, str(manager.catalog.resource(name, example['file']))],
                                capture_output=True, text=True, timeout=90)
        value = {'module': name, 'exit': result.returncode, 'output': result.stdout.strip()}
        if result.returncode:
            value['error'] = result.stderr[-3000:]
            failures.append(name)
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        failures.append(name)
        value = {'module': name, 'error': str(error)}
    print(json.dumps(value, ensure_ascii=False), flush=True)
raise SystemExit(bool(failures))
