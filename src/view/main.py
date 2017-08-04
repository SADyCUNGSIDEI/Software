
import sys

import os
from PyQt4 import QtGui, uic
from PyQt4.QtGui import QFileDialog, QMessageBox
from modoAdquisicionView import ModoAutomatizacionView, ModoInstrumentacionView

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
        self.setCentralWidget(ModoAutomatizacionView())

        self.actionAutomatizacion.triggered.connect(self.changeModoAutomat)
        self.actionInstrumentacion.triggered.connect(self.changeModoInstr)

        self.actionDescargar_Datos.triggered.connect(self.descargaDatos)
        self.actionAbrir_Graficos.triggered.connect(self.abrirGraficos)
        self.actionSetear_Reloj.triggered.connect(self.configReloj)

        self.show()

    def changeModoInstr(self):
        if self.confirmaChangeModo():
            self.setCentralWidget(ModoInstrumentacionView())

            QMessageBox.information(self, "Cambio de Modo",
                                    "Se cambio a Modo Instrumentacion",
                                    QMessageBox.Ok)

    def changeModoAutomat(self):
        if self.confirmaChangeModo():
            self.setCentralWidget(ModoAutomatizacionView())
            QMessageBox.information(self, "Cambio de Modo",
                                    "Se cambio a Modo Automatizacion",
                                    QMessageBox.Ok)

    def confirmaChangeModo(self):

        res = QMessageBox.question(self, 'Atencion',
                                   "Quiere cambiar de modo? Se perderan los cambios",
                                   QMessageBox.Yes | QMessageBox.No)

        if res == QMessageBox.Yes:
            return True
        else:
            return False

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
