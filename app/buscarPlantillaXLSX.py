#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

NOMBRE_ARCHIVO = "ruta_prinical.tmp"
listaArchivosRuta = []
extensionArchivo = ".xlsx"
nombreArcivoXLSX = ""

# toma la ruta actual donde se esta ejecutando el scrip
pathLocal = os.getcwd()

# Lectura del archivo temporal donde está la tuta principal
archivoPATH = open(pathLocal+"/temp/"+NOMBRE_ARCHIVO, "r")
PATH_PRINCIPAL = archivoPATH.read()

# lista de archivos que están en la ruta PATH_PRINCIPAL
listaArchivosRuta = os.listdir(PATH_PRINCIPAL)
def rutaArchivoXLS():

    # Le asigna los archivos que se encuentran en la ruta "PATH_PRINCIPAL"
    # a la lista "listaArchivosRuta"
    for i in range (0, len(listaArchivosRuta)):
        archivo = listaArchivosRuta[i]
        if (extensionArchivo in archivo):
            nombreArcivoXLSX = archivo

    if (extensionArchivo == ""):
            print("No se encontraron archivos compatibles")


    return (PATH_PRINCIPAL+nombreArcivoXLSX)

