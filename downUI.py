# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'down01.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 227)
        MainWindow.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 361, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 60, 271, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 60, 83, 31))
        self.pushButton_2.setStyleSheet("\n"
"    font: 75 11pt \"DejaVu Sans\";\n"
"    background-color: rgb(186, 189, 182);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 140, 151, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font: 75 11pt \"DejaVu Sans\";\n"
"    background-color: rgb(46, 52, 54);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    \n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(90, 100, 361, 23))
        self.progressBar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.label.setStyleSheet("font: 75 italic 13pt \"Z003\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 64, 17))
        self.label_2.setStyleSheet("font: 75 italic 13pt \"Z003\";")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menuFile.addAction(self.actionexit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.pushButton.setText(_translate("MainWindow", "Start Download"))
        self.label.setText(_translate("MainWindow", "Enter URL"))
        self.label_2.setText(_translate("MainWindow", "Location"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
