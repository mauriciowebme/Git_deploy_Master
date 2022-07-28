import os
import subprocess

def Comandos(cmd_list = []):
        """
        Exemplos:
        cmd_list = [
                "dir",
                "cd..",
                "dir",
                "git remote show origin",
                "git checkout master",
                "git pull origin master",
        ]
        """
        comandos_cmd = F"cd {os.path.dirname(__file__)} && "
        cont_cm = 0
        for cm in cmd_list:
                cont_cm += 1
                if cont_cm < len(cmd_list):
                        comandos_cmd += cm+" && "
                else:
                        comandos_cmd += cm
        retorno = subprocess.run(
                ["cmd.exe", "/C", comandos_cmd]
                #, stderr = subprocess.PIPE
                , capture_output=True
                , text=True
                , shell=True)
        if retorno.stdout != '':
                retorno = ('-'*60 + '\n') + retorno.stdout + ('-'*60)
                return retorno
        else:
                retorno = ('-'*60 + '\n') + retorno.stderr + ('-'*60)
                return retorno

