#!/bin/bash

for directory in $(echo "$PATH" | tr ':' '\n') ;
do
    if [[ -d "$directory" ]] ;
    then
        count=$(find "$directory" -maxdepth 1 -type f 2>/dev/null | wc -l)
        echo "$directory => $count"
    fi
done
