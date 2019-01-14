#!/bin/bash

script_dir=$(dirname "$0")

empty_db_fname=$(realpath $script_dir/empty_db.json)

pushd $(pwd)
cd $script_dir/../

pwd


python -m annotation_tools.db_dataset_utils --action load \
  --dataset $empty_db_fname \
  --normalize

popd
exit 0
