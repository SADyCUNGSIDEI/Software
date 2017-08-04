
import sys

import os
from PyQt4 import QtGui, uic
from PyQt4.QtGui import QFileDialog
from modoAdquisicionView import ModoAdquisicionView

import graficos
from relojConfig import RelojConfig

sys.path.append('../proc')
import modoAdquisicionService
import fileService


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):

        uic.loadUi("../../gui/mainwindow.ui", self)
        self.setCentralWidget(ModoAdquisicionView())

        self.actionDescargar_Datos.triggered.connect(self.descargaDatos)
        self.actionAbrir_Graficos.triggered.connect(self.abrirGraficos)
        self.actionSetear_Reloj.triggered.connect(self.configReloj)

        self.show()

    def descargaDatos(self):
        fname = QFileDialog.getSaveFileName(self, 'Guardar como archivo de registro',
                                            os.path.expanduser('~user'), "SADyC Registrer Files (*.sre)")
        if fname is not None:
            registroData = modoAdquisicionService.getFromRegistro()
            fileService.saveRegistroData(fname, registroData)

    def abrirGraficos(self):
        fname = QFileDialog.getOpenFileName(self, 'Guardar como archivo de registro',
                                            os.path.expanduser('~user'), "SADyC Registrer Files (*.sre)")

        if fname is not None:
            data = fileService.openGraficoData(fname)
            graficos.openGraficosOf(data)

    def configReloj(self):
        self.relojConfig = RelojConfig()
        self.relojConfig.show()


def main():

    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
