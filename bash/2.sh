#!/bin/bash

file=$1
dirToWrite=$2

if ! test -d $file ; then
        echo "256";
        exit 1
fi

if ! test -d $dirToWrite ; then
        echo "256";
        exit 1
fi

find $file -maxdepth 1 ! -name $file -type d -exec basename {} \; | while read saved;
        do
                filename=$2/$saved.txt;
                touch $filename;
                echo "$(ls $1/$saved | wc -l)" >> $filename;
        done
