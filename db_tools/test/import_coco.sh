#!/bin/bash

cd ../..

python -m annotation_tools.db_dataset_utils --action load \
--dataset /home/honglei/Data/Coco/annotations/person_keypoints_val2017.json \
--normalize

