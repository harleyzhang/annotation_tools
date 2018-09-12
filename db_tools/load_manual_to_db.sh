#!/bin/bash

annotation_json_fname="manually_annot_baby.json"
annot_path=/home/honglei/Dev/Pose/code/annotation_tools


PYTHONPATH=$annot_path python -m annotation_tools.db_dataset_utils --action load \
--dataset $annotation_json_fname


