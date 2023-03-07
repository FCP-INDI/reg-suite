import os
import subprocess
import pandas as pd
import numpy as np
import time
import click

@click.group()
@click.option('--lite', is_flag=True, help='Run lite regression test. This will use 5mm datasets with ' 
              'shortened timeseries for faster processing. Runs on the following pipelines: default,'
              'benchmark-FNIRT, and rbc-options. Lite version should be selected if pull request '
              'is ready for review.')
@click.option('--full', is_flag=True, help='Run full regression test. This will run full dataset '
              '(17 subjects from 4 Sites) on 9 pipelines. Full version should be selected if ready '
              'to merge to main branch.')

def run_cpac(lite, full):
    """
    Will run C-PAC using either "lite" datasets or full datasets
    """
    if lite:
        version = 'lite'
    elif full:
        version = 'full'
    click.echo(f"Selected {version} version of regression suite")
    
@run_cpac.command()
def run():
    click.echo('Running CPAC')
        


if __name__ == '__main__':  
    run_cpac()
    run()
