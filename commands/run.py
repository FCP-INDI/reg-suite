import os
import subprocess
import pandas as pd
import numpy as np
import click

def run_cpac(version, datapath=None, git_home=None):
    if version == 'lite':
        preconfigs = 'default benchmark-FNIRT rbc-options'
        bids_data = f'{datapath}/data'
        pipeline_config = f'{datapath}/configs'
    elif version == 'full':
        preconfigs = 'default rbc-options benchmark-FNIRT fmriprep-options ndmg fx-options abcd-options ccs-options rodent monkey'
        bids_data = f'{datapath}/data'
        pipeline_config = f'{datapath}/configs'

    cmd = ['bash', f'{git_home}/bash_scripts/run_cpac.sh', bids_data, preconfigs, pipeline_config]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    output = result.stdout.decode()

    return

@click.command()
@click.option('--lite', is_flag=True, help='Run lite regression test. This will use 5mm datasets with ' 
              'shortened timeseries for faster processing. Runs on the following pipelines: default,'
              'benchmark-FNIRT, and rbc-options. Lite version should be selected if pull request '
              'is ready for review.')
@click.option('--full', is_flag=True, help='Run full regression test. This will run full dataset '
              '(17 subjects from 4 Sites) on 9 pipelines. Full version should be selected if ready '
              'to merge to main branch.')

def run(lite, full):
    """
    Run C-PAC with either "lite" or "full" regression datasets
    """
    git_home = os.path.normpath(os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir)

    if lite:
        version = 'lite'
    elif full:
        version = 'full'
    click.echo(f"Selected {version} version of regression suite")
    
    cmd = ['bash', f'{git_home}/bash_scripts/setup_datalad.sh', version]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    datapath = result.stdout.decode()
    
    output = run_cpac(version, datapath, git_home)

    return