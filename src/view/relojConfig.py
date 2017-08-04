
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
        self.horaEquipo_btt.clicked.connect(self.setHoraEquipo)
        self.send_btt.clicked.connect(self.sendHora)
        self.cancel_btt.clicked.connect(self.close)

    def setHoraEquipo(self):
        horaEquipoRaw = placaService.getDateTime()
        horaEquipo = QDateTime(horaEquipoRaw[0], horaEquipoRaw[1],
                               horaEquipoRaw[2], horaEquipoRaw[3],
                               horaEquipoRaw[4], horaEquipoRaw[5])

        self.dateTimeEdit.setDateTime(horaEquipo)

    def setHoraPc(self):
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    def sendHora(self):
        toSend = self.dateTimeEdit.dateTime().toString("yyyy/MM/dd hh:mm:ss")

        placaService.setDateTime(toSend)

        QtGui.QMessageBox.information(self, 'Informacion',
                                      "El reloj del equipo se ha seteado con la hora \n" + toSend,
                                      QtGui.QMessageBox.Ok)
        self.close()

    def actualizeTime(self):
        self.dateTimeEdit.setDateTime(self.dateTimeEdit.dateTime().addSecs(1))
