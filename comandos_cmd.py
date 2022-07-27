# pip install GitPython
import os
import subprocess

def Comandos(comandos_cmd = []):
        """
        Exemplos:
        comandos_cmd = [
                "dir",
                "cd..",
                "dir",
        ]
        """
        comandos_cmd = F"cd {os.path.dirname(__file__)} && "
        cont_cm = 0
        for cm in cmd_list:
                cont_cm += 1
                if cont_cm < len(cmd_list):
                        comandos_cmd += cm+" && echo ------------------------------------------------------------------ && "
                else:
                        comandos_cmd += cm
        retorno = subprocess.run(
                ["cmd.exe", "/C", comandos_cmd]
                #, stderr = subprocess.PIPE
                , capture_output=True
                , text=True
                , shell=True)
        if retorno.stdout != '':
                print(retorno.stdout)
        else:
                print(retorno.stderr)
        return retorno.stdout

if __name__ == '__main__':
        os.system('cls')
        cmd_list = [
                "dir",
                "cd..",
                "dir",
                #"git remote show origin",
                #"git checkout teste2",
                #"git pull origin teste2",
                #"git config --list",
        ]
        retorno = Comandos(cmd_list)
        input()