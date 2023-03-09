import os
import subprocess
import pandas as pd
import numpy as np
import click

@click.command()
@click.option('--outdir', '-o', required=True, type=str, help='Path to output directory from regression run'
            'done using the `run` command.')


def correlate(outdir):
    """
    Correlate outputs from regression run again another C-PAC version.
    """
    click.echo('Correlating')