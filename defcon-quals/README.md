# Reproducing

    for i in 2013 2014 2015 2016; do
        mkdir -p $i
        for f in challenges categories notices teams users; do
            if [ ! -f $i/$f.json ]; then
                curl https://legitbs.net/statdump_$i/$f.json -o $i/$f.json
            fi
        done
    done

    python process.py
