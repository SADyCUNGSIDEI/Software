
from PyQt4 import QtGui, uic
from PyQt4.QtCore import QDateTime, QTimer

import sys
sys.path.append('../proc')
import modoOnlineService
import placaService
import fileService


class RelojConfig(QtGui.QDialog):

    def __init__(self):
        super(RelojConfig, self).__init__()
        uic.loadUi("../../gui/relojConfig.ui", self)

        if placaService.isMidiendo():
            self.setEnabled(False)

        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizeTime)
        self.timer.start(1000)


        self.horaPc_btt.clicked.connect(self.setHoraPc)

    def setHoraPc(self):
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    def actualizeTime(self):
        self.dateTimeEdit.setDateTime(self.dateTimeEdit.dateTime().addSecs(1))

if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = RelojConfig()
    gui.show()
    app.exec_()