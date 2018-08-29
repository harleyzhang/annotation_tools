"""
Default configurations.
"""

MONGO_URI = "mongodb://localhost:27017/anntest"

# directory struction of local dataset
LOCAL_DATASET_DIR = "/home/honglei/Data/TestDb"
LOCAL_ANNOTATIONS_DIR = LOCAL_DATASET_DIR + "/annotations"
LOCAL_IMAGES_DIR = LOCAL_DATASET_DIR + "/images"

# images are hosted by a local http server, and files are accessed by url
# http://localhost:<port>/<img_fname>
LOCAL_IMAGES_HTTP_PORT = 8007
