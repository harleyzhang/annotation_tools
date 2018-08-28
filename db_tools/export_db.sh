#!/bin/bash

annotation_json_fname="testdb.json"

script_dir=$(dirname "$0")
ofname=$(realpath $script_dir)/$annotation_json_fname

echo $ofname

pushd $(pwd)
cd $script_dir/../


python -m annotation_tools.db_dataset_utils --action export \
--output $ofname \
--denormalize

popd

