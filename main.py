from enum import Enum

from pygame.rect import Rect

import core




class Etat(Enum):
    MENU = 0,
    JEU = 1,
    GAMEOVER = 2,


def setup():
    print("Start setup")
    core.WINDOW_SIZE = [1200,800]
    core.fps = 60
    core.memory("etat",Etat.MENU)
    print("End setup")

def afficherMenu():
    core.Draw.rect((255,0,0),(500,360,200,80))
    core.Draw.text((255,255,255),"JOUER",(500,360),50)
    core.Draw.text((255,0,0),"press 'p' to play",(525,540),18)

    if core.getKeyPressList("p"):
        core.memory("etat",Etat.JEU)

def afficherJeu():
    core.Draw.rect((255,0,0),(350,280,100,40))
    core.Draw.text((255,255,255),"GAMEOVER",(355,282),30)

    if core.getKeyPressList("x"):
        core.memory("etat",Etat.GAMEOVER)

def afficherGameOver():
    core.Draw.rect((255,0,0),(350,280,100,40))
    core.Draw.text((255,255,255),"MENU",(355,282),30)

    if core.getKeyPressList("c"):
        core.memory("etat",Etat.MENU)

def run():
        core.cleanScreen()

        if core.memory('etat') == Etat.MENU:
            afficherMenu()
        if core.memory('etat') == Etat.JEU:
            afficherJeu()
        if core.memory('etat') == Etat.GAMEOVER:
            afficherGameOver()

core.main(setup,run)