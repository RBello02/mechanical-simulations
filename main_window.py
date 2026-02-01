import sys
from PyQt5.QtWidgets import QApplication
from Interface.Simulation import Simulation
from Objects.Ball import Ball

app = QApplication(sys.argv)

sim_win = Simulation(height=600, wide=600)

# crea palline
ball1 = Ball(10, [0,0], [1,1], radios=20)
sim_win.add_ball(ball1)

sim_win.animate()

sys.exit(app.exec_())