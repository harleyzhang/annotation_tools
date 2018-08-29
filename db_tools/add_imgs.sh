#!/bin/bash

# this script read image URLs from a text file and add them the the dataset one by one

if [ "$#" -lt 1 ]; then
  echo "Please specify a text file with URLs on each line"
  exit 1
fi

fname=$1

echo $fname

script_dir=$(dirname "$0")
root_dir=$(realpath $script_dir)/../

while read line; do
  echo $line
  PYTHONPATH=$root_dir python -m annotation_tools.db_dataset_utils --action add_img \
   --img_url "$line"
done < $fname



