# pip install GitPython
import os
import subprocess
base_dir = os.path.dirname(__file__)
retorno = subprocess.run([
        "cd", base_dir
        ]
        #, stderr = subprocess.PIPE
        , capture_output=True
        , text=True
        , shell=True)
retorno = subprocess.run([
        "dir"
        ]
        #, stderr = subprocess.PIPE
        , capture_output=True
        , text=True
        , shell=True)
print(retorno.stdout)
retorno = subprocess.run([
        "git", "pull", "origin", "master"
        ]
        #, stderr = subprocess.PIPE
        , capture_output=True
        , text=True
        , shell=True)
print(retorno.stdout)

base_dir = os.path.dirname(__file__)+'\\.git'
