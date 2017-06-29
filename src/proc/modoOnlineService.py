import commandSender
import threading


def setAnalogsInputs(cantPines):
    commandSender.setCantAnalog(cantPines)


def setTimingForInput(miliseconds):
    commandSender.setTimingOfReciv(miliseconds)


def toThread():
    while True:
        res = commandSender.readLine()
        digital = res[0]
        print bin(ord(digital))


def medir():
    setAnalogsInputs(2)
    setTimingForInput(1000)

    t = threading.Thread(target=toThread)
    t.start()
