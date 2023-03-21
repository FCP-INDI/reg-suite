#!/usr/bin/bash

VERSION="$1"

git config --global user.email "amygutierrezbme@gmail.com"
git config --global user.name "amygutierrez"

pip3 install osfclient
osf -p qjn8d clone reg-data

if [ ${VERSION} == 'lite' ]; then
    datapath=$(find "$(pwd -P)" -name reg_5mm_pack -print)
    echo "datapath=$datapath"

elif [ ${VERSION} == 'full' ]; then
    datapath=$(find "$(pwd -P)" -name raw -print)
    echo "datapath=$datapath"
fi