#! python3

'''Gross profit calculator
	created May 13, 2018'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
	def __init__(self):
		super().__init__()
		self.title = 'Profit Calculation'
		self.left = 80
		self.top = 80
		self.width = 220
		self.height = 180
		self.initUI()
 
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		# Button UI for calculate profit
		button = QPushButton('Calculate Profit', self)
		button.setToolTip('This calculates profit')
		button.move(70,55)
		button.clicked.connect(self.on_click)
		
		self.getText()
		self.getSales()
		self.getExpenses()
		self.getChoice()
		
		self.show()
	
	def on_click(self):
		# Displays profit amount
		print(text + ',' ' the calculated profit is: ', '$', i-j)
		
	def getSales(self):
		global i	# Makes variables global to be used # User input sales total
		i, okPressed = QInputDialog.getInt(self, "Sales total (in USD) ","Sales Amount ($0-100000):", 1000, 0, 100000, 500)
		if okPressed:
			print('The sales total is: ', '$', i)

	def getExpenses(self):
		global j	# User input cost of goods
		j, okPressed = QInputDialog.getInt(self, "Expenses/Cost of Goods total (in USD) ","Expenses Amount ($0-100000):", 1000, 0, 100000, 500)
		if okPressed:
			print('The total cost of goods (expenses) is: ', '$', j)
				
	def getChoice(self):
		items = ("1","2","3",'4','5')	# Rating system
		item, okPressed = QInputDialog.getItem(self, "Rating","How satisfied are you with this app?", items, 4, False)
		if okPressed and item > '3':
			print('Thanks for your rating of: ' + item)
		else:
			input('Please explain why you rated us so low ')
 
	def getText(self):
		global text
		text, okPressed = QInputDialog.getText(self, "The user's name","Your name:", QLineEdit.Normal, "")	# Asks for name
		if okPressed and text != '':
			print('Your name is: ' + text)
			
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
		

	
# User input Sales amount


# User input cost of goods/expenses
	
	
# Display profit amount 