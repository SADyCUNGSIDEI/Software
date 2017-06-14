
from PyQt4.Qt import QTabWidget, QLabel, QHBoxLayout
from PyQt4 import QtGui
from modoOnlineDigital import ModoOnlineDigital
from PyQt4.QtGui import QSpinBox, QVBoxLayout, QSpacerItem, QSizePolicy


class ModoOnlineView(QtGui.QWidget):
    
    def __init__(self):
        super(ModoOnlineView, self).__init__()
        
        self.init_ui()
    
    def init_ui(self):
        
        tabs = QTabWidget()
        tabs.addTab(ModoOnlineDigital(), "Digital")
        tabs.addTab(QLabel("test"), "Analogico")
        
        freqLayout = QHBoxLayout()
        
        freqSelector = QSpinBox()
        freqSelector.setMinimum(100)
        freqSelector.setMaximum(100000)
        freqSelector.setValue(10000)
        
        freqLayout.addSpacing(400)
        freqLayout.addWidget(QLabel("<b>Frequencia de medicion (Hz): </b>"))#Negrita
        freqLayout.addWidget(freqSelector)
        
        mainLay = QVBoxLayout()
        
        mainLay.addWidget(tabs)
        mainLay.addLayout(freqLayout)
        
        self.setLayout(mainLay)
        
    
    