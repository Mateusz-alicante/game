import pygame

black = 0, 0, 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

from UI.Components.BottomBar.BottomBar import BottomBar
from UI.Components.FinishScreen.FinishScreen import FinishScreen

class UI():

    def __init__(self, game):
        self.bottomBar = BottomBar(game)
        self.finishScreen = FinishScreen()

    def draw(self, game):

        if not game.finished:
            self.bottomBar.draw(game)
        else:
            self.finishScreen.draw(game)
           

    def listenForInput(self, game, keys, events, mous_pos):
        self.bottomBar.listenForInput(keys, game, events, mous_pos)
