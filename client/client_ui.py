# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client/client.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setStyleSheet("background-color: rgb(94, 92, 100);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 600, 800))
        self.tabWidget.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.tabWidget.setObjectName("tabWidget")
        self.program = QtWidgets.QWidget()
        self.program.setObjectName("program")
        self.send = QtWidgets.QPushButton(self.program)
        self.send.setGeometry(QtCore.QRect(10, 10, 120, 30))
        self.send.setStyleSheet("background-color: rgb(181, 131, 90);")
        self.send.setObjectName("send")
        self.message = QtWidgets.QTextEdit(self.program)
        self.message.setGeometry(QtCore.QRect(10, 45, 575, 715))
        self.message.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"background-color: rgb(205, 171, 143);")
        self.message.setObjectName("message")
        self.tabWidget.addTab(self.program, "")
        self.answer = QtWidgets.QWidget()
        self.answer.setObjectName("answer")
        self.result = QtWidgets.QLabel(self.answer)
        self.result.setGeometry(QtCore.QRect(10, 10, 575, 750))
        self.result.setStyleSheet("background-color: rgb(205, 171, 143);")
        self.result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.result.setObjectName("result")
        self.tabWidget.addTab(self.answer, "")
        self.support = QtWidgets.QWidget()
        self.support.setObjectName("support")
        self.tabWidget.addTab(self.support, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.send.setText(_translate("MainWindow", "send"))
        self.message.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.program), _translate("MainWindow", "program"))
        self.result.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.answer), _translate("MainWindow", "answer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.support), _translate("MainWindow", "support"))
