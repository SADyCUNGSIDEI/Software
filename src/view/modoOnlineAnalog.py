
from PyQt4 import QtGui, uic
from PyQt4.QtGui import QCheckBox
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QLineEdit


class AnalogInputView(QtGui.QFrame):

    numero = 0

    def __init__(self, numero, parent=None):

        self.numero = numero
        super(AnalogInputView, self).__init__(parent)
        self.initUI()

    def initUI(self):
        uic.loadUi("../../gui/onlineAnalogicoMini.ui", self)
        self.setEnabled(False)
        self.tipoInput.setText(self.tipoInput.text() + " " + str(self.numero))

    def getSetUp(self):
        pend = 1
        orde = 0
        if(self.calibrarChk.isChecked()):
            pend = float(self.pendienteTxt.text())
            orde = float(self.ordenadaTxt.text())

        unidad = self.unidadTxt.text()
        nombre = self.nombreTxt.text()

        return (pend, orde, unidad, nombre)


class ModoOnlineAnalog(QtGui.QWidget):

    _nextMini = 0

    def __init__(self):
        super(ModoOnlineAnalog, self).__init__()

        self.init_gui()

    def init_gui(self):
        uic.loadUi("../../gui/modoOnlineForm.ui", self)

        self.miniForms = []

        for i in range(1, 8 + 1):
            self.miniForms.append(AnalogInputView(i))

        self.mainLayout.addWidget(self.miniForms[0], 0, 0)
        self.mainLayout.addWidget(self.miniForms[1], 0, 1)
        self.mainLayout.addWidget(self.miniForms[2], 1, 0)
        self.mainLayout.addWidget(self.miniForms[3], 1, 1)
        self.mainLayout.addWidget(self.miniForms[4], 2, 0)
        self.mainLayout.addWidget(self.miniForms[5], 2, 1)
        self.mainLayout.addWidget(self.miniForms[6], 3, 0)
        self.mainLayout.addWidget(self.miniForms[7], 3, 1)

        self.addBtt.clicked.connect(self.addMiniForm)
        self.rmvBtt.clicked.connect(self.removeMiniForm)

    def addMiniForm(self):
        self.miniForms[self._nextMini].setEnabled(True)
        if(self._nextMini < len(self.miniForms)):
            self._nextMini += 1

    def removeMiniForm(self):
        if(self._nextMini > 0):
            self._nextMini -= 1

        self.miniForms[self._nextMini].setEnabled(False)

    def getGraficosSetUp(self):

        toRet = []

        for miniForm in self.miniForms:
            if miniForm.isEnabled():
                toRet.append(miniForm.getSetUp())

        return toRet
