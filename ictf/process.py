#!/usr/bin/env python

import json

def main():
    results = {}

    with open('data/2015-data.json', 'r') as fh:
        data = json.load(fh)

    for entry in data['dynamic']:
        for service in entry['exploited_services']:
            name = entry['exploited_services'][service]['service_name']
            teams = [x['team_name'] for x in entry['exploited_services'][service]['teams']]
            if name not in results:
                results[name] = set()

            results[name] |= set(teams)

    for name in results:
        results[name] = len(results[name])

    output = []

    output.append({
     'teams': len(data['static']['teams']),
      'year': 2015,
      'type': 'CTF',
      'title': 'iCTF',
      'results': results})

    print json.dumps(output, sort_keys=True, indent=4)

main()
