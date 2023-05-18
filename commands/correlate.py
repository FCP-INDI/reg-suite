#import subprocess
#import pandas as pd
#import numpy as np
import os
import click
import commands.bin.parse_yaml as parse_yaml
from commands.bin.utils import download_data

def download_output(workspace):
    
    git_home = os.path.normpath(os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir)
    project = '39vqd'
    datapath = download_data(workspace, project, git_home)

    return datapath


@click.command()
@click.option('--outdir', '-o', required=True, type=str, help='Path to output directory from regression run'
            'done using the `run` command.')
@click.option('--workspace','-w', type=str, help = 'Github workspace. This input is generated in git actions '
              'and should remain as $GITHUB_WORKSPACE')


def correlate(outdir, workspace):
    """
    Correlate outputs from regression run again another C-PAC version.
    """

    datapath = download_data(workspace)

    y = parse_yaml.cpac_yaml(datapath, outdir, f'{workspace}/correlations', 'run', 1)
    print(y)
    click.echo('Correlating')