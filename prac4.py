from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 0, 361, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 100, 151, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 140, 151, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 170, 141, 21))
        self.label_4.setObjectName("label_4")
        self.amp = QtWidgets.QLineEdit(self.centralwidget)
        self.amp.setGeometry(QtCore.QRect(330, 110, 113, 22))
        self.amp.setObjectName("amp")
        self.fre = QtWidgets.QLineEdit(self.centralwidget)
        self.fre.setGeometry(QtCore.QRect(330, 140, 113, 22))
        self.fre.setObjectName("fre")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 200, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.k = QtWidgets.QLineEdit(self.centralwidget)
        self.k.setGeometry(QtCore.QRect(330, 170, 113, 22))
        self.k.setObjectName("k")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))Moreactions
        self.label.setText(_translate("MainWindow", "Затухающие колебания"))
        self.label_2.setText(_translate("MainWindow", "Начальная амплитуда, °"))
        self.label_3.setText(_translate("MainWindow", "Частота, ГЦ"))
        self.label_4.setText(_translate("MainWindow", "Коэф затухания, 1/с"))
        self.pushButton.setText(_translate("MainWindow", "Построить график"))


