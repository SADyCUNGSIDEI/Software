import serial

CANT_ANALOG_MAX = 8
CANT_ANALOG_MIN = 1
commandChar = "\x1B"
endChar = "\x13"
port = serial.Serial("/dev/pts/17", 9600, timeout=1)


def pause():
    __send("P")


def setMode(mode):
    modeChar = chr(mode)
    __send("E" + modeChar)


def setCantAnalog(cantAnalog):
    if(cantAnalog < CANT_ANALOG_MIN or cantAnalog > CANT_ANALOG_MAX):
        raise ValueError("la cantidad de canales " +
                         "analogicos deben estar entre " +
                         str(CANT_ANALOG_MIN) + " y " + str(CANT_ANALOG_MAX) +
                         ". Fue " + str(cantAnalog))

    else:

        charCantAnalog = chr(cantAnalog + 48)
        __send("A" + charCantAnalog)


def setTimingOfReciv(miliseconds):
    __send("T")  # TODO


def read(cantBytes):
    return port.read(cantBytes)


def __send(data):
    port.write(commandChar + data + endChar)

