import commandSender
import threading

cantAnalogicos = 0


def setAnalogsInputs(cantPines):
    global cantAnalogicos
    commandSender.setCantAnalog(cantPines)
    cantAnalogicos += cantPines


def setTimingForInput(miliseconds):
    commandSender.setTimingOfReciv(miliseconds)


def medir(callback):

    def toThread():
        while True:
            res = commandSender.read(1 + cantAnalogicos * 2)
            if(res):
                toPlot = ord(res[1]) >> 8
                toPlot += ord(res[2])
                callback(toPlot) 

    t = threading.Thread(target=toThread)
    t.start()
