# -*- coding: utf-8 -*-

"""
Module implementing Wizard.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .Ui_Wizard import Ui_Wizard
import os


class Wizard(QWizard, Ui_Wizard):

    """
    Class documentation goes here.
    """

    def __init__(self, parent=None, data=None):
        """
        Constructor

        @param parent reference to the parent widget (QWidget)
        """
        super(Wizard, self).__init__(parent)
        self.setupUi(self)

        self.nextButton = self.button(QWizard.NextButton)
        self.nextButton.clicked.connect(self.login)
        self.textEdit.textChanged.connect(self.onTextChanged)
        self.dataDict = data
        if self.dataDict != {}:  # 如果有数据了，那么
            self.wizardPage1.setSubTitle('请输入之前已设置的班级名称和管理密码')
        self.wizardPage1.registerField(
            'className*', self.classNameLineEdit)  # 注册className这个filed，方便后面读取和保证wizardPage1上面的数据都填满之后才enable nextButton
        self.wizardPage1.registerField('password*', self.passwordLineEdit)
        # 注册nameList这个filed，但wizardPage2上面的数据都填满之后并没有enable FinishButton，所以其作用只在让textEdit首次启动没有数据的时候disable FinishButton
        # self.button(QWizard.FinishButton).setEnabled(False)不起作用，因此采用这个蹩脚的方法
        self.wizardPage2.registerField('nameList*', self.textEdit)


    def login(self):

        if self.dataDict:  # 如果之前的数据字典有数据则需要对比账户和密码，否则的话按照Wizard的默认操作，转入下一页
            print('login------------', self.dataDict)
            isSucceed = {self.wizardPage1.field('className'): self.wizardPage1.field(
                'password')} == self.dataDict['admin']
            # 如果登陆不成功的话就会把FinishButton disable
            self.button(QWizard.FinishButton).setEnabled(isSucceed)

            if isSucceed:  # 如果登陆成功，就显示学生名单
                self.textEdit.setPlainText(
                    os.linesep.join(self.dataDict['students']))
            else:
                QMessageBox.critical(self, '登陆错误', '班级名称或管理密码不正确')

    def onTextChanged(self):
        count = len(self.textEdit.toPlainText().splitlines())
#         self.tipsLabel.setText('你录入了{}个学生的名字，请确保一个也不能少！'.format(count))

        self.tipsLabel.setText(
            '<html><head/><body><p><span style=" color:#ff0000;">你录入了{}个学生的名字，请确保一个也不能少！</span></p></body></html>'.format(count))
        # 有内容的时候才会Enable，竟然可以排除空格的情况！！！！
        self.button(QWizard.FinishButton).setEnabled(count)
