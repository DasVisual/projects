import pyqtgraph as pg
import random

xVals = [1,2,3]
yVals = [2,4,6]
yVals2 = [5,7,0]

data1 = 1
data2 = 2
data3 = 3

pw = pg.plot(xVals, yVals, pen='r')  # plot x vs y in red
pw.plot(xVals, yVals2, pen='y')

win = pg.GraphicsWindow()  # Automatically generates grids with multiple items
win.addPlot(data1, row=0, col=0)
win.addPlot(data2, row=1, col=1)
win.addPlot(data3, row=2, col=0, colspan=2)

pg.show(imageData)  # imageData must be a numpy array with 2 to 4 dimensions
