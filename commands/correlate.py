import os
import click
import subprocess
from commands.bin import parse_yaml
from commands.bin import utils

def download_output(workspace, git_home):

    project = '39vqd'
    datapath = utils.download_data(workspace, project, git_home)

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

    git_home = os.path.normpath(os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir)
    datapath = utils.download_data(workspace, git_home)

    parse_yaml.cpac_yaml(datapath, outdir, f'{workspace}/correlations', 'run', 1)
    click.echo('YML obtained!')
    click.echo('** Starting Correlations **')
    
    cmd = ['bash', f'{git_home}/bash_scripts/correlate.sh', f'{workspace}/output.yml', workspace]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    print("Correlating: ", output)

    return