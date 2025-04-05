#!/bin/bash

directory=$1

if [ ! -d "$directory" ]; then
    echo "Error: Directory '$directory' does not exist."
    exit 1
fi

for subdir in "$directory"
do
    if [ -d "$subdir" ];
  then
        subdir_name=$(basename "$subdir")
        count=$(find "$subdir" -mindepth 1 -maxdepth 1 | wc -l)
        echo "$count" > "$directory/$subdir_name.txt"
    fi
done
