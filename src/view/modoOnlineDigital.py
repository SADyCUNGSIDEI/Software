
from PyQt4 import QtGui
from PyQt4.QtGui import QCheckBox
from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QLineEdit


class DigitalInputView(QtGui.QFrame):

    _nombreInput = ""
    mainLayout = None

    def __init__(self, nombre, parent=None):

        self._nombreInput = nombre
        super(DigitalInputView, self).__init__(parent)
        self.setObjectName("DigitalInputView")
        self.setStyleSheet(
            "#DigitalInputView {border:1px solid rgb(0, 0, 0); }")
        self.initUI()

    def initUI(self):
        self.mainLayout = QGridLayout()

        nombreInputLbl = QLabel(self._nombreInput)

        self.negarChk = QCheckBox("Negar")
        self.activadoChk = QCheckBox("Activar")

        self.activadoChk.setChecked(False)
        self.activadoChk.stateChanged.connect(self.activarChanged)

        self.negarChk.setChecked(False)
        self.negarChk.stateChanged.connect(self.negadoChange)

        self.nombreTxt = QLineEdit()

        self.nombreTxt.setEnabled(False)

        self.mainLayout.addWidget(nombreInputLbl, 0, 0)
        self.mainLayout.addWidget(self.activadoChk, 0, 1)
        self.mainLayout.addWidget(self.negarChk, 0, 2)

        self.mainLayout.addWidget(QLabel("Nombre: "), 1, 0)

        self.mainLayout.addWidget(self.nombreTxt, 1, 1)

        self.setLayout(self.mainLayout)

    def negadoChange(self):
        pass

    def activarChanged(self):
        if(self.activadoChk.isChecked()):
            self.nombreTxt.setEnabled(True)
        else:
            self.nombreTxt.setEnabled(False)


class ModoOnlineDigital(QtGui.QWidget):

    _mainLayout = None

    def __init__(self):
        super(ModoOnlineDigital, self).__init__()

        self.init_gui()

    def init_gui(self):
        self._mainLayout = QGridLayout()

        self._mainLayout.addWidget(DigitalInputView("Input 1"), 0, 0)
        self._mainLayout.addWidget(DigitalInputView("Input 2"), 0, 1)
        self._mainLayout.addWidget(DigitalInputView("Input 3"), 1, 0)
        self._mainLayout.addWidget(DigitalInputView("Input 4"), 1, 1)
        self._mainLayout.addWidget(DigitalInputView("Input 5"), 2, 0)
        self._mainLayout.addWidget(DigitalInputView("Input 6"), 2, 1)
        self._mainLayout.addWidget(DigitalInputView("Input 7"), 3, 0)
        self._mainLayout.addWidget(DigitalInputView("Input 8"), 3, 1)

        self.setLayout(self._mainLayout)
