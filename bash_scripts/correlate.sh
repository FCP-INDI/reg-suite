#!/usr/bin/bash

YAML="$1"
GIT_WORKSPACE="$2"

git clone https://github.com/FCP-INDI/CPAC_regtest_pack.git

echo "$(python3 ${GIT_WORKSPACE}/CPAC_regtest_pack/cpac_correlations.py ${YAML})"