from PyQt5 import QtCore, QtGui, QtWidgets
from .Window import Window

class Simulation(Window):

    def __init__(self, height = 600, wide = 600):

        super().__init__(height, wide)

        self.ball_items = []
        self.walls = []
        self.counter_walls = 0
        self.counter_balls = 0

    def add_wall(self, wall):
        self.walls.append(wall)
        self.counter_walls += 1

    def add_ball(self, ball):
        self.counter_balls += 1 
        item = self.draw_ball(ball)
        self.ball_items.append((ball, item))

    def animate(self):
        """UPDATE 16ms (~60fps)"""
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update_positions)
        timer.start(16)
        self.timer = timer

    def update_positions(self):
        for ball, item in self.ball_items:
            ball.x += ball.vx
            ball.y += ball.vy
            item.setPos(ball.x - ball.radios, ball.y - ball.radios)