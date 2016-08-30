#!/usr/bin/env python

import json
from lxml import html

def main():
    results = {}

    with open('data/progress', 'r') as fh:
        data = fh.read()
    tree = html.fromstring(data)

    teams = tree.xpath('//span[@class="highlight"]/text()')
    counts = tree.xpath('//span[@class="col-count"]/text()')
    levels = tree.xpath('//span[@class="col-level"]/text()')

    levels = [x[2:-1] for x in levels]
    for count, level in zip(counts, levels):
        results[level] = int(count)

    output = []

    output.append({
     'teams': int(teams[0]), 
      'year': 2016,
      'type': 'CTF',
      'title': 'Microcorruption',
      'results': results})

    print json.dumps(output, sort_keys=True, indent=4)

main()
