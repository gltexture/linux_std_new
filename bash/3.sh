#!/bin/bash


files=$@

for file in "$@";
        do
                if test -f $file ; then
                        strokes=$(cat $file | wc -l);
                        echo "$file -> $strokes";
                else
                        echo "$file does not exist"
                fi
        done
