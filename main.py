#!/usr/bin/env python3
# coding: utf-8

import json
import os
from pathlib import Path

from mpkg.load import Load

for repo in ['main', 'extras']:
    os.system(
        f'wget -q https://github.com/mpkg-project/mpkg-autobuild/releases/download/AutoBuild/{repo}.json -O {repo}.json')
    softs = Load(f'{repo}.json')[0]
    root = Path(repo)
    if not root.exists():
        root.mkdir()
    for soft in softs:
        with open(root/(soft['id']+'.json'), 'w', encoding='utf8') as f:
            f.write(json.dumps(soft, indent=4))

os.system(f'wget -q https://github.com/mpkg-project/mpkg-autobuild/releases/download/AutoBuild/warning.txt')
