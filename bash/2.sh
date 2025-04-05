#!/bin/bash

if [ ! -e "$1" ]; then
    echo "256"
    exit 1
fi

for dir in "$1"/*/; do
    if [ -d "$dir" ]; then
        count=$(find $dir -maxdepth 1 | wc -l)
        echo "$count" >> $dir
    fi
done
