
from graficosUtils import plot


class Graficos():

    analogs = []
    digitals = []

    def __init__(self, dataAnalog, dataDigital):

        for (pendiente, ordenada, unidad, nombre) in dataAnalog:
            self.analogs.append(GraficoAnalogico(
                pendiente, ordenada, unidad, nombre))

        for (nombre, negado) in dataDigital:
            self.digitals.append(GraficoDigital(nombre, negado))

    def actualizeAnalogicos(self, data):
        for i in range(len(data)):
            self.analogs[i].addData(data[i])

    def actualizeDigitales(self, data):
        for i in range(len(self.digitals)):
            self.digitals[i].addData(data[i])

    def closeAll(self):

        for graficoAnalogico in self.analogs:
            graficoAnalogico.close()

        for graficoDigital in self.digitals:
            graficoDigital.close()

        del self.analogs[:]
        del self.digitals[:]


class GraficosRegistro():

    analogs = []
    inAmps = []
    digitals = []

    def __init__(self, cantAnalogicos, cantInAmp, cantDigitales, dateString):

        for i in range(cantAnalogicos):
            self.analogs.append(GraficoAnalogico(
                nombre=dateString, isUnclosable=False))

        for i in range(cantInAmp):
            self.inAmps.append(GraficoAnalogico(
                nombre=dateString, isUnclosable=False))

        for i in range(cantDigitales):
            self.digitals.append(GraficoDigital(
                nombre=dateString, isUnclosable=False))

    def actualizeAll(self, dataAnalog, dataInAmp, dataDigital):
        for i in range(len(dataAnalog)):
            self.analogs[i].addData(dataAnalog[i])

        for i in range(len(dataInAmp)):
            self.inAmps[i].addData(dataInAmp[i])

        for i in range(len(dataDigital)):
            if dataDigital[i]:
                self.digitals[i].addData(1)
            else:
                self.digitals[i].addData(0)

    def closeAll(self):

        for graficoAnalogico in self.analogs:
            graficoAnalogico.close()

        for graficoDigital in self.digitals:
            graficoDigital.close()

        del self.analogs[:]
        del self.digitals[:]


class GraficoAnalogico():

    pendiente = 1
    ordenada = 0
    unidad = ""

    def __init__(self, pendiente=1, ordenada=0, unidad="", nombre="Grafico Analogico", isUnclosable=True):
        self.window = plot(title=nombre, labels={
                           'left': unidad}, isUnclosable=isUnclosable)
        self.window.resize(400, 250)
        self.plotItem = self.window.getPlotItem()
        self.curve = self.plotItem.plot()
        self.data = []

        self.pendiente = pendiente
        self.ordenada = ordenada
        self.unidad = unidad

    def addData(self, newData):
        self.data.append((newData * self.pendiente) + self.ordenada)
        self.plotItem.setXRange(len(self.data) - 20, len(self.data) + 20)
        self.curve.setData(self.data, pen='y')

    def close(self):
        self.window.close()


class GraficoDigital(GraficoAnalogico):

    def __init__(self, nombre="Grafico Digital", negado=False, isUnclosable=True):
        GraficoAnalogico.__init__(
            self, nombre=nombre, isUnclosable=isUnclosable)
        self.negado = negado
        self.window.resize(250, 100)

    def addData(self, newData):
        trueData = newData
        if self.negado:
            trueData = 1 - newData

        self.data.append(trueData)

        self.plotItem.setXRange(len(self.data) - 5, len(self.data) + 5)

        if trueData == 1:
            self.curve.setData(self.data, pen='g')
        else:
            self.curve.setData(self.data, pen='r')


def openGraficosOf(data):

    firstHeader = data[0]

    cantAnalogicos = int(firstHeader["data"]["canalesAnalogicos"])
    cantInAmp = int(firstHeader["data"]["canalesInAmp"])
    cantDigitales = int(firstHeader["data"]["canalesDigitales"])

    dateString = firstHeader["data"]["anio"] + "/" + \
        firstHeader["data"]["mes"] + \
        "/" + firstHeader["data"]["dia"] + \
        " " + firstHeader["data"]["hora"] + ":" + \
        firstHeader["data"]["minutos"] + ":" + firstHeader["data"]["segundos"]

    graficos = GraficosRegistro(
        cantAnalogicos, cantInAmp, cantDigitales, dateString)

    for d in data:
        if d["type"] == "dataSection":
            dataAnalog = d["data"]["analogicos"]
            dataInAmp = d["data"]["inAmp"]
            dataDigital = d["data"]["digitales"]

            graficos.actualizeAll(dataAnalog, dataInAmp, dataDigital)
