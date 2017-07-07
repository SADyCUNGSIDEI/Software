
import sys

from PyQt4 import QtGui, uic
from modoOnlineView import ModoOnlineView


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):

        uic.loadUi("../../gui/mainwindow.ui", self)
        self.setCentralWidget(ModoOnlineView())

        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
