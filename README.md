# co-discovery

Co-discovering vulnerabilities in CTFs.  See [discussion](http://www.lungetech.com/2017/04/01/co-discovery/).

# Reproducing

    DATA="gits cgc-qualifier defcon-quals ictf microcorruption"

    for i in $DATA; do
        (cd $i && ./build.sh)
    done

    python process.py `for i in $DATA; do echo $i/results.json; done` > results.txt
