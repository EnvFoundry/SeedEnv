"""Run local research programs against software already prepared by SeedEnv."""
import argparse
import json
import subprocess
from seedenv import Manager

parser = argparse.ArgumentParser()
location = parser.add_mutually_exclusive_group()
location.add_argument('--home')
location.add_argument('--research-space')
parser.add_argument('--include-network', action='store_true')
parser.add_argument('modules', nargs='*', help='Run these examples; otherwise run examples with prepared software')
args = parser.parse_args()
manager = Manager(args.home, research_space=args.research_space)
unknown = set(args.modules) - manager.catalog.modules.keys()
if unknown:
    parser.error('Unknown modules: ' + ', '.join(sorted(unknown)))
failures = []
for name, module in manager.catalog.modules.items():
    if args.modules and name not in args.modules:
        continue
    example = module.get('example')
    if not example or not example['file'].endswith('.py'):
        if name in args.modules:
            failures.append(name)
            print(json.dumps({'module': name, 'error': 'No local Python example; see the working guide'}), flush=True)
        continue
    if name == 'references' and not args.include_network:
        continue
    try:
        command = manager.entry(example['component'])['command']
    except (ValueError, OSError) as error:
        if args.modules:
            failures.append(name)
            print(json.dumps({'module': name, 'error': str(error)}), flush=True)
        continue
    try:
        result = subprocess.run([*command, str(manager.catalog.resource(name, example['file']))],
                                capture_output=True, text=True, timeout=180)
        value = {'module': name, 'exit': result.returncode, 'output': result.stdout.strip()}
        if result.returncode:
            value['error'] = result.stderr[-3000:]
            failures.append(name)
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        failures.append(name)
        value = {'module': name, 'error': str(error)}
    print(json.dumps(value, ensure_ascii=False), flush=True)
raise SystemExit(bool(failures))
