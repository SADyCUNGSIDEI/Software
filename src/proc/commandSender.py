import serial

CANT_ANALOG_MAX = 8
CANT_ANALOG_MIN = 0
commandChar = "\x1B"
endChar = "\x13"
port = serial.Serial("/dev/pts/8", 9600, timeout=1)


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


def setCantAnalogInAmp(cantAnalogInAmp):
    charCantAnalog = chr(cantAnalogInAmp + 48)
    __send("B" + charCantAnalog)


def setAmpForInAmp(amp, pinInAmp):
    inAmpStr = str(pinInAmp + 9)  # de 09 a 12
    if pinInAmp + 9 < 10:
        inAmpStr = "0" + inAmpStr

    ampChar = chr(amp)  # de 0 a 3

    __send("C" + inAmpStr + ampChar)


def setTimingOfReciv(miliseconds):

    __send("T" + str(miliseconds))


def setTimingOfRegistro(seconds):
    __send("R" + str(seconds))


def setDateTime(dateTimeStr):
    __send("H" + dateTimeStr)


def getDateTime():
    __send("h")

    return read(14)

def setPinesMedTiempo(pin1, pin2):
    __send("D" + str(pin1) + str(pin2))#TODO: se mandan como strings?


def read(cantBytes):
    return port.read(cantBytes)

def readLine():

    line = ""
    while True:
        char = read(1)
        if char == "\n":
            break
        line +=char
    return line

def getFromRegistro():
    __send("d")

    registro = read(port.inWaiting())

    return registro


def __send(data):
    port.write(commandChar + data + endChar)
