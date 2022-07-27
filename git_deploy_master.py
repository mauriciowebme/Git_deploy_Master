# pip install GitPython
import os
import subprocess

def Comandos(comandos_list = []):
        base_dir = os.path.dirname(__file__)
        retorno = subprocess.run(
                comandos_list
                #, stderr = subprocess.PIPE
                , capture_output=True
                , text=True
                , shell=True)
        if retorno.stdout != '':
                print(retorno.stdout)
        else:
                print(retorno.stderr)
        return retorno.stdout
        
base_dir = os.path.dirname(__file__)
os.system('cd..')
retorno = Comandos(['cd', 'C:\\DESENVOLVIMENTO\\testes'])
retorno = Comandos(['ls'])
retorno = Comandos(['dir'])

retorno = subprocess.run([
        "git", "pull", "origin", "master"
        ]
        #, stderr = subprocess.PIPE
        , capture_output=True
        , text=True
        , shell=True)
print(retorno.stdout)

base_dir = os.path.dirname(__file__)+'\\.git'
