#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import subprocess
import os
from subprocess import check_output
from unittest import result



# Esta función guarda el PATH donde se esjecuta el script principal
# Para la lectura de la plmatilla de la nomina

NOMBRE_ARCHIVO = "ruta_prinical.tmp"
def guardarPath(nombreArcivo: str):
    pathLocal = os.getcwd()    # toma la ruta actual donde se esta ejecutando el scrip
    file = open(pathLocal+"/app/temp/"+nombreArcivo, "w")
    file.write(pathLocal)
    file.close()

guardarPath(NOMBRE_ARCHIVO)
"""
ejecutarVirtualEnv = "nomina\\Scripts\\activate.bat &&"
ejecutarPython = "python anlizarNomina.py"

comandos = ejecutarVirtualEnv + ejecutarPython

resultado = subprocess.run(comandos, shell=True)
resultado.check_returncode()

input("Ha finalizado la ejecución \n " +
      " Preciona (ENTER) para continuar... ")

"""
