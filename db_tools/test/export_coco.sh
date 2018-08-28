#!/bin/bash

cd ../..

python -m annotation_tools.db_dataset_utils --action export \
--output  /home/honglei/Dev/Pose/code/annotation_tools/db_tools/test/testdb.json \
--denormalize
