#!/usr/bin/python

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def process(data):
    results = set()
    for notice in data['notices']:
            if " solved " not in notice['body']:
                continue
            if '[' not in notice['body']:
                continue
            if not notice['body'].startswith("Your teammate"):
                continue
            body = notice['body']
            msg = body.split()
            cat_start = body.rindex('[')
            cat_end = body.rindex(']')

            category = body[cat_start+1:cat_end]
            solved = body.index('solved')
            player = body[len('Your teammate '):solved-1]
            challenge = body[solved+len('solved')+1:cat_start-1]
            entry = (player, category, challenge)
            results.add(entry)

    return results

def load(year, files):
    data = {}
    for fname in files:
            with open('%s/%s.json' % (year, fname), 'r') as fh:
                data[fname] = json.load(fh)
    return data

def only_these(results, categories):
    solved = {}
    ignoring = {}
    for result in results:
        if result[1] not in categories:
            continue
        if result[2] not in solved:
            solved[result[2]] = 0
        solved[result[2]] += 1

    return solved

def main():
    years = ['2013', '2014', '2015', '2016']
    files = ['notices', 'challenges', 'categories', 'teams']
    pwnage = [u'Web', u'HJ', u'Duchess', u'Vito Genovese', u'Pwnable', u'Selir', u'See Gee Sea', u'There I Fixed It', u'Gynophage', u'Lightning', u'censored', u'3dub', u'Jymbolia']

    for year in years:
        data = load(year, files)
        results = process(data)
        filtered = only_these(results, pwnage)
        print "%s - %d teams" % (year, len(data['teams']))
        print json.dumps(filtered, sort_keys=True, indent=4)

main()
