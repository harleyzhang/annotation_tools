#!/bin/bash

if [ "$#" -lt 1 ]; then
  fname=testdb.json
else
  fname=$1
fi

#python -m json.tool $fname | less
python -m json.tool $fname > tmp.txt


