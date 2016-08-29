# Reproducing

    for i in cqe_results-0d5587e0.zip; do
        if [ ! -f $i ]; then
            curl https://repo.cybergrandchallenge.com/cqe_results/$i -o $i
        fi
    done

    if [ ! -f cqe_results/CQE_SCORES.csv ]; then
        unzip cqe_results-0d5587e0.zip cqe_results/CQE_SCORES.csv
    fi

    python process.py > results.txt
