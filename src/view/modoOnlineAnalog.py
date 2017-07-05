
from PyQt4 import QtGui, uic
from PyQt4.QtGui import QCheckBox
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
        self.tipoInput.setText(self.tipoInput.text() + " " + str(self.numero))

    def isActivated(self):
        return self.activadoChk.isChecked()

    def getSetUp(self):
        if(self.calibrarChk.isChecked()):
            pend = float(self.pendienteTxt.text())
            orde = float(self.ordenadaTxt.text())
        else:
            pend = 1
            orde = 0

        unidad = self.unidadTxt.text()
        nombre = self.nombreTxt.text()

        return (pend, orde, unidad, nombre)


class ModoOnlineAnalog(QtGui.QWidget):

    _mainLayout = None

    def __init__(self):
        super(ModoOnlineAnalog, self).__init__()

        self.init_gui()

    def init_gui(self):
        self._mainLayout = QGridLayout()

        self.miniForms = [AnalogInputView(1),
                          AnalogInputView(2),
                          AnalogInputView(3),
                          AnalogInputView(4),
                          AnalogInputView(5),
                          AnalogInputView(6),
                          AnalogInputView(7),
                          AnalogInputView(8)]

        self._mainLayout.addWidget(self.miniForms[0], 0, 0)
        self._mainLayout.addWidget(self.miniForms[1], 0, 1)
        self._mainLayout.addWidget(self.miniForms[2], 1, 0)
        self._mainLayout.addWidget(self.miniForms[3], 1, 1)
        self._mainLayout.addWidget(self.miniForms[4], 2, 0)
        self._mainLayout.addWidget(self.miniForms[5], 2, 1)
        self._mainLayout.addWidget(self.miniForms[6], 3, 0)
        self._mainLayout.addWidget(self.miniForms[7], 3, 1)

        self.setLayout(self._mainLayout)

    def getGraficosSetUp(self):

        toRet = []

        for miniForm in self.miniForms:
            if miniForm.isActivated():
                toRet.append(miniForm.getSetUp())

        return toRet
