
from PyQt4 import QtGui, uic
from modoAdquisicionAnalog import ModoAdquisicionAnalog
from modoAdquisicionDigital import ModoAdquisicionDigital

from graficos import Graficos

import sys
sys.path.append('../proc')
import modoAdquisicionService
import placaService


class ModoAdquisicionView(QtGui.QWidget):

    graficos = None
    analogSetUp = []
    digitalSetUp = []

    def __init__(self):
        super(ModoAdquisicionView, self).__init__()
        placaService.changeModeAutomatOnLine()
        self.init_ui()

    def init_ui(self):
        uic.loadUi("../../gui/modoAdquisicionView.ui", self)

        self.formAnalogico = ModoAdquisicionAnalog()
        self.formDigital = ModoAdquisicionDigital()

        self.tabs.addTab(self.formAnalogico, "Analogico")
        self.tabs.addTab(self.formDigital, "Digital")

        self.registroChk.toggled.connect(self.setRegistro)

        self.comenzarBtt.clicked.connect(self.iniciaMedicion)
        self.detenerBtt.clicked.connect(self.stopMedicion)
        self.pausarBtt.clicked.connect(self.pauseMedicion)

    def setRegistro(self):
        if self.registroChk.isChecked():
            self.intervaloLbl.setText("Intervalo de medicion (<b>s</b>): ")
            self.intervaloSpin.setValue(1)
            self.intervaloSpin.setMinimum(1)
            self.intervaloSpin.setMaximum(3600)
        else:
            self.intervaloLbl.setText("Intervalo de medicion (<b>ms</b>): ")
            self.intervaloSpin.setValue(50)
            self.intervaloSpin.setMinimum(1)
            self.intervaloSpin.setMaximum(10000)

    def iniciaMedicion(self):

        if not placaService.isSeteado():
            self.setMedicion()

        if self.registroChk.isChecked():
            self.iniciaRegistro()
        else:
            self.iniciaOnline()

    def iniciaOnline(self):
        placaService.changeModeAutomatOnLine()
        self.openGraficos()

        if len(self.analogSetUp) > 0 or len(self.digitalSetUp) > 0:

            modoAdquisicionService.setTimingForInput(
                int(self.intervaloSpin.text()))
            modoAdquisicionService.medir(self.graficos.actualizeAnalogicos,
                                    self.graficos.actualizeDigitales)

        self.tabs.setEnabled(False)

        self.comenzarBtt.setEnabled(False)
        self.pausarBtt.setEnabled(True)
        self.detenerBtt.setEnabled(True)

    def iniciaRegistro(self):
        placaService.changeModeAutomatRegistro()

        modoAdquisicionService.setTimingForRegistro(int(self.intervaloSpin.text()))

        self.tabs.setEnabled(False)

        self.comenzarBtt.setEnabled(False)
        self.detenerBtt.setEnabled(True)

    def pauseMedicion(self):
        placaService.pause()

        self.comenzarBtt.setEnabled(True)
        self.pausarBtt.setEnabled(False)
        self.detenerBtt.setEnabled(True)

    def setMedicion(self):
        self.analogSetUp = self.formAnalogico.getGraficosSetUp()
        self.digitalSetUp = self.formDigital.getGraficosSetUp()

        modoAdquisicionService.setAnalogsAutomatInputs(len(self.analogSetUp))

    def openGraficos(self):
        self.graficos = Graficos(self.analogSetUp, self.digitalSetUp)

    def stopMedicion(self):
        if self.graficos is not None:
            self.graficos.closeAll()
        placaService.pause()

        self.tabs.setEnabled(True)

        self.comenzarBtt.setEnabled(True)
        self.pausarBtt.setEnabled(False)
        self.detenerBtt.setEnabled(False)


class ModoAutomatizacionView(ModoAdquisicionView):

    def __init__(self):
        pass
