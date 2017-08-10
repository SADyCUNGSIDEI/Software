
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import QDateTime
from modoAdquisicionAnalog import ModoAutomatAnalog, ModoInstrAnalog
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
    unidadTiempo = "ms"

    def __init__(self):
        super(ModoAdquisicionView, self).__init__()

    def init_ui(self):
        uic.loadUi("../../gui/modoAdquisicionView.ui", self)

        self.tabs.addTab(self.formAnalogico, "Analogico")
        self.tabs.addTab(self.formDigital, "Digital")

        self.registroChk.toggled.connect(self.setRegistro)

        self.comenzarBtt.clicked.connect(self.iniciaMedicion)
        self.detenerBtt.clicked.connect(self.stopMedicion)
        self.pausarBtt.clicked.connect(self.pauseMedicion)

    def setRegistro(self):
        if self.registroChk.isChecked():
            self.intervaloLbl.setText("Intervalo de medicion (<b>s</b>): ")
            self.unidadTiempo = "s"
            self.intervaloSpin.setValue(1)
            self.intervaloSpin.setMinimum(1)
            self.intervaloSpin.setMaximum(3600)
        else:
            self.intervaloLbl.setText("Intervalo de medicion (<b>ms</b>): ")
            self.unidadTiempo = "ms"
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
        modoAdquisicionService.setTimingForRegistro(
            int(self.intervaloSpin.text()))

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

    def openGraficos(self):
        if self.graficos is None:
            intervalo = int(self.intervaloSpin.text())
            self.graficos = Graficos(self.analogSetUp, self.digitalSetUp,
                                    intervalo, self.unidadTiempo, QDateTime.currentDateTime())

    def stopMedicion(self):
        if self.graficos is not None:
            self.graficos.closeAll()
            self.graficos = None

        self.tabs.setEnabled(True)

        self.comenzarBtt.setEnabled(True)
        self.pausarBtt.setEnabled(False)
        self.detenerBtt.setEnabled(False)


class ModoAutomatizacionView(ModoAdquisicionView):

    def __init__(self):
        super(ModoAutomatizacionView, self).__init__()

        placaService.changeModeAutomatOnLine()

        self.formAnalogico = ModoAutomatAnalog()
        self.formDigital = ModoAdquisicionDigital()

        self.init_ui()

        self.modo_lbl.setText("Modo Automatizacion")

    def setMedicion(self):
        super(ModoAutomatizacionView, self).setMedicion()

        if self.registroChk.isChecked():
            placaService.changeModeAutomatRegistro()
        else:
            placaService.changeModeAutomatOnLine()

        modoAdquisicionService.setAnalogsAutomatInputs(len(self.analogSetUp))

    def stopMedicion(self):
        placaService.changeModeAutomatOnLine()
        super(ModoAutomatizacionView, self).stopMedicion()


class ModoInstrumentacionView(ModoAdquisicionView):

    def __init__(self):
        super(ModoInstrumentacionView, self).__init__()

        placaService.changeModeInstrOnLine()

        self.formAnalogico = ModoInstrAnalog()
        self.formDigital = ModoAdquisicionDigital()

        self.init_ui()

        self.modo_lbl.setText("Modo Instrumentacion")

    def setMedicion(self):
        super(ModoInstrumentacionView, self).setMedicion()

        if self.registroChk.isChecked():
            placaService.changeModeInstrRegistro()
        else:
            placaService.changeModeInstrOnLine()

        amps = self.formAnalogico.getAmps()

        modoAdquisicionService.setAnalogsInAmpInputs(len(self.analogSetUp))
        modoAdquisicionService.setAmplificaciones(amps)

    def stopMedicion(self):
        placaService.changeModeInstrOnLine()
        super(ModoInstrumentacionView, self).stopMedicion()
