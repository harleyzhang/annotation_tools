#!/bin/bash
img_dir=`python -c 'import annotation_tools.default_config as cfg; print(cfg.LOCAL_IMAGES_DIR);'`
img_port=$(python -c 'import annotation_tools.default_config as cfg; print(cfg.LOCAL_IMAGES_HTTP_PORT);')

pushd $(pwd)
cd $img_dir
#for python2
#python -m SimpleHTTPServer $img_port &

echo image dir: $img_dir

#for python3
python -m http.server $img_port &

img_server_pid=$!
echo $img_server_pid

popd


python run.py --port 8008 

kill $img_server_pid




