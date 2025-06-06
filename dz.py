from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 351, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 120, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 160, 241, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 200, 241, 16))
        self.label_4.setObjectName("label_4")
        self.line_T = QtWidgets.QLineEdit(self.centralwidget)
        self.line_T.setGeometry(QtCore.QRect(460, 120, 113, 22))
        self.line_T.setObjectName("line_T")
        self.line_Tenv = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Tenv.setGeometry(QtCore.QRect(460, 160, 113, 22))
        self.line_Tenv.setObjectName("line_Tenv")
        self.line_k = QtWidgets.QLineEdit(self.centralwidget)
        self.line_k.setGeometry(QtCore.QRect(460, 200, 113, 22))
        self.line_k.setObjectName("line_k")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 230, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(101, 90, 255, 255), stop:1 rgba(255, 112, 112, 255));")
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 791, 571))
        self.widget.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(101, 90, 255, 255), stop:1 rgba(255, 112, 112, 255));\n"
"")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.line_T.raise_()
        self.line_Tenv.raise_()
        self.line_k.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translateMoreactions
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "График изменения Т"))
        self.label_2.setText(_translate("MainWindow", "Температура тела, °C"))
        self.label_3.setText(_translate("MainWindow", "Температура окружающей среды, °C"))
        self.label_4.setText(_translate("MainWindow", "коэффициент теплообмена, 1/с"))
        self.pushButton.setText(_translate("MainWindow", "Построить график"))