#!/usr/bin/env bash
set -euf

GHT_CONF=.github/ght.yaml

render()
{
    in=$1
    out=$2
    ght_conf=${3:-$GHT_CONF}

    created=false
    if [ ! -d $(dirname $in)/.github ]; then
        mkdir -p $(dirname $in)/.github/
        cp -af $(dirname $GHT_CONF)/ght $(dirname $in)/.github
        created=true
    fi
    jinja2 \
        --format yaml\
        -e jinja2_time.TimeExtension \
        -o $out \
        $in $ght_conf
    if $created; then
        rm -rf $(dirname $in)/.github
    fi
}

converged()
{
    diff -q $1 $2 > /dev/null
}

render_configuration()
{
    set -e
    ght_temp=$(mktemp)
    declare -i i=1
    until converged $GHT_CONF $ght_temp; do
        echo "Rendering $GHT_CONF: Pass $i"
        stop_rendering_lines=false
        mv $GHT_CONF $ght_temp
        while IFS= read line; do
            in=$(mktemp)
            printf "%s\n" "$line" > $in
            if [ "$stop_rendering_lines" == false ]; then
                out=$(mktemp)
                render $in $out $ght_temp
                cat < $out >> $GHT_CONF
                if ! converged $in $out; then
                    stop_rendering_lines=true
                fi
            else
              cat < $in >> $GHT_CONF
            fi
        done < $ght_temp
        let i++
    done
    #git commit -m "ght: configuration rendered" $GHT_CONF
}

# This is so we can test things locally without screwing up the master branch
# tmp=$(basename $(mktemp -t ght-XXXX))
# git checkout -b $tmp

cmd=${1//-/_}
if [ ! -z "$cmd" ]; then
    shift 1
    $cmd "$@"
    exit
fi
