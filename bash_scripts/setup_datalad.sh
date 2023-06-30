#!/usr/bin/bash

GITHUB_WORKSPACE="$1"
PROJECT="$2"

git config --global user.email "CMI_CPAC_Support@childmind.org"
git config --global user.name "Theodore (Machine User)"

pip3 install osfclient 1> /dev/null
osf -p ${PROJECT} clone ${GITHUB_WORKSPACE}/reg-data 1> /dev/null
datapath=$(find "$(pwd -P)" -name reg_5mm_pack -print)
chmod +x ${datapath}
echo "datapath=${datapath}"