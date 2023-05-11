from pygame import Vector2
import core


def drawGun():
    p1 = Vector2(core.memory("gunPosition").x,core.memory("gunPosition").y) + Vector2(-5, 0).rotate(180-core.memory("gunPosition").z)
    p1.y = -p1.y
    p1 = p1 + core.memory("origine")
    p2 = Vector2(core.memory("gunPosition").x,core.memory("gunPosition").y) + Vector2(0, -15).rotate(180-core.memory("gunPosition").z)
    p2.y = -p2.y
    p2 = p2 + core.memory("origine")
    p3 = Vector2(core.memory("gunPosition").x,core.memory("gunPosition").y) + Vector2(5, 0).rotate(180-core.memory("gunPosition").z)
    p3.y = -p3.y
    p3 = p3 + core.memory("origine")

    core.Draw.polygon((255, 0, 0), ((p1), (p2), (p3)))


def moveGun():
    core.memory("gunHistorique").append(Vector2(core.memory("gunPosition").x,-core.memory("gunPosition").y)+ core.memory("origine"))

    vel = Vector2(1,1)
    angle =( vel.angle_to(Vector2(0, 1)) + core.memory("gunPosition").z )
    posx = core.memory("gunPosition").x +vel.x
    posy = core.memory("gunPosition").y + vel.y
    core.memory("gunPosition",Vector3(posx,posy,angle))