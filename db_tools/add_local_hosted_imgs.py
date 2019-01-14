#!/usr/bin/env python

# This script add images from a local hosted repository to the annotation database
# Note that this will copy images to another local directory and all image ids will be 
# regenerated again. 

import glob
import os
import subprocess
import sys

this_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(this_path)
print(root_path)
sys.path.append(root_path)

from annotation_tools import db_dataset_utils
from annotation_tools import annotation_tools
from annotation_tools import default_config as cfg

# show usage and ask for input images
print("""
-------------------------

This script load images stored in the given directory into the annotation tool. 
Note: this script will copy all .jpg images from the given image folder to another direcory and
rename them to the format of COCO IDs. Other image format are ignored by this script. 

First check the configurations in the annotation_tools/default_config.py. 

MONGO_URI is the connection to MongoDb. The name of the collection is specified in this variable. 
LOCAL_DATASET_DIR point to the directory where the images will be stored. 

---------------------------

""")

print("""
Current configuration:

MONGO_URI = {}

LOCAL_DATASET_DIR = {}

---------------------------

""".format(cfg.MONGO_URI, cfg.LOCAL_DATASET_DIR))


# create directories
if not os.path.exists(cfg.LOCAL_ANNOTATIONS_DIR):
  os.makedirs(cfg.LOCAL_ANNOTATIONS_DIR)

if not os.path.exists(cfg.LOCAL_IMAGES_DIR):
  os.makedirs(cfg.LOCAL_IMAGES_DIR)


# check input argument
if len(sys.argv)<2:
  print("Please give the image folder as the input argument!")
  sys.exit(1)

img_folder = sys.argv[1]


# drop db if necessary
print("Note, if you choose to clean the dataset, the annotations in the current dataset \
will be lost. You cannot undo this operation! ")

choice = input("Do you want to clean the dataset? [yes/no]")

print(choice)

if choice.lower()=='yes':
  print('clean the dataset....')
  result = subprocess.Popen(["/bin/bash", "drop_db.sh"]) 
  rslt_txt = result.communicate()[0]
  rslt_code = result.returncode
  #print('return code: {}'.format(rslt_code))
else:
  print("continue without clean the dataset.\n")

# init db and ignore error
result = subprocess.Popen(["/bin/bash", "init_db.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE);
#print("init db return code: {}".format(result.returncode))
if result.returncode != 0:
  print("*****  init_db.sh failed. This is mostly because the dataset has been already initialized! \n")


local_img_server="http://localhost:" + str(cfg.LOCAL_IMAGES_HTTP_PORT)
#img_folder='/home/honglei/Data/Baby_carseat/images'


print('connecting to mongo db....')
db = annotation_tools.get_db()

print('loading files into annotation tools....')
for f1 in sorted(glob.glob(os.path.join(img_folder, '*.jpg'))):
  #file_url =   local_img_server + '/' + os.path.basename(f1)
  file_url = 'file://'+f1
  print(file_url)
  db_dataset_utils.add_image(db, file_url)

print('done!')


