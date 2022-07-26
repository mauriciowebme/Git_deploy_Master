# pip install GitPython
import os
import subprocess

teste = subprocess.run([
        "git"
        ,"branch"
        ]
        #, stderr = subprocess.PIPE
        , capture_output=True
        , text=True
        , shell=True)
print(teste.stdout)
base_dir = os.path.dirname(__file__)+'\\.git'
