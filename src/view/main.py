#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This example shows a tooltip on 
a window and a button

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QTabWidget, QWidget, QPushButton, QLineEdit
from PyQt4.Qt import QLabel, QString, QHBoxLayout, QGridLayout
from modoOnlineView import ModoOnlineView

class MainWindow(QtGui.QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        onlineView = ModoOnlineView()
        
        mainLay = QHBoxLayout()
        mainLay.addWidget(onlineView)
        onlineView.show()
        self.setLayout(mainLay)
        
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Sistema de adquisicion de datos y control')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    

    
    