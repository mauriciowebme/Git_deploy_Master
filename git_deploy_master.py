# pip install GitPython
import os
import subprocess

def Comandos(cmd_ajustado = []):
        cmd_ajustado = F"cd {os.path.dirname(__file__)} && "
        cont_cm = 0
        for cm in cmd_list:
                cont_cm += 1
                if cont_cm < len(cmd_list):
                        cmd_ajustado += cm+" && "
                else:
                        cmd_ajustado += cm
        retorno = subprocess.run(
                ["cmd.exe", "/C", cmd_ajustado]
                #, stderr = subprocess.PIPE
                , capture_output=True
                , text=True
                , shell=True)
        if retorno.stdout != '':
                print(retorno.stdout)
        else:
                print(retorno.stderr)
        return retorno.stdout

cmd_list = [
        #"dir",
        #"git status",
        "git pull origin master"
]
retorno = Comandos(cmd_list)
o=0
input()