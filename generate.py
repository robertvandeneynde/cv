#!/usr/bin/env python3
import re

def list_get(L, i, default=''):
    try:
        return L[i]
    except IndexError:
        return default

from generate_utils import OutFile

for filename in ('cv.html', ): # 'cv-edu.html'):
  base = filename.split('.')[0]
  with open(f'{base}.html') as f:
    s = f.read();

  R = re.compile('{{(.*?)}}', re.DOTALL)

  for i, lang in enumerate(('fr', 'en', 'ru')):
    with OutFile(f'{base}.{lang}.html', 'w') as f:
        f.write(R.sub(lambda m: list_get(m.group(1).split('|'), i, default="NOT TRANSLATED"), s))
