import time

# Función que devuleve la diferencia entre dos horas
def diferrenciaHoras(horaInicial: time, horaFinal: time):
    horasTotales = 0.0
    horaSalida = horaInicial.hour
    minutoEntrada = horaInicial.minute
    horaLlegada = horaFinal.hour
    minutoLlegada = horaFinal.minute

    horasTotales = (horaLlegada - horaSalida)
    Minutostotales = minutoLlegada - minutoEntrada

# Si tras restar los minutos da un número negativo, se suman 60 minutos y restar 1 a las horas
    if (Minutostotales < 0):
        totalMinutos = Minutostotales + 60
        minutosAdicionales = conversionMinutos(totalMinutos)
        horasTotales = (horasTotales - 1) + minutosAdicionales
    else:
        Minutostotales = conversionMinutos(Minutostotales)
        horasTotales = (horasTotales + Minutostotales)

    return abs(horasTotales)


# recibe la cantidad de minutos y los tranforma a un porcentaje en base a una hora
def conversionMinutos(minutos: int):
    porcentajeHora = (minutos * 100) / 60
    porcentajeHora = porcentajeHora / 100  # se divide entre 100 para si valor decimal

    return porcentajeHora
