import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtWidgets
from zadanie1 import Ui_MainWindow
import sys
g=9.81
class plot(QtWidgets.QMainWindow):
    def __init__(self):
        super(plot,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUI(self)
        self.ui.button.clicked.connect(self.btClicked)
    def btnClicked(self):
        try:
            speed = float(self.ui.speed.text())
            ugol = float(self.ui.ugol.text())
            ugol_rad= np.radians(ugol)
            t=2*speed* np.sin(ugol_rad)/g
            t_toch=np.linspace(0,t,100)
            x=speed*np.cos(ugol_rad)*t_toch
            y=speed* np.sin(ugol_rad)*t_toch - 0.5*g*t_toch**2
            plt.figure(figsize=(8,6))
            plt.plot(x,y)
            plt.xlabel("Расстояние")
            plt.xlabel("Высота")
            plt.grid(True)
            plt.legend
            plt.show()
        except ValueError:
            None
app=QtWidgets.QApplication([])
window=plot()
window.show()
sys.exit(app.exec())


