# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import subprocess
from subprocess import check_output
from unittest import result


ejecutarVirtualEnv = "nomina\\Scripts\\activate.bat &&"
ejecutarPython = "python anlizarNomina.py"

comandos = ejecutarVirtualEnv + ejecutarPython

resultado = subprocess.run(comandos, shell=True)
resultado.check_returncode()

input("Ha finalizado la ejecución \n " +
      " Preciona (ENTER) para continuar... ")