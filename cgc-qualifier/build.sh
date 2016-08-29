#!/bin/bash

if [ ! -f cqe_results/CQE_SCORES.csv ]; then

    for i in cqe_results-0d5587e0.zip; do
        if [ ! -f $i ]; then
            curl https://repo.cybergrandchallenge.com/cqe_results/$i -o $i
        fi
    done

    unzip cqe_results-0d5587e0.zip cqe_results/CQE_SCORES.csv
    rm cqe_results-0d5587e0.zip
fi

python process.py > results.json
