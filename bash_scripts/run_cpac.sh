#!/usr/bin/bash

DATA_DIR="$1"
OUT_DIR="$2"
PRECONFIGS="$3"

mkdir outputs

docker run --rm \
    --user $(id -u):$(id -g) -v /etc/passwd:/etc/passwd -v /etc/group:/etc/group \
    -v ${DATA_DIR}:/reg-data \
    -v ${OUT_DIR}:/outputs \
    ${{ env.DOCKER_TAG }} \
    /reg-data /outputs test_config \
    --preconfig ${PRECONFIGS} \
    --participant_label \
    --n_cpus 2