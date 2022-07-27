# pip install GitPython
import os
import subprocess

def Comandos(comandos_list = []):
        base_dir = os.path.dirname(__file__)
        retorno = subprocess.run([
                comandos_list
                ]
                #, stderr = subprocess.PIPE
                , capture_output=True
                , text=True
                , shell=True)
        return retorno.stdout

teste = Comandos(['dir'])

print(teste)

retorno = subprocess.run([
        "git", "pull", "origin", "master"
        ]
        #, stderr = subprocess.PIPE
        , capture_output=True
        , text=True
        , shell=True)
print(retorno.stdout)

base_dir = os.path.dirname(__file__)+'\\.git'
