#!/bin/bash

python -m annotation_tools.db_dataset_utils --action load \
--dataset ~/Downloads/annotations/person_keypoints_val2017.json \
--normalize
