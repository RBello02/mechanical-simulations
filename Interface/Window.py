import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets

class Window:
    def __init__(self, height=600, wide=600, title=None):

        # prepare the window

        self.win = pg.GraphicsLayoutWidget(show=True)

        if title is not None:
            self.win.setWindowTitle(title)

        self.win.resize(height, wide)

        self.plot = self.win.addPlot()
        self.plot.setXRange(0, wide)
        self.plot.setYRange(0, height)
        self.plot.setAspectLocked(True) 
        self.plot.hideAxis('bottom')
        self.plot.hideAxis('left')

        # save param

        self.height = height
        self.wide = wide 

    def draw_ball(self, ball):
        
        circle = QtWidgets.QGraphicsEllipseItem(
            ball.x - ball.radios, 
            ball.y - ball.radios, 
            2*ball.radios, 
            2*ball.radios
        )
        circle.setBrush(QtGui.QBrush(QtGui.QColor(255, 0, 0)))  #red
        self.plot.addItem(circle)
        return circle