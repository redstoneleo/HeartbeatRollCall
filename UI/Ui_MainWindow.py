# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\360云盘\编程\Python\Project\HeartbeatRollCall\UI\MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("楷体"))
        font.setPointSize(144)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.pickButton = QtGui.QPushButton(self.centralWidget)
        self.pickButton.setObjectName(_fromUtf8("pickButton"))
        self.verticalLayout.addWidget(self.pickButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu = QtGui.QMenu(self.menuBar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menuBar)
        self.openWizard = QtGui.QAction(MainWindow)
        self.openWizard.setObjectName(_fromUtf8("openWizard"))
        self.about = QtGui.QAction(MainWindow)
        self.about.setObjectName(_fromUtf8("about"))
        self.autoRun = QtGui.QAction(MainWindow)
        self.autoRun.setCheckable(True)
        self.autoRun.setChecked(True)
        self.autoRun.setObjectName(_fromUtf8("autoRun"))
        self.menu.addAction(self.openWizard)
        self.menu.addAction(self.autoRun)
        self.menu.addAction(self.about)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "心跳点名", None))
        self.pickButton.setText(_translate("MainWindow", "抽取幸运星", None))
        self.menu.setTitle(_translate("MainWindow", "帮助", None))
        self.openWizard.setText(_translate("MainWindow", "管理名单", None))
        self.openWizard.setToolTip(_translate("MainWindow", "添加名单", None))
        self.about.setText(_translate("MainWindow", "关于软件", None))
        self.autoRun.setText(_translate("MainWindow", "开机启动", None))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

