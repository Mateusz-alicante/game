from utils.getFrames import loadGIF
import pygame


class Background():

    def __init__(self):
        self.frames = loadGIF("utils/Background/beach.gif", pygame)
        self.frame = 0
        self.sinceFrameChange = 0
        self.image = self.frames[self.frame]

    def draw(self, game):

        # Draw to screen
        game.screen.blit(self.image, (0,0))


        # adjust texture for animation
        if self.sinceFrameChange > 3:
            self.frame += 1
            if self.frame >= len(self.frames):
                self.frame = 0
            self.image = self.frames[self.frame]
            self.sinceFrameChange = 0
        else:
            self.sinceFrameChange += 1