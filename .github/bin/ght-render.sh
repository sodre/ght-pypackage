#!/usr/bin/env bash
set -euf

GHT_CONF=.github/ght.yaml

render()
{
    in=$1
    out=$2
    ght_conf=${3:-$GHT_CONF}

    jinja2 \
        --format yaml\
        -e jinja2_time.TimeExtension \
        -o $out \
        $in $ght_conf
}

converged()
{
    diff -q $1 $2 > /dev/null
}

tree_converged()
{
    templ=$1;
    rendered=$2;

    # List all the types under the repo, ignoring the .git dir
    find . -path ./.git -prune -o ${@:3}  | grep -v '^\./\.git' | sort > ${templ}
    render $templ $rendered

    converged $templ $rendered
}

tmp=$(basename $(mktemp -t ght))
git checkout -b $tmp master

set -e
ght_temp=$(mktemp)
declare -i i=1
until converged $GHT_CONF $ght_temp; do
    echo "Pass $i"
    stop_rendering_lines=false
    mv $GHT_CONF $ght_temp
    while IFS= read line; do
        in=$(mktemp)
        printf "%s\n" "$line" > $in
        echo "Processing line '$line'"
        if [ "$stop_rendering_lines" == false ]; then
            echo "Rendering line '$line'"
            out=$(mktemp)
            render $in $out $ght_temp
            cat < $out >> $GHT_CONF
            if ! converged $in $out; then
                stop_rendering_lines=true
            fi
        else
          echo "Not rendering '$line'"
          cat < $in >> $GHT_CONF
        fi
    done < $ght_temp
    let i++
done
git commit -m "ght: configuration rendered" $GHT_CONF


for filter in "-type d" "-type f"; do
    ght_temp=$(mktemp)
    until tree_converged $ght_temp ${ght_temp}.rendered $filter ; do
        paste -- $ght_temp $ght_temp.rendered |
            while IFS=$'\t' read -r d1 d2; do
                if [ $d1 != $d2 ]; then
                  git mv $d1 $d2 || true
                fi
            done
    done
done
git commit -m 'ght: template structure rendered'

find . -path ./.git -prune -o -type f  |
    grep -v './.git' |
    sort |
    while IFS=$'\n' read -r in; do
        out=$(mktemp)
        echo "rendering ${in}"
        render $in $out
        cp -a ${out} ${in}
        git add ${in}
    done
git commit -m 'ght: rendered content'
