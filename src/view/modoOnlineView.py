
from PyQt4 import QtGui, uic
from modoOnlineAnalog import ModoOnlineAnalog
from modoOnlineDigital import ModoOnlineDigital

from graficos import Graficos

import sys
sys.path.append('../proc')
import modoOnlineService
import placaService


class ModoOnlineView(QtGui.QWidget):  # TODO: cambiar nombre a mas adecuado

    graficos = None
    analogSetUp = []
    digitalSetUp = []

    def __init__(self):
        super(ModoOnlineView, self).__init__()
        placaService.changeModeOnLine()
        self.init_ui()

    def init_ui(self):
        uic.loadUi("../../gui/modoOnlineView.ui", self)

        self.formAnalogico = ModoOnlineAnalog()
        self.formDigital = ModoOnlineDigital()

        self.tabs.addTab(self.formAnalogico, "Analogico")
        self.tabs.addTab(self.formDigital, "Digital")

        self.comenzarBtt.clicked.connect(self.iniciaMedicion)
        self.detenerBtt.clicked.connect(self.stopMedicion)
        self.pausarBtt.clicked.connect(self.pauseMedicion)

    def iniciaMedicion(self):
        if not placaService.isSeteado():
            self.setMedicion()

        if len(self.analogSetUp) > 0 or len(self.digitalSetUp) > 0:

                modoOnlineService.setTimingForInput(
                    int(self.intervaloSpin.text()))
                modoOnlineService.medir(self.graficos.actualizeAnalogicos,
                                        self.graficos.actualizeDigitales)

        self.tabs.setEnabled(False)

        self.comenzarBtt.setEnabled(False)
        self.pausarBtt.setEnabled(True)
        self.detenerBtt.setEnabled(True)

    def pauseMedicion(self):
        placaService.pause()

        self.comenzarBtt.setEnabled(True)
        self.pausarBtt.setEnabled(False)
        self.detenerBtt.setEnabled(True)

    def setMedicion(self):
        self.analogSetUp = self.formAnalogico.getGraficosSetUp()
        self.digitalSetUp = self.formDigital.getGraficosSetUp()

        self.graficos = Graficos(self.analogSetUp, self.digitalSetUp)
        modoOnlineService.setAnalogsInputs(len(self.analogSetUp))

    def stopMedicion(self):
        self.graficos.closeAll()
        placaService.changeModeOnLine()

        self.tabs.setEnabled(True)

        self.comenzarBtt.setEnabled(True)
        self.pausarBtt.setEnabled(False)
        self.detenerBtt.setEnabled(False)
