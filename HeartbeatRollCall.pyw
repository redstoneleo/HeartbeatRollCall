from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from PyQt4.QtWidgets import *
from UI.MainWindow import MainWindow


def main():

    import sys
    app = QApplication(sys.argv)

    translator = QTranslator()
    translator.load("qt_zh_CN.qm")
    app.installTranslator(translator)

    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
