#! python3

'''The GUI portion of the pokeScraper
created May 7, 2018'''
'''Tried to fix the modules to work with Qt5 but could not'''

import pandas as pd
import sys, urllib.request
import requests
from PyQt5 import QtGui, QtCore, QtWidgets

class PokeDex(QtWidgets.QWidget):
    
    def __init__(self):
        super(PokeDex, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        '''Initial UI'''
        
        #Grid Layout
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)
        
        #Parse JSON for DataFrame
        self.df = pd.read_json('PokemonData.json')
        self.df = self.df.set_index(['#'])
        
        #Drop Down
        self.dropdown = QtWidgets.QComboBox(self)
        self.names = self.df['Name'].values
        self.dropdown.addItems(self.names)
        self.grid.addWidget(self.dropdown, 0,0,1,1)
        
        #Search Button
        self.btn = QtWidgets.QPushButton('Search', self)
        self.btn.clicked.connect(self.runSearch)      
        self.grid.addWidget(self.btn, 0,1,1,1)
        
        #Image
        self.img = QtWidgets.QLabel(self)
        self.grid.addWidget(self.img, 1,1,1,1)
        
        #Data
        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText('\nName:\n\nType:\n\nHP:\n\nAttack\n\nSp. Attack\n\n Defense:\n\nSp. Defense:\n\nSpeed:\n\nTotal:')
        self.label.setAlignment(QtCore.Qt.AlignLeft)
        self.grid.addWidget(self.label, 1,0,1,1)
        
        #Customize Widgets
        self.resize(500, 250)
        self.center()
        self.setWindowTitle('PokeDex')    
        self.show()
        
    def runSearch(self):
        '''Event for run button'''
        
        #Parse value
        index = self.dropdown.currentIndex()
        val= self.names[index]
        cond = self.df['Name']== val
        
        #Image
        base = 'http://img.pokemondb.net/artwork/'
        img_url = base + val.lower() + '.jpg'
        data = urllib.request(img_url).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        self.img.setPixmap(QtGui.QPixmap(image))
        
        #Set values
        name = 'Name:\t\t\t'+val+'\n\n'
        ty = 'Type:\t\t\t'+ ', '.join(self.df[cond]['Type'].values[0])+'\n\n'
        hp = 'HP:\t\t\t'+ str(self.df[cond]['HP'].values[0])+'\n\n'
        atk = 'Attack:\t\t\t'+str(self.df[cond]['Attack'].values[0])+'\n\n'
        satk = 'Sp. Attack:\t\t'+str(self.df[cond]['Sp. Atk'].values[0])+'\n\n'
        deff = 'Defense:\t\t\t'+str(self.df[cond]['Defense'].values[0])+'\n\n'
        sdef = 'Sp. Defense:\t\t'+str(self.df[cond]['Sp. Def'].values[0])+'\n\n'
        speed = 'Speed:\t\t\t'+str(self.df[cond]['Speed'].values[0])+'\n\n'
        total = 'Total:\t\t\t'+str(self.df[cond]['Total'].values[0])+'\n\n'
        
        #Add text
        final = name+ty+hp+atk+satk+deff+sdef+speed+total
        self.label.setText(final)
        
    def center(self):
        '''Center Widget on screen'''
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
def main():
    '''Codes for running GUI'''
    
    #Create Application object to run GUI
    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    
    #Run GUI
    gui = PokeDex()
    #Exit cleanly when closing GUI
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()