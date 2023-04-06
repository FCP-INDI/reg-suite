#!/usr/bin/bash

DATA_DIR="$1"
PRECONFIGS="$2"
CONFIGS="$3"
DOCKER_TAG="$4"
GITHUB_WORKSPACE="$5"
DATA_SOURCE="KKI Site-CBIC Site-SI HNU_1"

echo ${DATA_DIR}
echo ${PRECONFIGS}
echo ${CONFIGS}
echo ${DOCKER_TAG}
echo ${GITHUB_WORKSPACE}

echo "Running lite regression test ..."
for pipeline in ${PRECONFIGS}; do
    for data in ${DATA_SOURCE}; do
        if [ ${data} == 'KKI' ]; then
            subject="sub-2014113"
            datapath=${DATA_DIR}/KKI
        elif [ ${data} == 'HNU_1' ]; then
            subject="sub-0025428"
            datapath=${DATA_DIR}/HNU_1
        elif [ ${data} == 'Site-CBIC' ]; then
            subject="sub-NDARAA947ZG5"
            datapath=${DATA_DIR}/Site-CBIC
        elif [ ${data} == 'Site-SI' ]; then
            subject="sub-NDARAD481FXF"
            datapath=${DATA_DIR}/Site-SI
        fi

        OUTPUT=${GITHUB_WORKSPACE}/output/${pipeline}/${data}
        [ ! -d  ${OUTPUT} ] && mkdir -p ${OUTPUT}

        cat << TMP > reglite_${pipeline}_${data}_${subject}.sh
#!/usr/bin/bash

docker run --rm \
    --user $(id -u):$(id -g) -v /etc/passwd:/etc/passwd -v /etc/group:/etc/group \
    -v ${datapath}:/reg-data \
    -v ${OUTPUT}:/outputs \
    -v ${CONFIGS}:/pipeline \
    ${DOCKER_TAG} /reg-data /outputs participant \
    --save_working_dir --skip_bids_validator \
    --pipeline_file /pipeline/${pipeline}_lite.yml \
    --participant_label ${subject} \
    --n_cpus 2
TMP
        chmod +x reglite_${pipeline}_${data}_${subject}.sh
        bash reglite_${pipeline}_${data}_${subject}.sh
        echo "Finished reglite_${pipeline}_${data}_${subject}.sh"
    done
done