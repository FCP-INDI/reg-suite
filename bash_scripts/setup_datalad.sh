#!/usr/bin/bash

VERSION="$1"
GITHUB_WORKSPACE="$2"

git config --global user.email "CMI_CPAC_Support@childmind.org"
git config --global user.name "Theodore (Machine User)"

pip3 install osfclient 1> /dev/null
osf -p qjn8d clone ${GITHUB_WORKSPACE}/reg-data 1> /dev/null

if [ ${VERSION} == 'lite' ]; then
    datapath=$(find "$(pwd -P)" -name reg_5mm_pack -print)
    chmod +x ${datapath}
    echo "datapath=${datapath}"

elif [ ${VERSION} == 'full' ]; then
    datapath=$(find "$(pwd -P)" -name raw -print)
    chmod +x ${datapath}
    echo "datapath=${datapath}"
fi