#!/usr/bin/env python

import json

def main():
    results = {}
    teams = set()

    with open('data/solve-counts.txt', 'r') as fh:
        for line in fh:
            if line.startswith('-'):
                continue
            data = line.split('|')
            name, count = [x.strip() for x in data]
            if name == 'name':
                continue
            if name.startswith('--'):
                continue
            if name in ['ti-1337', 'gitsmsg', 'Fuzzy', 'Byte Sexual']:
                results[name] = int(count)

    with open('data/team-solves.txt', 'r') as fh:
        for line in fh:
            if line.startswith('-'):
                continue
            if '|' not in line:
                continue
            data = line.split('|')
            data = [x.strip() for x in data]
            if data[0] == 'question_name':
                continue
            if data[0].startswith('-----'):
                continue
            teams.add(data[1])

    output = []

    output.append({
     'teams': len(teams),
      'year': 2014,
      'type': 'CTF',
      'title': 'Ghost in the Shellcode',
      'results': results})

    print json.dumps(output, sort_keys=True, indent=4)

main()
