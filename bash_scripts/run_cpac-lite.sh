#!/usr/bin/bash

REG_DATA="$1"
DATA_DIR="$2"
PIPELINE_CONFIGS="$3"
DOCKER_TAG="$4"
GITHUB_WORKSPACE="$5"
DATA_SOURCE="Site-CBIC Site-SI HNU_1"
PRECONFIGS="default"

echo "OSF Data: ${REG_DATA}"
echo "Data Directory: ${DATA_DIR}"
echo "Preconfigs for lite regression test: ${PRECONFIGS}"
echo "Pipeline Configs directory: ${PIPELINE_CONFIGS}"
echo "Docker tag: ${DOCKER_TAG}"
echo "Github Workspace: ${GITHUB_WORKSPACE}"

echo "Running lite regression test ..."
for pipeline in ${PRECONFIGS}; do
    for data in ${DATA_SOURCE}; do
        if [ ${data} == 'HNU_1' ]; then
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

singularity run --rm \
    -B ${REG_DATA}:/reg-data \
    -B ${datapath}:/data \
    -B ${OUTPUT}:/outputs \
    -B ${PIPELINE_CONFIGS}:/pipeline_configs \
    ${DOCKER_TAG} /data /outputs participant \
    --save_working_dir --skip_bids_validator \
    --pipeline_file /pipeline_configs/${pipeline}_lite.yml \
    --participant_label ${subject} \
    --n_cpus 1 --mem_gb 7
TMP
        chmod +x reglite_${pipeline}_${data}_${subject}.sh
        bash reglite_${pipeline}_${data}_${subject}.sh
        echo "Finished reglite_${pipeline}_${data}_${subject}.sh"
    done
done