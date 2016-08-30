#!/bin/bash

mkdir -p data
for i in 2015-data.json ; do
    if [ ! -f data/$i ]; then
        curl https://ictf.cs.ucsb.edu/ictfdata/2015/scoreboard/$i -o data/$i
    fi
done

python process.py > results.json
