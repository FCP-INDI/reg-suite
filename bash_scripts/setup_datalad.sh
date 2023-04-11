#!/usr/bin/bash

VERSION="$1"
GITHUB_WORKSPACE="$2"

git config --global user.email "amygutierrezbme@gmail.com"
git config --global user.name "amygutierrez"

pip3 install osfclient 1> /dev/null
osf -p qjn8d clone ${GITHUB_WORKSPACE}/reg-data 1> /dev/null

if [ ${VERSION} == 'lite' ]; then
    datapath=$(find "$(pwd -P)" -name reg_5mm_pack -print)
    echo "datapath=${datapath}"

elif [ ${VERSION} == 'full' ]; then
    datapath=$(find "$(pwd -P)" -name raw -print)
    echo "datapath=${datapath}"
fi