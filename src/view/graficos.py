
import pyqtgraph as pg

from PyQt4 import QtGui


class Grafico():

    def __init__(self):
        self.window = pg.plot(pen='y')
        self.window.resize(400, 250)
        self.plotItem = self.window.getPlotItem()
        self.curve = self.plotItem.plot()
        self.data = []

    def addData(self, newData):
        self.data.append(newData)
        self.plotItem.setXRange(len(self.data) - 20 , len(self.data) + 20)
        self.curve.setData(self.data)


