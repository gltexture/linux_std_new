#!/bin/bash

if [[ "$FOO" == 5 && "$BAR" == 1 ]];
then
	exit 1
fi

while [[ ! -f fix.txt ]] ;
do
	sleep 1
done

echo "File"
