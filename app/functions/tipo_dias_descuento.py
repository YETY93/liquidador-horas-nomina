import datetime
import holidays_co

# Retorna el total horas restando la hora de almuerzo
# se descuenta 0.75 horas  si es  dia habil y 0.5 horas si es fin de semana o festivo
# tiposDia = ["FIN_SEM_SABADO", "FIN_SEM_DOMINGO", "FESTIVO", "HABIL"]

def descuentoAlmuerzo(totalHoras: float, fecha: datetime):
    DESC_DIA_HABIL = 0.75
    DESC_DIA_FESTIVO = 0.5  # o fin de semana
    horaDescuento = 0.0
    dia = tipoDia(fecha)
    if totalHoras > 0:
        if dia != "HABIL":
            horaDescuento = totalHoras - DESC_DIA_FESTIVO
        else:
            horaDescuento = totalHoras - DESC_DIA_HABIL
    else:
        horaDescuento = 0.0
    return horaDescuento




# aaaa/mm/dd
# Segun la fecha enviada devolvera si es fin de samana, hábil o festivo
# primando como fecha de mas valor el dia festivo
def tipoDia(fecha: datetime):
    tiposDia = ["FIN_SEM_SABADO", "FIN_SEM_DOMINGO", "FESTIVO", "HABIL"]
    festivo = holidays_co.is_holiday_date(fecha)
    fecha = fecha.isoweekday()
    if festivo:
        tiposDia = tiposDia[2]
    elif fecha == 6:
        tiposDia =  tiposDia[0]
    elif fecha == 7:
        tiposDia = tiposDia[1]
    else:
        tiposDia = tiposDia[3]
    return tiposDia
