import time

# Función que devuleve la diferencia entre dos horas y su valor porcentual de los minutos
def diferrenciaHoras(horaInicial: time, horaFinal: time):
    HORAS_DIA = 24  # Horas totales del dia
    horasTotales = 0.0
    horaInicio = horaInicial.hour
    minutoHoraInicio = horaInicial.minute
    horaFin = horaFinal.hour  # Hora en que
    minutoHoraFin = horaFinal.minute

    if horaInicio > horaFin:
        holaRestantes = HORAS_DIA - horaInicio
        horasTotales = holaRestantes + horaFin

    elif horaInicio < horaFin:
        horasTotales = horaInicio - horaFin

    # Si tras restar los minutos da un número negativo, se suman 60 minutos y restar 1 a las horas
    Minutostotales = minutoHoraFin - minutoHoraInicio
    #print ("Minutostotales", Minutostotales, " fin",minutoHoraFin, " fin",minutoHoraInicio  )
    if (Minutostotales < 0):
        totalMinutos = Minutostotales + 60
        minutosAdicionales = conversionMinutos(totalMinutos)
        horasTotales = ((abs (horasTotales)) - 1) + minutosAdicionales
        print("totalMinutos despues", horasTotales - 1, ":", minutosAdicionales, " hora", (horasTotales - 1) + minutosAdicionales)
    else:
        Minutostotales = conversionMinutos(Minutostotales)
        horasTotales = ( (abs(horasTotales))+ Minutostotales)
        print("totalMinutos despues", horasTotales - 1, ":", Minutostotales, " hora", horasTotales + Minutostotales)

    return horasTotales


# recibe la cantidad de minutos y los tranforma a un porcentaje en base a una hora
def conversionMinutos(minutos: int):
    porcentajeHora = (minutos * 100) / 60
    porcentajeHora = porcentajeHora / 100  # se divide entre 100 para si valor decimal
    return porcentajeHora
