#!/bin/bash

FILES=(key-procedure.dot)

function gen()
{
    dot -Tsvg $1 -o $2
}

function genpng()
{
    dot -Tpng $1 -o $2
}

function cgen()
{
    circo -Tsvg $1 -o $2
}

for i in ${FILES[*]}
do
    output=`basename $i .dot`
    gen $i $output.svg
    genpng $i $output.png
done

