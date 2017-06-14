from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QCheckBox, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel,\
    QLineEdit
from PyQt4.QtCore import QRect
from PyQt4.Qt import QPushButton, QWidget
from PIL.ImageDraw2 import Pen


class DigitalInputView(QtGui.QFrame):
    
    
    _nombreInput = ""
    mainLayout = None
    
    def __init__(self, nombre, parent=None):
        
        self._nombreInput = nombre
        super(DigitalInputView, self).__init__(parent)
        self.setObjectName("DigitalInputView")
        self.setStyleSheet("#DigitalInputView {border:1px solid rgb(0, 0, 0); }")
        self.initUI()
        
        
    def initUI(self):
        self.mainLayout = QGridLayout()
        
        nombreInputLbl = QLabel(self._nombreInput)
        
        self.calibrarChk = QCheckBox("Calibrar")
        self.activadoChk = QCheckBox("Activar")
        
        self.activadoChk.setChecked(False)
        self.activadoChk.stateChanged.connect(self.activarChanged)
        
        self.calibrarChk.setChecked(False)
        self.calibrarChk.stateChanged.connect(self.calibrarChanged)
        
        self.nombreTxt = QLineEdit()
        self.unidadTxt = QLineEdit()
        self.pendienteTxt = QLineEdit()
        self.ordenadaTxt = QLineEdit()
        
        self.nombreTxt.setEnabled(False)
        self.unidadTxt.setEnabled(False)
        self.pendienteTxt.setEnabled(False)
        self.ordenadaTxt.setEnabled(False)
        
        self.mainLayout.addWidget(nombreInputLbl, 0 , 0)
        self.mainLayout.addWidget(self.activadoChk, 0 , 1)
        self.mainLayout.addWidget(self.calibrarChk, 0, 2)
        
        self.mainLayout.addWidget(QLabel("Nombre: "), 1 , 0)
        self.mainLayout.addWidget(QLabel("Unidad: "), 2 , 0)
        
        self.mainLayout.addWidget(self.nombreTxt, 1 , 1)
        self.mainLayout.addWidget(self.unidadTxt, 2 , 1)
        
        self.mainLayout.addWidget(QLabel("Pendiente: "), 1, 2)
        self.mainLayout.addWidget(QLabel("Ordenada: "), 2, 2)
        self.mainLayout.addWidget(self.pendienteTxt, 1, 3)
        self.mainLayout.addWidget(self.ordenadaTxt, 2, 3)
    
        self.setLayout(self.mainLayout)
        
        
    def calibrarChanged(self):
        if(self.calibrarChk.isChecked()):
            self.ordenadaTxt.setEnabled(True)
            self.pendienteTxt.setEnabled(True)
        else:
            self.ordenadaTxt.setEnabled(False)
            self.pendienteTxt.setEnabled(False)
            
    def activarChanged(self):
        if(self.activadoChk.isChecked()):
            self.nombreTxt.setEnabled(True)
            self.unidadTxt.setEnabled(True)
        else:
            self.nombreTxt.setEnabled(False)
            self.unidadTxt.setEnabled(False)
        
        

class ModoOnlineDigital(QtGui.QWidget):
    
    _mainLayout = None
    
    def __init__(self):
        super(ModoOnlineDigital, self).__init__()
        
        self.init_gui()
    
    def init_gui(self):
        self._mainLayout = QGridLayout()
        
        self._mainLayout.addWidget(DigitalInputView("Input 1"),0,0)
        self._mainLayout.addWidget(DigitalInputView("Input 2"),0,1)
        self._mainLayout.addWidget(DigitalInputView("Input 3"),1,0)
        self._mainLayout.addWidget(DigitalInputView("Input 4"),1,1)
        self._mainLayout.addWidget(DigitalInputView("Input 5"),2,0)
        self._mainLayout.addWidget(DigitalInputView("Input 6"),2,1)
        self._mainLayout.addWidget(DigitalInputView("Input 7"),3,0)
        self._mainLayout.addWidget(DigitalInputView("Input 8"),3,1)
        
        self.setLayout(self._mainLayout)
        
        
        
        