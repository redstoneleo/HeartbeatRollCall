# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

from .Ui_MainWindow import Ui_MainWindow
from .ConfigWindow import Dialog
from .Wizard import Wizard
import random
import sys
import pickle
import autorun
import copy


class MainWindow(QMainWindow, Ui_MainWindow):

    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (QWidget)
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.readSettings()

        self.manager = QNetworkAccessManager()
        self.checkUpdate()

        autorun.add("HeartbeatRollCall", sys.argv[0])

    def readSettings(self):  # 读取设置的数据
        self.dataBaseName = 'data.pickle'
        try:
            with open(self.dataBaseName, 'rb') as f:
                self.dataDict = pickle.load(f)
        except FileNotFoundError:  # 尤其是第一次不存在这个文件的时候发生，把文件删了清空数据重启也会发生
            self.dataDict = {}  # 必须有，用于接下来的创建Wizard
            self.on_openWizard_triggered()

    @pyqtSlot()
    def on_openWizard_triggered(self):

        wizard = Wizard(self, self.dataDict)

        if wizard.exec() == QDialog.Accepted:
            print('Accepted---------------')
            # 赋予self.dataDict新内容
            self.dataDict['admin'] = {
                wizard.wizardPage1.field('className'): wizard.wizardPage1.field('password')}
            nameList = wizard.textEdit.toPlainText().splitlines()
            random.shuffle(nameList)  # 必须混乱，否则会导致选人的顺序按照excel表格顺序来选，影响效果
            self.dataDict['students'] = nameList
            self.dataDict['unpicked'] = copy.deepcopy(nameList)

            # 必须立即写入本地才能确保持久保存，因为self.dataDict已经被赋予新值，所以写入本地之后也不用重新读取它的值了
            with open(self.dataBaseName, 'wb') as f:
                pickle.dump(self.dataDict, f)

        # 有个变态的做法：首次设置账号密码后不输入学生名单（按cancel）就会导致这个条件为True，那么让pickButton不能用，否则的话按pickButton的时候就会pop空list，出问题
        elif 'students' not in self.dataDict:
            self.pickButton.setEnabled(False)

    @pyqtSlot()
    def on_pickButton_clicked(self):
        """
        random sampling without replacement
        """
#         print('before poped-----------', self.dataDict)

        try:
            picked = self.dataDict['unpicked'].pop()

        except IndexError:  # 名字没有了导致IndexError
            print('名字没有了')
            nameList = self.dataDict['students']
            random.shuffle(nameList)  # 重新再混乱一次，这样就和上一轮的顺序不同了
            # 混乱之后,deepcopy一份存入unpicked，直接引用则都是指向同一对象
            # 浅copy会导致指向同一个nameList，使得unpicked和students的数据不能独立
            self.dataDict['unpicked'] = copy.deepcopy(nameList)
            picked = self.dataDict['unpicked'].pop()

        finally:
            self.label.setText(picked)
            print('poped-----------', self.dataDict)
            # pop之后赶快存入本地，这样才能确保选过的学生确实被记录了
            with open(self.dataBaseName, 'wb') as f:
                pickle.dump(self.dataDict, f)

    @pyqtSlot()
    def on_about_triggered(self):
        Dialog(self).exec()

    @pyqtSlot()
    def on_autoRun_triggered(self, checked):
        if checked:
            autorun.add("HeartbeatRollCall", sys.argv[0])
        else:
            autorun.remove("HeartbeatRollCall")
        print('exists("test_xxx")---------',
              autorun.exists("HeartbeatRollCall"))

    def changeEvent(self, event):  # 失去焦点的时候就清空显示名字的label
        if self.isActiveWindow() == False:
#             print('self.isActiveWindow() == False')
            self.label.clear()

        return super().changeEvent(event)

    def getReply(self, url):

        request = QNetworkRequest(QUrl(url))
        userAgent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
        request.setRawHeader('user-agent', userAgent)
        reply = self.manager.get(request)
        return reply

    def checkUpdate(self):
        reply = self.getReply('http://mathjoy.lofter.com/post/42208d_894553a')
        reply.finished.connect(self.checkNewVersion)

    def checkNewVersion(self):
        reply = self.sender()
        pageSrc = reply.readAll()
        content = str(pageSrc.data(), 'utf-8')

        if '心跳点名' in content:
            if '2015-10-15' in content:
                print('no NewVersion')

            else:
                print('has NewVersion')
                standardButton = QMessageBox.information(
                    None, '发现新版本', '确认后将前往官网下载最新版 <strong>心跳点名</strong>')
                if standardButton == QMessageBox.Ok:
                    QDesktopServices.openUrl(reply.url())

        else:
            print('无法访问主页')
            QTimer.singleShot(120000, self.checkUpdate)
