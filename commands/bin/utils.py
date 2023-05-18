import os
import subprocess

def download_data(workspace, project, git_home):

    cmd = ['bash', f'{git_home}/bash_scripts/setup_datalad.sh', workspace, project]
    result = subprocess.check_output(cmd)

    path = None
    for line in result.splitlines():
        if line.startswith(b'datapath='):
            path = line.split(b'=')[1]
            break
    datapath = path.decode()
    print("datapath: ", datapath)

    return datapath