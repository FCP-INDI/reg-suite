import os
import subprocess
import pandas as pd
import numpy as np
import click

@click.command()
@click.option('--lite', is_flag=True, help='Run lite regression test. This will use 5mm datasets with ' 
              'shortened timeseries for faster processing. Runs on the following pipelines: default,'
              'benchmark-FNIRT, and rbc-options. Lite version should be selected if pull request '
              'is ready for review.')
@click.option('--full', is_flag=True, help='Run full regression test. This will run full dataset '
              '(17 subjects from 4 Sites) on 9 pipelines. Full version should be selected if ready '
              'to merge to main branch.')
@click.option('--data', '-d', required=False, type=str, help='Path to input BIDS data')
@click.option('--outdir', '-o', required=True, type=str, help='Path to output directory. working,'
              'log, and output subdirectories will be stored in this path.')


def run(lite, full, data=None, outdir=None):
    """
    Run C-PAC with either "lite" or "full" regression datasets
    """
    if lite:
        version = 'lite'
    elif full:
        version = 'full'
    else:
        version = 'local'
    click.echo(f"Selected {version} version of regression suite")
    click.echo(f"data path {data}")
    click.echo(f"output path {outdir}")
    
    if (version == 'lite' or 'full') and data is not None:
        datapath=data
        click.echo(f'\n*******************************************************************\n'
                f'You have selected {version} regression version, but added a data path.\n'
                f'Will not run {version} datasets. Will instead run datasets in {data}\n'
                f'*******************************************************************\n')
    if (version == 'local') and data is None:
        raise Exception(f'Must add data input path using --data flag')
    if (version == 'lite' or 'full') and data is None:
        if version == 'lite':
            datapath = 'datapath for lite'
            #insert datalad subprocess here
        elif version == 'full':
            datapath = 'datapath for full'
            #insert datalad subprocess here
            #datapath = data/path/for/lite
    return(datapath, outdir)