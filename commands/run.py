import os
import subprocess
import click
from commands.bin.utils import download_data

def run_cpac(version, datapath=None, git_home=None, docker_tag=None,
             workspace=None):
    if version == 'lite':
        reg_data = datapath
        bids_data = f'{datapath}/data'
        pipeline_config = f'{datapath}/configs'
        cmd = ['bash', f'{git_home}/bash_scripts/run_cpac-lite.sh', reg_data,
               bids_data, pipeline_config, docker_tag, workspace]

    elif version == 'full':
        preconfigs = ('default rbc-options benchmark-FNIRT fmriprep-options '
                      'ndmg fx-options abcd-options ccs-options rodent monkey')
        bids_data = f'{datapath}/data'
        pipeline_config = f'{datapath}/configs'
        cmd = ['bash', f'{git_home}/bash_scripts/run_cpac-full.sh', bids_data,
               preconfigs, pipeline_config, docker_tag, workspace]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    print("run output: ", output)

    return

@click.command()
@click.option('--lite', is_flag=True, help='Run lite regression test. This will use 5mm datasets with ' 
              'shortened timeseries for faster processing. Runs on the following pipelines: default,'
              'benchmark-FNIRT, and rbc-options. Lite version should be selected if pull request '
              'is ready for review.')
@click.option('--full', is_flag=True, help='Run full regression test. This will run full dataset '
              '(17 subjects from 4 Sites) on 9 pipelines. Full version should be selected if ready '
              'to merge to main branch.')
@click.option('--docker_tag','-t', type=str, help = 'Docker tag. This input is generated in git actions '
              'and should remain as $\{\{ env.DOCKER_TAG \}\}`')
@click.option('--workspace','-w', type=str, help = 'Github workspace. This input is generated in git actions '
              'and should remain as $GITHUB_WORKSPACE')

def run(lite, full, docker_tag, workspace):
    """
    Run C-PAC with either "lite" or "full" regression datasets
    """

    git_home = os.path.normpath(os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir)

    if lite:
        version = 'lite'
    elif full:
        version = 'full'
    click.echo(f"Selected {version} version of regression suite")
    project = 'qjn8d'

    datapath = download_data(workspace, project, git_home)

    output = run_cpac(version, datapath, git_home, docker_tag, workspace)

    return