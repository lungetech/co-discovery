#!/usr/bin/env python

import json

def main():
    results = {}
    teams = set()

    with open('cqe_results/CQE_SCORES.csv', 'r') as fh:
        for line in fh:
            data = line.strip().split(',')
            if data[0] == 'TeamName':
                continue

            teams.add(data[0])

            name = data[1]
            evaluation = data[-1]

            if name not in results:
                results[name] = 0

            if evaluation == "2":
                results[name] += 1

    print "%d teams" % len(teams)
    print json.dumps(results, sort_keys=True, indent=4)

main()
