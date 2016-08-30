#!/usr/bin/python

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def process(data):
    results = set()

    users = {}
    for user in data['users']:
        users[user['username']] = user['team_id']

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
        team = users[player]
        challenge = body[solved+len('solved')+1:cat_start-1]
        entry = (player, category, challenge, team)
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
    teams = set()

    for result in results:
        player, category, challenge, team = result
        teams.add(team)
        if category not in categories:
            continue
        if challenge not in solved:
            solved[challenge] = 0
        solved[challenge] += 1

    return solved, teams

def main():
    years = ['2013', '2014', '2015', '2016']
    files = ['notices', 'challenges', 'categories', 'teams', 'users']
    pwnage = [u'Web', u'HJ', u'Duchess', u'Vito Genovese', u'Pwnable', u'Selir', u'See Gee Sea', u'There I Fixed It', u'Gynophage', u'Lightning', u'censored', u'3dub', u'Jymbolia']

    output = []
    for year in years:
        data = load(year, files)
        results = process(data)
        filtered, teams = only_these(results, pwnage)
        output.append({
            'teams': len(teams),
            'year': int(year),
            'type': 'CTF',
            'title': 'DEFCON CTF Qualifier',
            'results': filtered})

    print json.dumps(output, sort_keys=True, indent=4)

main()
