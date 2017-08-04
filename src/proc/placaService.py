
import commandSender

__estados = {"midiendo": False,
             "seteado": False}


def isSeteado():
    return __estados["seteado"]


def isMidiendo():
    return __estados["midiendo"]


def changeModeAutomatOnLine():
    pause()
    commandSender.setMode(1)
    __estados["seteado"] = False
    __estados["midiendo"] = False

def changeModeAutomatRegistro():
    pause()
    commandSender.setMode(2)
    __estados["seteado"] = False
    __estados["midiendo"] = False


def changeModeInstrOnLine():
    pause()
    commandSender.setMode(3)
    __estados["seteado"] = False
    __estados["midiendo"] = False


def changeModeInstrRegistro():
    pause()
    commandSender.setMode(4)
    __estados["seteado"] = False
    __estados["midiendo"] = False


def setDateTime(dateTimeStr):

    anio = dateTimeStr[0:4]
    mes = dateTimeStr[5:7]
    dia = dateTimeStr[8:10]
    hora = dateTimeStr[11:13]
    minutos = dateTimeStr[14:16]
    segundos = dateTimeStr[17:19]

    commandSender.setDateTime(hora + minutos + segundos + dia + mes + anio)


def getDateTime():
    dateTimeStr = commandSender.getDateTime()

    anio = int(dateTimeStr[10:14])
    mes = int(dateTimeStr[8:10])
    dia = int(dateTimeStr[6:8])
    hora = int(dateTimeStr[0:2])
    minutos = int(dateTimeStr[2:4])
    segundos = int(dateTimeStr[4:6])

    return (anio, mes, dia, hora, minutos, segundos)


def pause():
    __estados["midiendo"] = False
    commandSender.pause()
