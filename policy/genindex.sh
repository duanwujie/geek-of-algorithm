#!/bin/bash


index_head(){
cat <<EOF > index.rst.in
Hacking Kernel
===========================

.. toctree::
   :maxdepth: 3
   :numbered:



EOF
}


index_head
for x in `ls -1d */`
do
    if [[ "$x" != "_build/" && "$x" != "images/" ]] ; then
        for y in `ls $x*.rst`
        do
            echo  "   ${y%%.*}" >> index.rst.in
        done

    fi
done
