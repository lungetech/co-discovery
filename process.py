#!/usr/bin/env python

import sys
import json
import numpy


def process(data):
    for entry in sorted(data, key=lambda x: (x['year'], x['title'])):
        print "%d - %s" % (entry['year'], entry['title'])

        dups = 0
        solved = 0
        for item in entry['results']:
            if entry['results'][item]:
                solved += 1
            if entry['results'][item] > 1:
                dups += 1

        print "%3.2f%% were identified by more than one entity (%d of %d)" % (
            float(dups) / solved * 100, dups, solved)

        if entry['type'] == 'CTF':
            likely = []
            for item in entry['results']:
                if entry['results'][item]:
                    likely.append(
                        float(entry['results'][item]) / entry['teams'] * 100)

            print "%3.2f%% chance in co-discovery" % numpy.mean(likely)
            # print json.dumps(entry, sort_keys=True, indent=4)

        print ""


def main():
    data = []
    for filename in sys.argv[1:]:
        with open(filename, 'r') as fh:
            data += json.load(fh)

    process(data)


main()
