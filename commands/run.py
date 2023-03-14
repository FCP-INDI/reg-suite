import os
import subprocess
import pandas as pd
import numpy as np
import click

#def run_cpac(version, datapath=None, output=None, access_flag=False): 
    #if version == 'lite' or 'local':
        #preconfigs = 'default benchmark-FNIRT rbc-options'
    #elif version == 'full':
        #preconfigs = 'default rbc-options benchmark-FNIRT fmriprep-options ndmg fx-options abcd-options ccs-options rodent monkey'

    #cmd = ['./bash_scripts/run_cpac.sh', datapath, output, preconfigs]
    #result = subprocess.run(cmd, stdout=subprocess.PIPE)
    #return

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

    if lite:
        version = 'lite'
    elif full:
        version = 'full'
    click.echo(f"Selected {version} version of regression suite")
    
    cmd = ['bash', './bash_scripts/setup_datalad.sh', version]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    datapath = result.stdout.decode()
    print(datapath)
    #if lite: 
        #datapath = os.path.join(datapath,"resampled_5mm_datasets")
    #elif full: 
        #datapath = os.path.join(datapath,'raw','cpac_regtest_data.tar.gz')
    
    #output = run_cpac(version, datapath, outdir, access_flag)

    return(datapath)