#!/usr/bin/bash

VERSION="$1"

git config --global user.email "amygutierrezbme@gmail.com"
git config --global user.name "amygutierrez"

#pip install datalad-installer
#datalad-installer git-annex -m datalad/packages
#git config --global filter.annex.process "git-annex filter-process"
#pip install --user datalad
#yes | conda install -c conda-forge datalad
#pip3 install datalad
#datalad clone osf://qjn8d/ reg-data

pip3 install osfclient
osf -p qjn8d clone reg-data

if [ ${VERSION} == 'lite' ]; then
    find "$(pwd -P)" -name reg_5mm_pack -print
elif [ ${VERSION} == 'full' ]; then
    find "$(pwd -P)" -name raw -print
fi