
__codigosInicioReg = {"0": "vueltaEnergia",
                      "1": "init",
                      "2": "descargaDatos",
                      "3": "watchdog"}


def decode(data):

    toRet = []
    i = 0

    while i < len(data):
        if  len(data) >= i + 28 and __isHeader(data[i: i + 28]):
            currentHeader = __translateHeader(data[i:i + 28])
            toRet.append({"type": "header",
                          "data": currentHeader})

            i += 27
        else:
            cantAnalogicos = int(currentHeader["canalesAnalogicos"])
            cantAnalogicosAmp = int(currentHeader["canalesInAmp"])
            cantDigitales = int(currentHeader["canalesDigitales"])

            offsetAnalog = cantAnalogicos * 2
            offsetInAmp = (cantAnalogicos * 2) + (cantAnalogicosAmp * 2)

            analogRawData = data[i:i + offsetAnalog]
            inAmpRawData = data[i + offsetAnalog:i + offsetInAmp]
            digitalRawData = data[i + offsetInAmp]

            analogData = []
            inAmpData = []
            digitalData = []

            for analog in range(0, len(analogRawData), 2):
                analogData.append(__getAnalogValue(
                    analogRawData[analog], analogRawData[analog + 1]))

            for inAmp in range(0, len(inAmpRawData), 2):
                inAmpData.append(__getAnalogValue(
                    inAmpRawData[inAmp], inAmpRawData[inAmp + 1]))

            digitalData = __getDigitalValues(digitalRawData, cantDigitales)

            dataSection = {"analogicos": analogData,
                           "inAmp": inAmpData,
                           "digitales": digitalData}

            toRet.append({"type": "dataSection",
                          "data": dataSection})

            # dos bytes por cada canal analogico, dos por cada canal in amp, y
            # uno por TODOS los digitales
            i = i + (cantAnalogicos * 2) + (cantAnalogicosAmp * 2) + 1

    return toRet


def __isHeader(toTest):
    if toTest[0] != "\xFF" or toTest[1] != "\xFF":
        return False
    if toTest[25] != "\xFF" or toTest[26] != "\xFF":
        return False

    for char in toTest[2:23]:
        if ord(char) - 48 >= 10 or ord(char) - 30 < 0:
            return False

    return True 

def __getAnalogValue(lowByte, highByte):
    lowDecimal = ord(lowByte)
    highDecimal = ord(highByte)

    return (highDecimal << 8) + lowDecimal


def __getDigitalValues(byte, cant):
    binaryData = bin(ord(byte))[8:1:-1]#al reves
    binaryData = binaryData + "00000000" # para que aparezcan almenos 8 bits. Si sobra no importa
    toRet = []

    for i in range(cant):
        if binaryData[i] == "0":
            toRet.append(False)
        else:
            toRet.append(True)

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


