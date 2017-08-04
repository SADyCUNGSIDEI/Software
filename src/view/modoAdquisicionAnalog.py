
from PyQt4 import QtGui, uic


class AnalogInputView(QtGui.QFrame):

    numero = 0

    def __init__(self, numero, parent=None):

        self.numero = numero
        super(AnalogInputView, self).__init__(parent)
        self.initUI()

    def initUI(self):
        uic.loadUi("../../gui/adquisicionAnalogicoMini.ui", self)
        self.setEnabled(False)
        self.tipoInput.setText(self.tipoInput.text() + " " + str(self.numero))

        self.setAmpVisible(False)

    def setAmpVisible(self, visible):
        self.amp_lbl.setVisible(visible)
        self.amp_slider.setVisible(visible)

    def getSetUp(self):
        pend = 1
        orde = 0
        if(self.calibrarChk.isChecked()):
            pend = float(self.pendienteTxt.text())
            orde = float(self.ordenadaTxt.text())

        unidad = str(self.unidadTxt.text())
        nombre = str(self.nombreTxt.text())

        return (pend, orde, unidad, nombre)


class ModoAdquisicionAnalog(QtGui.QWidget):

    _nextMini = 0

    def __init__(self):
        super(ModoAdquisicionAnalog, self).__init__()

        self.init_gui()

    def init_gui(self):
        uic.loadUi("../../gui/modoAdquisicionForm.ui", self)

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


class ModoAutomatAnalog(ModoAdquisicionAnalog):

    def __init__(self):
        super(ModoAutomatAnalog, self).__init__()

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


class ModoInstrAnalog(ModoAdquisicionAnalog):

    def __init__(self):
        super(ModoInstrAnalog, self).__init__()

        self.miniForms = []

        for i in range(1, 4 + 1):
            mini = AnalogInputView(i)
            mini.setAmpVisible(True)
            self.miniForms.append(mini)

        self.mainLayout.addWidget(self.miniForms[0], 0, 0)
        self.mainLayout.addWidget(self.miniForms[1], 0, 1)
        self.mainLayout.addWidget(self.miniForms[2], 1, 0)
        self.mainLayout.addWidget(self.miniForms[3], 1, 1)
