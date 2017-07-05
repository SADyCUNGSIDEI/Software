
from PyQt4 import QtGui, uic
from modoOnlineAnalog import ModoOnlineAnalog
from modoOnlineDigital import ModoOnlineDigital

from graficos import Graficos

import sys
sys.path.append('../proc')
import modoOnlineService
import placaService


class ModoOnlineView(QtGui.QWidget):  # TODO: cambiar nombre a mas adecuado

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

        self.comenzarBtt.clicked.connect(self.setMedicion)
        self.detenerBtt.clicked.connect(self.pauseMedition)

    def setMedicion(self):
        analogSetUp = self.formAnalogico.getGraficosSetUp()
        digitalSetUp = self.formDigital.getGraficosSetUp()

        if(len(analogSetUp) > 0):
            graficos = Graficos(analogSetUp, digitalSetUp)
            modoOnlineService.setAnalogsInputs(len(analogSetUp))
            modoOnlineService.setTimingForInput(1000)
            modoOnlineService.medir(graficos.actualizeAnalogicos, graficos.actualizeDigitales)

    def pauseMedition(self):
        placaService.pause()
