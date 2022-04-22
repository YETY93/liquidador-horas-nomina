import datetime
import tipoDia


# Retorna el total horas restando la hora de almuerzo
# se descuenta 0.75 horas  si es  dia habil y 0.5 horas si es fin de semana o festivo
# tiposDia = ["FIN_SEM_SABADO", "FIN_SEM_DOMINGO", "FESTIVO", "HABIL"]

def descuentoAlmuerzo(totalHoras: float, fecha: datetime):
    DESC_DIA_HABIL = 0.75
    DESC_DIA_FESTIVO = 0.5  # o fin de semana
    horaDescuento = 0.0
    dia = tipoDia.tipoDia(fecha)

    if dia != "HABIL":
        horaDescuento = totalHoras - DESC_DIA_FESTIVO
        return horaDescuento
    else:
        horaDescuento = totalHoras - DESC_DIA_HABIL
        return horaDescuento

