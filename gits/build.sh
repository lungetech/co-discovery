#!/bin/bash

mkdir -p data
for i in team-solves.txt solve-counts.txt; do
    if [ ! -f data/$i ]; then
        curl http://ghostintheshellcode.com/2014-final/$i -o data/$i
    fi
done

python process.py > results.json
