import holidays_co
import datetime


# aaaa/mm/dd
# Segun la fecha enviada devolvera si es fin de samana, hábil o festivo
# primando como fecha de mas valor el dia festivo
def tipoDia(fecha: datetime):
    tiposDia = ["FIN_SEM_SABADO", "FIN_SEM_DOMINGO", "FESTIVO", "HABIL"]
    festivo = holidays_co.is_holiday_date(fecha)
    fecha = fecha.isoweekday()
    if festivo:
        return tiposDia[2]
    elif fecha == 6:
        return tiposDia[0]
    elif fecha == 7:
        return tiposDia[1]
    else:
        return tiposDia[3]
