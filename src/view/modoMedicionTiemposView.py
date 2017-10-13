from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import QDateTime
from modoAdquisicionAnalog import ModoAutomatAnalog, ModoInstrAnalog
from modoAdquisicionDigital import ModoAdquisicionDigital

from graficos import Graficos

import sys
sys.path.append('../proc')
import modoMedicionTiemposService
import placaService


class ModoMedicionTiemposView(QtGui.QWidget):

    def __init__(self):
        super(ModoMedicionTiemposView, self).__init__()
        self.initUi()
        placaService.changeModeMedicionTiempo()

    def initUi(self):
        uic.loadUi("../../gui/modoMedicionTiemposView.ui", self)
        self.progressBar.setVisible(False)
        self.detener_button.setEnabled(False)

        self.medir_button.clicked.connect(self.iniciaMedicion)
        self.detener_button.clicked.connect(self.detieneMedicion)

        self.fillCombos()

    def iniciaMedicion(self):
        print "inicia medicion"
        self.progressBar.setVisible(True)
        self.detener_button.setEnabled(True)
        self.medir_button.setEnabled(False)

        pin1 = int(self.primerPin_combo.currentText())
        pin2 = int(self.segundoPin_combo.currentText())

        modoMedicionTiemposService.setPines(pin1, pin2)
        modoMedicionTiemposService.medir(self.medicionCompleta)


    def detieneMedicion(self):
        print "detiene Medicion"
        self.progressBar.setVisible(False)
        self.detener_button.setEnabled(False)
        self.medir_button.setEnabled(True)

        placaService.pause()

    def fillCombos(self):
        self.primerPin_combo.addItems(["49", "50", "51", "52", "53"])
        self.segundoPin_combo.addItems(["49", "50", "51", "52", "53"])

    def medicionCompleta(self, microSegundos):
        self.detieneMedicion()
        self.lcdNumber.display(microSegundos)
