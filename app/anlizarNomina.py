from datetime import datetime, time
from functions import  totalHoras

import openpyxl

import buscarPlantillaXLSX


ARCHIVO_XLSX = buscarPlantillaXLSX.rutaArchivoXLS()
COLUMNA_FECHA = 'C'
COLUMNA_HORA_ENTRADA = 'D'
COLUMNA_HORA_SALIDA = 'E'
COLUMNA_TOTAl_HORAS = 'F'
ListHojasCalculo = []

try:
    libroExcel = openpyxl.load_workbook(ARCHIVO_XLSX)
    ListHojasCalculo = libroExcel.sheetnames
    # contador del ciclo while
    contadorHojas = 0# valor inicial debe ser 0
    while contadorHojas < len(ListHojasCalculo):
        hojaActiva = libroExcel[ListHojasCalculo[contadorHojas]]
        contadorFila = 7
        for fila in hojaActiva.iter_rows():
            filaActivaFecha = COLUMNA_FECHA + str(contadorFila)
            filaHoraEntrada = COLUMNA_HORA_ENTRADA + str(contadorFila)
            filaHoraSalida = COLUMNA_HORA_SALIDA + str(contadorFila)
            filaTotalHoras = COLUMNA_TOTAl_HORAS + str(contadorFila)
            valorFecha = hojaActiva[filaActivaFecha].value
            valorHoraEntrada = hojaActiva[filaHoraEntrada].value
            valorHoraSalida = hojaActiva[filaHoraSalida].value

            #si en la celda actual es vacia se le asigan la hora 00:00
            if(valorHoraEntrada == None or valorHoraSalida == None):
                valorHoraEntrada = time(0, 0, 0)
                valorHoraSalida = valorHoraEntrada

            if str(valorFecha) == "TOTALES":
                break

            cantidaHoras = totalHoras.diferrenciaHoras(valorHoraEntrada,valorHoraSalida )
            print("valorHoraEntrada: ", valorHoraEntrada, " valorHoraSalida: ", valorHoraSalida," Total Horas: ", cantidaHoras )
            hojaActiva[filaTotalHoras].value = cantidaHoras
            libroExcel.save(ARCHIVO_XLSX)  # guarda los cambios

            contadorFila = contadorFila + 1

        contadorHojas = contadorHojas + 1

except Exception as ex:
    print("Archivo corrupto \n posible falla " + str(ex) +
          "\n Hoja: ", hojaActiva)
