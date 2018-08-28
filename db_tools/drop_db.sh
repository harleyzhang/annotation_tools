#!/bin/bash

echo This will drop the database that has been specified in your config file.
echo There is no way to recover the loss. 
echo Are you sure to drop the current annotations?

#read -p "Are you really sure? " -n 1 -r
read -p "Are you really sure[y|n]? " 
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1 # handle exits from shell or function but don't exit interactive shell
fi


script_dir=$(dirname "$0")

pushd $(pwd)
cd $script_dir/../

python -m annotation_tools.db_dataset_utils --action drop

popd
