#!/usr/bin/env python3
# coding: utf-8

import json
import os
from pathlib import Path

from mpkg.load import Load

for repo in ['main', 'extras', 'scoop', 'winget']:
    filename = f'{repo}.json'
    os.system(
        f'wget -q https://github.com/mpkg-project/mpkg-autobuild/releases/download/AutoBuild/{filename} -O {filename}')
    os.system(
        f'if [ -n "$(git diff {filename})" ]; then echo "$(date +%y%m%d)" > {filename}.ver; fi')

for repo in ['main', 'extras']:
    softs = Load(f'{repo}.json')[0]
    root = Path(repo)
    if not root.exists():
        root.mkdir()
    for soft in softs:
        with open(root/(soft['id']+'.json'), 'w', encoding='utf8') as f:
            f.write(json.dumps(soft, indent=4))

os.system(f'wget -q https://github.com/mpkg-project/mpkg-autobuild/releases/download/AutoBuild/warning.txt -O warning.txt')
