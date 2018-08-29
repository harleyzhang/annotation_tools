#!/bin/bash

# this script test adding an image by URL to the dataset

#img_url='https://images-na.ssl-images-amazon.aksdg.com/images/I/jkgja71Mem-06i0L.jpg'
img_url='https://images-na.ssl-images-amazon.com/images/I/71Mem-06i0L._SY450_.jpg'

script_dir=$(dirname "$0")
root_dir=$(realpath $script_dir)/../


PYTHONPATH=$root_dir python -m annotation_tools.db_dataset_utils --action add_img \
  --img_url $img_url


