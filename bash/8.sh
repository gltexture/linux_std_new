#!/bin/bash

lc_vars=$(env | grep "^LC_")

first=$(echo "$lc_vars" | head -n 1 | cut -d '=' -f2)

while IFS= read -r line;
do
    value=$(echo "$line" | cut -d '=' -f2)
    if [ "$value" != "$first" ]; then
        exit 1
    fi
done <<< "$lc_vars"
