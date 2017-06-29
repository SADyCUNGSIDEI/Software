import serial

CANT_ANALOG_MAX = 8
CANT_ANALOG_MIN = 1
port = serial.Serial("/dev/pts/5")


def setCantAnalog(cantAnalog):
    if(cantAnalog < CANT_ANALOG_MIN or cantAnalog > CANT_ANALOG_MAX):
        raise ValueError("la cantidad de canales " +
                         "analogicos deben estar entre " +
                         CANT_ANALOG_MIN + " y " + CANT_ANALOG_MAX +
                         ". Fue " + cantAnalog)

    else:

        charCantAnalog = chr(cantAnalog + 30)
        toSend = "\x1B" + charCantAnalog + "\x13"
        port.write(toSend)


def setTimingOfReciv(miliseconds):
    port.write("\x1BT1\x13") # TODO


def readLine():
    toRet = ""
    while not toRet.endswith("\x13"):
        toRet += port.read()

    return toRet
