import time
from turtle import position

import self as self
from pygame import Vector2, Vector3
import core



class Player:
    def __init__(self):
        self.vie = 15
        self.size = 17
        self.vmax = 7
        self.accmax = 2
        self.pos = Vector2(core.WINDOW_SIZE[0] / 2, core.WINDOW_SIZE[1] / 2)
        self.acc = Vector2(0, 0)
        self.vit = Vector2(0, 0)
        self.couleur = (255, 255, 255)
        self.orient = Vector2(-1, 1)
        self.starttime = time.time()

    def show(self):
        orientation = Vector2(self.orient)
        orientation.scale_to_length(30)
        orientation = orientation.rotate(140)

        p1 = self.pos + orientation
        orientation = Vector2(self.orient)
        orientation.scale_to_length(30)
        orientation = orientation.rotate(-140)

        p3 = self.pos + orientation
        orientation = Vector2(self.orient)
        orientation.scale_to_length(20)

        p2 = self.pos + orientation

        core.Draw.text(self.couleur, ("LIFE REMAINING : " + str(self.vie)), (200, 100), 20)
        core.Draw.polygon(self.couleur, (self.pos, p1, p2, p3), 2)
        core.Draw.circle(self.couleur, core.getMouseLocation(), self.size, 2)


    def move(self):
        self.vit += self.acc
        self.pos += self.speed
        if self.vit.length() > self.vmax:
            self.vit.scale_to_length(self.vmax)

        if self.acc.length() > self.accmax:
            self.acc.scale_to_length(self.accmax)
        self.orient = Vector2(core.getMouseLocation()) - self.pos

    def on_edge(self):
        if self.pos.x < 0:
            self.pos.x = core.WINDOW_SIZE[0]
        if self.pos.x > core.WINDOW_SIZE[0]:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = core.WINDOW_SIZE[1]
        if self.pos.y > core.WINDOW_SIZE[1]:
            self.pos.y = 0

    def lose_vie(self):
        if time.time() - self.starttime > 2:
            self.vie -= 1
            self.starttime = time.time()
            print(self.vie)

            self.gun.update()
            self.gun.show()
            self.gun()


