#!/usr/bin/env python3
"""Rewrite the waxing Book Online buttons from waxing-links.json.

Every run clears the existing buttons first, so the JSON is the single
source of truth: nothing survives that is not currently listed there.
"""
import json, re, sys

BASE  = 'https://api.leadconnectorhq.com/booking/oz27FgTyetnlFEnG2O11/sv/'
FILES = ['services-menu-block.html', 'services-menu-preview.html', 'menu-artifact.html']
START, END = '<!-- DIVIDER - Waxing<br>for Women. -->', '<div class="page closing-page">'

links = {k: v for k, v in json.load(open('waxing-links.json')).items()
         if not k.startswith('_')}
ids = [v['id'] for v in links.values()]
dupe = {i for i in ids if ids.count(i) > 1}
if dupe:
    sys.exit(f"ERROR: same link on more than one service: {dupe}")

ROW    = re.compile(r'(<div class="service-row">.*?</div>\s*</div>)', re.S)
ONLINE = re.compile(r'\n\s*<a class="book-btn book-btn-online"[^>]*>Book Online</a>')
used, unlinked = set(), []

for f in FILES:
    h = open(f).read()
    s, e = h.index(START), h.index(END)
    def fix(m):
        blk  = ONLINE.sub('', m.group(1))
        name = re.search(r'service-name">(.*?)</div>', blk).group(1).replace('&amp;', '&').strip()
        price= re.search(r'service-price">(.*?)</div>', blk).group(1).strip()
        key  = f"{name}|{price}"
        if key not in links:
            if f == FILES[0]: unlinked.append(key)
            return blk
        used.add(key)
        btn = (f'\n        <a class="book-btn book-btn-online" href="{BASE}{links[key]["id"]}"'
               f' target="_blank" rel="noopener">Book Online</a>')
        return blk.replace('</a>\n      </div>', '</a>' + btn + '\n      </div>', 1)
    open(f, 'w').write(h[:s] + ROW.sub(fix, h[s:e]) + h[e:])

    body = open(f).read()
    if body.count('<div') != body.count('</div>') or body.count('<a ') != body.count('</a>'):
        sys.exit(f"ERROR: unbalanced tags in {f}")

print(f"linked {len(used)} waxing rows; {len(links)-len(used)} JSON entries matched nothing")
for k in links:
    if k not in used:
        print(f"  UNMATCHED KEY: {k}")
print(f"\nstill without a link ({len(unlinked)}):")
for k in unlinked:
    print("  " + k.replace('|', '  '))
