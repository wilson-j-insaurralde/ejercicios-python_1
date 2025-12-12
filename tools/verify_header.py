#!/usr/bin/env python3
"""
Verifica que todos los archivos .py contienen la cabecera de autor.
Sale con código 1 si alguno no la contiene.
"""
from pathlib import Path
import sys
import re

HEADER_TEST = re.compile(r"Autor: Wilson J\. Insaurralde")


def should_skip(p: Path) -> bool:
    parts = {x.lower() for x in p.parts}
    if 'venv' in parts or '.venv' in parts or '__pycache__' in parts:
        return True
    if p.name in {'add_header.py', 'verify_header.py'}:
        return True
    return False


def main() -> int:
    root = Path('.').resolve()
    missing = []
    for p in root.rglob('*.py'):
        if should_skip(p):
            continue
        try:
            text = p.read_text(encoding='utf-8')
        except Exception:
            continue
        if not HEADER_TEST.search(text):
            missing.append(str(p))

    if missing:
        print('ERROR: Los siguientes archivos no tienen la cabecera de autor:')
        for m in missing:
            print(' -', m)
        print('\nPor favor, añade la cabecera o usa tools/add_header.py para automatizarlo.')
        return 1
    print('OK: Todos los archivos .py contienen la cabecera de autor')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
