
from PyQt4 import QtGui, QtCore, uic
import pyqtgraph as pg


class PlotWindow(pg.PlotWidget):

    def __init__(self, title=None,**kargs):
        pg.mkQApp()
        if kargs["isUnclosable"]:
            self.win = UnclosableMainWindow()
        else:
            self.win = QtGui.QMainWindow()

        self.layout = QtGui.QVBoxLayout()

        pg.PlotWidget.__init__(self, **kargs)
        self.layout.addWidget(self)
        self.layout.addWidget(QtGui.QLabel("Intervalo de Medicion: " + kargs["intervaloStr"]))
        self.layout.addWidget(QtGui.QLabel("Fecha de Inicio: " + kargs["fechaStr"]))

        centralWid = QtGui.QWidget()
        centralWid.setLayout(self.layout)

        self.win.setCentralWidget(centralWid)

        for m in ['resize']:
            setattr(self, m, getattr(self.win, m))
        if title is not None:
            self.win.setWindowTitle(title)
        self.showGrid(True, False, 1.0)
        self.win.show()


class UnclosableMainWindow(QtGui.QMainWindow):

    wantToClose = False

    def __init__(self):
        super(UnclosableMainWindow, self).__init__()

    def close(self):
        self.wantToClose = True
        QtCore.QCoreApplication.instance().quit()

    def closeEvent(self, evnt):
        if self.wantToClose:
            super(UnclosableMainWindow, self).closeEvent(evnt)
        else:
            evnt.ignore()


def plot(*args, **kargs):

    pg.mkQApp()

    pwArgList = ['title', 'labels', 'name', 'left',
                 'right', 'top', 'bottom', 'background', "isUnclosable",
                 "intervaloStr", "fechaStr"]
    pwArgs = {}
    dataArgs = {}
    for k in kargs:
        if k in pwArgList:
            pwArgs[k] = kargs[k]
        else:
            dataArgs[k] = kargs[k]

    w = PlotWindow(**pwArgs)
    if len(args) > 0 or len(dataArgs) > 0:
        w.plot(*args, **dataArgs)
    w.show()

    return w
