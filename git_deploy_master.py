# pip install GitPython
import os
import subprocess

retorno = subprocess.run([
        "git"
        ,"branch"
        ]
        #, stderr = subprocess.PIPE
        , capture_output=True
        , text=True
        , shell=True)
retorno = subprocess.run([
        "git"
        ,"branch"
        ]
        #, stderr = subprocess.PIPE
        , capture_output=True
        , text=True
        , shell=True)
print(retorno.stdout)
base_dir = os.path.dirname(__file__)+'\\.git'
