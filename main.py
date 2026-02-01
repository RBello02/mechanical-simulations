import sys
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
import numpy as np

app = QApplication(sys.argv)

# Finestra principale
win = pg.GraphicsLayoutWidget(show=True)
win.setWindowTitle("Pallina che si muove")
win.resize(600, 600)

# Area di disegno
plot = win.addPlot()
plot.setXRange(0, 100)
plot.setYRange(0, 100)
plot.setAspectLocked(True)  # scala uguale su x e y
plot.hideAxis('bottom')
plot.hideAxis('left')

# Pallina
ball = pg.ScatterPlotItem(size=20, brush=pg.mkBrush(255, 0, 0))
plot.addItem(ball)

# Stato iniziale
pos = np.array([50.0, 50.0])
vel = np.array([1.2, 0.8])  # velocità
radius = 10

def update():
    global pos, vel

    pos += vel

    # Rimbalzo sui bordi
    if pos[0] <= radius or pos[0] >= 100 - radius:
        vel[0] *= -1
    if pos[1] <= radius or pos[1] >= 100 - radius:
        vel[1] *= -1

    ball.setData([pos[0]], [pos[1]])

# Timer per animazione
timer = QTimer()
timer.timeout.connect(update)
timer.start(16)  # ~60 FPS

sys.exit(app.exec_())
