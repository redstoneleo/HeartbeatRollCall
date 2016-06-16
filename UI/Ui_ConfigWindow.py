# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\360云盘\编程\Python\Project\HeartbeatRollCall\UI\ConfigWindow.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(790, 488)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(71, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(Dialog)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_2.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_2.addWidget(self.cancelButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "设置 - 必应好壁纸", None))
        self.groupBox.setTitle(_translate("Dialog", "本软件", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">心跳点名</span>（2015-10-15）可以帮助老师随机公平性地对学生点名！</p><p>点击“管理名单”然后按照心跳点名向导的指示一步一步设置完后，点击“抽取幸运星”按钮或者直接按空格键就可以随机点名了！</p><p><span style=\" color:#0000ff;\">本软件使用不放回随机抽样（random sampling without replacement）点名，所以点名过程中会随机性地点到每一位同学，因而保证了点名的公平性！本软件目前只支持设置一个学生名单，后期将视用户反馈考虑解除这个限制，本软件会自动提示你更新到最新版。</span></p><p><span style=\" color:#0000ff;\">一个人即便不能有好的考试成绩，但必须拥有好的品德，希望老师们不要因为一些学生成绩不好而看不起他们，希望也能够给这部分学生些关爱。</span></p><p><span style=\" font-size:10pt;\">软件主页：</span><a href=\"http://mathjoy.lofter.com/post/42208d_894553a\"><span style=\" text-decoration: underline; color:#0000ff;\">http://mathjoy.lofter.com/post/42208d_894553a</span></a></p><p>问题反馈：redstone-cold@163.com</p><p><span style=\" font-size:10pt;\">用户QQ群（iMath软件）：272830154</span></p></body></html>", None))
        self.groupBox_3.setTitle(_translate("Dialog", "我", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>你好！我喜欢数学、物理、编程（专Python、PyQt）、国语动画、国语布袋戏、看书、看杂志、音乐、乒乓球、羽毛球。</p><p>如果你在软件方面有比较具有创意的点子，但你又不会写软件，那么不妨和我谈谈，我可能帮你把它给做出来哟！</p><p>欢迎光临我的专页：<a href=\"http://mathjoy.lofter.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">http://mathjoy.lofter.com/</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "关于", None))
        self.okButton.setText(_translate("Dialog", "确认", None))
        self.cancelButton.setText(_translate("Dialog", "取消", None))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

