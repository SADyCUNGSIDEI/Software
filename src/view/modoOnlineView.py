
from PyQt4 import QtGui
from PyQt4.Qt import QHBoxLayout
from PyQt4.Qt import QLabel
from PyQt4.Qt import QTabWidget
from PyQt4.QtGui import QCheckBox
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QSpinBox
from PyQt4.QtGui import QVBoxLayout
from modoOnlineAnalog import ModoOnlineAnalog
from modoOnlineDigital import ModoOnlineDigital

from graficos import Grafico
import sys
sys.path.append('../proc')
import modoOnlineService


class ModoOnlineView(QtGui.QWidget):  # TODO: cambiar nombre a mas adecuado

    def __init__(self):
        super(ModoOnlineView, self).__init__()

        self.init_ui()

    def init_ui(self):

        medirBtt = QPushButton("Medir")

        medirBtt.clicked.connect(self.setMedicion)

        tabs = QTabWidget()
        tabs.addTab(ModoOnlineAnalog(), "Analogico")
        tabs.addTab(ModoOnlineDigital(), "Digital")

        freqLayout = QHBoxLayout()

        freqSelector = QSpinBox()
        freqSelector.setMinimum(100)
        freqSelector.setMaximum(100000)
        freqSelector.setValue(10000)

        freqLayout.addWidget(QLabel("Registro: "))
        freqLayout.addWidget(QCheckBox())
        freqLayout.addSpacing(400)
        freqLayout.addWidget(QLabel("<b>Frequencia " +
                                    "de medicion (Hz): </b>"))  # Negrita

        freqLayout.addWidget(freqSelector)
        freqLayout.addWidget(medirBtt)

        mainLay = QVBoxLayout()

        mainLay.addWidget(tabs)
        mainLay.addLayout(freqLayout)

        self.setLayout(mainLay)

    def setMedicion(self):
        g = Grafico();
        modoOnlineService.setAnalogsInputs(2)
        modoOnlineService.setTimingForInput(1000)
        modoOnlineService.medir(g.addData)


