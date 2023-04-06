#!/usr/bin/bash

DATA_DIR="$1"
PRECONFIGS="$2"
CONFIGS="$3"
DATA_SOURCE="KKI Site-CBIC Site-SI HNU_1"
DOCKER_TAG="$4"

echo ${DATA_DIR}
echo ${PRECONFIGS}
echo ${CONFIGS}
echo ${DOCKER_TAG}

echo "Running full regression test ..."
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

        OUTPUT=/output/${pipeline}/${data}
        [ ! -d  ${OUTPUT} ] && mkdir -p ${OUTPUT}

        cat << TMP > regfull_${pipeline}_${data}_${subject}.sh
#!/usr/bin/bash

docker run --rm -it \
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
        chmod +x regfull_${pipeline}_${data}_${subject}.sh
        #bash regfull_${pipeline}_${data}_${subject}.sh
        echo "Finished regfull_${pipeline}_${data}_${subject}.sh"
    done
done