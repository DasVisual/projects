#! python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

'''Used PyQt5 template from pythonspot.com'''
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Alhamdulillah App: Get Closer to God'
        self.left = 500
        self.top = 350
        self.width = 480
        self.height = 300
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        button = QPushButton('Alhamdulillah', self)
        button.setToolTip('This gives you one alhamdulillah')
        button.move(200,130) 
        button.clicked.connect(self.on_click)
 
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        print('+1 alhamdulillah')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())