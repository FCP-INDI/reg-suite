#!/usr/bin/bash

git config --global user.email "CMI_CPAC_Support@childmind.org"
git config --global user.name "Theodore (Machine User)"
wget -O- http://neuro.debian.net/lists/focal.us-tn.libre | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
sudo apt-key adv --recv-keys --keyserver hkps://keyserver.ubuntu.com 0xA5D32F012649A5A9
sudo apt-get update
sudo apt-get install datalad git-annex-standalone
pip install datalad-osf