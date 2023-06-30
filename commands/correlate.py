import os
import click
import subprocess
from commands.bin import parse_yaml


@click.command()
@click.option('--pipeline1', required=True, type=str, help='Path to output directory from CPAC run '
              'to correlate against pipeline2')
@click.option('--pipeline2', required=True, type=str, help='Path to output directory from CPAC run '
              'to correlate against pipeline1')
@click.option('--workspace','-w', type=str, help = 'Github workspace. This input is generated in git actions '
              'and should remain as $GITHUB_WORKSPACE')


def correlate(pipeline1, pipeline2, workspace):
    """
    Correlate outputs from regression run again another C-PAC version.
    """

    git_home = os.path.normpath(os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir)
    run_name = ((pipeline2.split(workspace+'lite'))[1]).replace('/','_')

    parse_yaml.cpac_yaml(pipeline1, pipeline2, f'{workspace}/correlations', run_name, 1)
    click.echo('YML obtained!')
    click.echo('** Starting Correlations **')
    
    cmd = ['bash', f'{git_home}/bash_scripts/correlate.sh', f'{workspace}/output.yml', workspace]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    print("Correlating: ", output)

    return