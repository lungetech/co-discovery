#!/bin/bash

mkdir -p data
for i in progress; do
    if [ ! -f data/$i ]; then
        curl https://microcorruption.com/hall_of_fame/$i -o data/$i
    fi
done

python process.py > results.json
