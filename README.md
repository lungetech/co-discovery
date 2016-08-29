# co-discovery

# Reproducing

    for i in cgc-qualifier defcon-quals; do
        (cd $i && ./build.sh)
    done

    python process.py cgc-qualifier/results.json defcon-quals/results.json > results.txt


