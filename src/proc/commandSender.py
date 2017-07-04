import serial

CANT_ANALOG_MAX = 8
CANT_ANALOG_MIN = 1
port = serial.Serial("/dev/pts/11", 9600, timeout=1)


def setCantAnalog(cantAnalog):
    if(cantAnalog < CANT_ANALOG_MIN or cantAnalog > CANT_ANALOG_MAX):
        raise ValueError("la cantidad de canales " +
                         "analogicos deben estar entre " +
                         str(CANT_ANALOG_MIN) + " y " + str(CANT_ANALOG_MAX) +
                         ". Fue " + str(cantAnalog))

    else:

        charCantAnalog = chr(cantAnalog + 48)
        print charCantAnalog
        toSend = "\x1BA" + charCantAnalog + "\x13"
        port.write(toSend)


def setTimingOfReciv(miliseconds):
    port.write("\x1BT1\x13")  # TODO


def read(cantBytes):
    return port.read(cantBytes)
