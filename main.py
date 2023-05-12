from enum import Enum

from pygame import Vector3, Vector2, Rect

import core
from asteroid import asteroids
from player import drawGun, moveGun


class Etat(Enum):
    MENU = 0,
    JEU = 1,
    GAMEOVER = 2,


def setup():
    print("Start setup")
    core.WINDOW_SIZE = [1200,800]
    core.fps = 60
    core.memory("etat",Etat.MENU)

    core.memory("gunPosition", Vector3(0, 0,0))
    core.memory("origine",Vector2(600,400))
    core.memory("gunHistorique", [])

    print("End setup")

def afficherMenu():
    core.Draw.rect((255,0,0),(490,360,220,80))
    core.Draw.text((0,0,0),"J O U E R",(520,370),50,font=("Impact", "bold"))
    core.Draw.text((255,0,0),"CLIQUER SUR LE BOUTON 'JOUER'",(495,443),15)
    core.Draw.text((255,0,0),"OU",(585,458),15)
    core.Draw.text((255, 0, 0), "APPUYER SUR 'J' POUR JOUER", (505, 473), 15)

    if core.getMouseLeftClick():
        position = core.getMouseLeftClick()
        rec = Rect(490,360,220,80)
        if rec.collidepoint(position):
            core.memory("etat",Etat.JEU)
    if core.getKeyPressList("p"):
        core.memory("etat",Etat.JEU)


def afficherJeu():
    core.Draw.rect((255,0,0),(5,5,200,30))
    core.Draw.text((0,0,0),"S C O R E : .......",(7,2),30)


    if core.getKeyPressList("x"):
        core.memory("etat",Etat.GAMEOVER)

def afficherGameOver():
    core.Draw.rect((255,0,0),(490,360,220,80))
    core.Draw.text((0,0,0),"G A M E  O V E R",(508,373),50,font=("Impact", 20, "bold"))
    core.Draw.text((255,0,0),"P R E S S  ' R '  T O  R E S T A R T",(482,450),20)

    if core.getKeyPressList("c"):
        core.memory("etat",Etat.MENU)



def run():
        core.cleanScreen()

        if core.memory('etat') == Etat.MENU:
            afficherMenu()
        if core.memory('etat') == Etat.JEU:
            afficherJeu()
            drawGun()
            moveGun()
            core.printMemory()
            asteroids()
        if core.memory('etat') == Etat.GAMEOVER:
            afficherGameOver()

core.main(setup,run)