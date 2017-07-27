
import sys

import os
from PyQt4 import QtGui, uic
from PyQt4.QtGui import QFileDialog
from modoOnlineView import ModoOnlineView

import graficos

sys.path.append('../proc')
import modoOnlineService
import placaService
import fileService


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):

        uic.loadUi("../../gui/mainwindow.ui", self)
        self.setCentralWidget(ModoOnlineView())

        self.actionDescargar_Datos.triggered.connect(self.descargaDatos)
        self.actionAbrir_Graficos.triggered.connect(self.abrirGraficos)

        self.show()

    def descargaDatos(self):
        fname = QFileDialog.getSaveFileName(self, 'Guardar como archivo de registro',
                                            os.path.expanduser('~user'), "SADyC Registrer Files (*.sre)")
        if fname is not None:
            registroData = modoOnlineService.getFromRegistro()
            fileService.saveRegistroData(fname, registroData)

    def abrirGraficos(self):
        fname = QFileDialog.getOpenFileName(self, 'Guardar como archivo de registro',
                                            os.path.expanduser('~user'), "SADyC Registrer Files (*.sre)")

        if fname is not None:
            data = fileService.openGraficoData(fname)
            graficos.openGraficosOf(data)


def main():

    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
