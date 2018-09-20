#!/usr/bin/env python

# This script add images from a local hosted repository to the annotation database
# Note that this will copy images to another local directory and all image ids will be 
# regenerated again. 

import glob
import os

import sys

this_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(this_path)
print(root_path)
sys.path.append(root_path)

from annotation_tools import db_dataset_utils
from annotation_tools import annotation_tools



local_img_server="http://localhost:8007"
img_folder='/home/honglei/Data/Baby_carseat/images'


db = annotation_tools.get_db()


for f1 in sorted(glob.glob(os.path.join(img_folder, '*.jpg'))):
  file_url =   local_img_server + '/' + os.path.basename(f1)
  print(file_url)
  db_dataset_utils.add_image(db, file_url)

print('done!')


