
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


class GraficoAnalogico():

    pendiente = 1
    ordenada = 0
    unidad = ""

    def __init__(self, pendiente=1, ordenada=0, unidad="", nombre=""):
        self.window = plot(title=nombre, labels={'left': unidad})
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

    def __init__(self, nombre, negado):
        GraficoAnalogico.__init__(self, nombre=nombre)
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
