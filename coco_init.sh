#!/bin/bash


annotation_fname=/home/honglei/Data/Coco/annotations/person_keypoints_val2017.json


python -m annotation_tools.db_dataset_utils --action load \
--dataset $annotation_fname \
--normalize
