from turtle import position

import self as self
from pygame import Vector2, Vector3
import core




class Player:
def drawGun():
    p1 = Vector2(core.memory("gunPosition").x,core.memory("gunPosition").y) + Vector2(-15, 20).rotate(180-core.memory("gunPosition").z)
    p1.y = -p1.y
    p1 = p1 + core.memory("origine")
    p2 = Vector2(core.memory("gunPosition").x,core.memory("gunPosition").y) + Vector2(0, -20).rotate(180-core.memory("gunPosition").z)
    p2.y = -p2.y
    p2 = p2 + core.memory("origine")
    p3 = Vector2(core.memory("gunPosition").x,core.memory("gunPosition").y) + Vector2(15, 20).rotate(180-core.memory("gunPosition").z)
    p3.y = -p3.y
    p3 = p3 + core.memory("origine")
    p4 = Vector2(core.memory("gunPosition").x,core.memory("gunPosition").y) + Vector2(0, 5).rotate(180-core.memory("gunPosition").z)
    p4.y = -p4.y
    p4 = p4 + core.memory("origine")

    core.Draw.polygon((255, 255, 255), ((p1), (p2), (p3), (p4)))

def moveGun():
    core.memory("gunHistorique").append(Vector2(core.memory("gunPosition").x,-core.memory("gunPosition").y)+ core.memory("origine"))

    if core.getKeyPressList("z"):
        vel = Vector2(0,1)
        posx = core.memory("gunPosition").x + vel.x
        posy = core.memory("gunPosition").y + vel.y
        angle = core.memory("gunPosition").z
        core.memory("gunPosition", Vector3(posx, posy, angle))


    if core.getKeyPressList("q"):
        vel = Vector2(0,0)
        posx = core.memory("gunPosition").x + vel.x
        posy = core.memory("gunPosition").y + vel.y
        angle = ( vel.angle_to(Vector2(0,180)) + core.memory("gunPosition").z )
        core.memory("gunPosition", Vector3(posx, posy, angle))

    if core.getKeyPressList("d"):
        vel = Vector2(0,0)
        posx = core.memory("gunPosition").x + vel.x
        posy = core.memory("gunPosition").y + vel.y
        angle = p1=p1.rotate(1)
        core.memory("gunPosition", Vector3(posx, posy, angle))


        self.gun.update()
        self.gun.show()
        self.gun()
def control(self):
    if core.getKeyPressList("z"):
        acc = Vector2(self.gun.orientation)
        acc.scale_to_length(self.gun.acc.lenght()+0.1)
        self.gun.acc = Vector2(acc)
    if core.getKeyPressList("s"):
        if self.gun.acc.lenght() -0.1 > 0:
            self.gun.acc.scale_to_length(self.gun.acc.lenght()-0.1)
    if core.getKeyPressList("q"):
        self.gun.orientation=self.gun.orientation.rotate(-5)
    if core.getKeyPressList("d"):
        self.gun.orientation = self.gun.orientation.rotate(5)

