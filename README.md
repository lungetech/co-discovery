# co-discovery

# Reproducing

    DATA="gits cgc-qualifier defcon-quals"

    for i in $DATA; do
        (cd $i && ./build.sh)
    done

    python process.py `for i in $DATA; do echo $i/results.json; done` > results.txt
