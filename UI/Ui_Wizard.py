# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\360云盘\编程\Python\Project\HeartbeatRollCall\UI\Wizard.ui'
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

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName(_fromUtf8("Wizard"))
        Wizard.resize(400, 300)
        Wizard.setWizardStyle(QtGui.QWizard.AeroStyle)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.wizardPage1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.wizardPage1)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.classNameLineEdit = QtGui.QLineEdit(self.wizardPage1)
        self.classNameLineEdit.setObjectName(_fromUtf8("classNameLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.classNameLineEdit)
        self.label_2 = QtGui.QLabel(self.wizardPage1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.passwordLineEdit = QtGui.QLineEdit(self.wizardPage1)
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.passwordLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.wizardPage2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textEdit = QtGui.QTextEdit(self.wizardPage2)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_2.addWidget(self.textEdit)
        self.tipsLabel = QtGui.QLabel(self.wizardPage2)
        self.tipsLabel.setText(_fromUtf8(""))
        self.tipsLabel.setWordWrap(True)
        self.tipsLabel.setObjectName(_fromUtf8("tipsLabel"))
        self.verticalLayout_2.addWidget(self.tipsLabel)
        Wizard.addPage(self.wizardPage2)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(_translate("Wizard", "心跳点名向导", None))
        self.wizardPage1.setTitle(_translate("Wizard", "输入账号", None))
        self.wizardPage1.setSubTitle(_translate("Wizard", "检测到你还没有创建使用数据，请一步一步开始创建吧！", None))
        self.label.setText(_translate("Wizard", "班级名称", None))
        self.label_2.setText(_translate("Wizard", "管理密码", None))
        self.wizardPage2.setTitle(_translate("Wizard", "学生名单管理", None))
        self.wizardPage2.setSubTitle(_translate("Wizard", "请确保每一行只包含一个姓名", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Wizard = QtGui.QWizard()
    ui = Ui_Wizard()
    ui.setupUi(Wizard)
    Wizard.show()
    sys.exit(app.exec_())

