import buscarPlantillaXLSX
import openpyxl

ARCHIVO_XLSX = buscarPlantillaXLSX.rutaArchivoXLS()
CELDA_FECHA = 'C'
ListHojasCalculo = []


try:
    libroExcel = openpyxl.load_workbook(ARCHIVO_XLSX)
    ListHojasCalculo = libroExcel.sheetnames
    #contador del ciclo while
    contadorHojas = 0




except Exception as ex:
        print("Archivo corrupto \n posible falla " + str(ex))