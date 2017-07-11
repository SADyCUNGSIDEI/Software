
__codigosInicioReg = {"0": "vueltaEnergia",
                      "1": "init",
                      "2": "descargaDatos",
                      "3": "watchdog"}


def decode(data):

    toRet = []

    firstHeader = __translateHeader(data[0:25])

    toRet.append({"type": "header",
                  "data": firstHeader})

    return toRet


def __translateHeader(header):

    headerToRet = {
        "hora": str(header[2:4]),
        "minutos": str(header[4:6]),
        "segundos": str(header[6:8]),
        "dia": str(header[8:10]),
        "mes": str(header[10:12]),
        "anio": str(header[12:16]),
        "intervalo": str(header[16:20]),
        "modo": str(header[20]),
        "canalesAnalogicos": str(header[21]),
        "canalesInAmp": str(header[22]),
        "canalesDigitales": str(header[23]),
        "codigoInicio": __codigosInicioReg[str(header[24])]
    }

    return headerToRet
