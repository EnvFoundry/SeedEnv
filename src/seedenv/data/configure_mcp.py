"""Configure a copied MCP package for this computer and its research space."""
import argparse
import json
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    location = parser.add_mutually_exclusive_group()
    location.add_argument('--research-space', help='User research space on this computer')
    location.add_argument('--home', help='Direct environment directory on this computer')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    environment = {}
    if args.research_space:
        environment['SEEDENV_HOME'] = str(Path(args.research_space).expanduser().absolute() / 'system' / 'seedenv')
    elif args.home:
        environment['SEEDENV_HOME'] = str(Path(args.home).expanduser().absolute())
    value = {'mcpServers': {'seedenv': {'command': sys.executable,
             'args': ['-B', str(root / 'server.py')], 'env': environment}}}
    config = root / 'mcp.json'
    config.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
    print(f'Import {config} into your agent host.')


if __name__ == '__main__':
    main()
