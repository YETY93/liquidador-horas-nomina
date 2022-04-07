from datetime import datetime, time
from functions import totalHoras
from openpyxl.styles import Font, PatternFill

import openpyxl

import buscarPlantillaXLSX

ARCHIVO_XLSX = buscarPlantillaXLSX.rutaArchivoXLS()
ListHojasCalculo = []

COLUMNA_FECHA = 'C'
COLUMNA_HORA_ENTRADA = 'D'
COLUMNA_HORA_SALIDA = 'E'
COLUMNA_TOTAl_HORAS = 'F'

try:
    libroExcel = openpyxl.load_workbook(ARCHIVO_XLSX)
    ListHojasCalculo = libroExcel.sheetnames
    # contador del ciclo while
    contadorHojas = 0  # valor inicial debe ser 0
    while contadorHojas < len(ListHojasCalculo):
        hojaActiva = libroExcel[ListHojasCalculo[contadorHojas]]
        contadorFila = 7  # a partir de la celda 7 estan las horas
        for fila in hojaActiva.iter_rows():
            filaActivaFecha = COLUMNA_FECHA + str(contadorFila)
            filaHoraEntrada = COLUMNA_HORA_ENTRADA + str(contadorFila)
            filaHoraSalida = COLUMNA_HORA_SALIDA + str(contadorFila)
            filaTotalHoras = COLUMNA_TOTAl_HORAS + str(contadorFila)
            valorFecha = hojaActiva[filaActivaFecha].value
            valorHoraEntrada = hojaActiva[filaHoraEntrada].value
            valorHoraSalida = hojaActiva[filaHoraSalida].value
            # la Celda final
            if str(valorFecha) == "TOTALES":
                print(hojaActiva)
                break
            # Confirma si la celda tiene un tipo de formato valido y si no se coloca un fondo rojo
            # con el texto "NO DATOS"
            elif type(valorHoraEntrada) is str or type(valorHoraSalida) is str:
                hojaActiva[filaTotalHoras].value = "NO DATOS"
                hojaActiva[filaTotalHoras].fill = PatternFill(patternType="solid",
                                                              fgColor="CA4958")  # Despues debe cambiar el color a al original
            # si la celda actual es vacia se le asigna 0 al total horas
            elif valorHoraEntrada is None or valorHoraSalida is None:
                hojaActiva[filaTotalHoras].value = 0
                libroExcel.save(ARCHIVO_XLSX)
            else:
                hojaActiva[filaTotalHoras].fill = PatternFill(patternType=None)  # Despues debe cambiar el color a al original
                #print (hojaActiva[filaTotalHoras].fill)
                # se emplea el metodo diferrenciaHoras del modulo totalHoras
                cantidaHoras = totalHoras.diferrenciaHoras(valorHoraEntrada, valorHoraSalida)
                print("valorHoraEntrada: ", valorHoraEntrada, " valorHoraSalida: ", valorHoraSalida, " Total Horas: ",
                      cantidaHoras, " ", hojaActiva)
                # asigna el valor de las horas a la celda
                hojaActiva[filaTotalHoras].value = cantidaHoras
                # guarda los cambios
                libroExcel.save(ARCHIVO_XLSX)

            contadorFila = contadorFila + 1

        contadorHojas = contadorHojas + 1

except Exception as ex:
    print("Archivo corrupto \n posible falla " + str(ex) +
          "\n Hoja: ", hojaActiva, filaHoraEntrada, valorHoraEntrada)
