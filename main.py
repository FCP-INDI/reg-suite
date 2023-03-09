import os
import subprocess
import pandas as pd
import numpy as np
import click
from commands import run
#from commands import correlate

@click.group(help="CLI tool to sutomate CPAC regression tests")

def cli():
    pass

cli.add_command(run.run)
#cli.add_command(correlate.correlate)

if __name__ == '__main__':
    cli()