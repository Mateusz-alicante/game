#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      m.kazimierczak
#
# Created:     14/04/2021
# Copyright:   (c) m.kazimierczak 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame

class Crate():

    Crates = []
    UsedCoors = set()

    def drawCrates(screen):
        for crate in Crate.Crates:
            crate.draw(screen)

    def reset():
        Crate.Crates = []
        Crate.UsedCoors = set()


    def __init__(self, row, col, game, texturePath = "crates/images/Default.png"):

        # Detect if there already is a crate in the same column or row
        if (row, col) in Crate.UsedCoors:
            print(f"prevented a crate on creating on {str((row, col))}")
            return

        # Load texture from image
        self.image = pygame.image.load(texturePath)
        self.image = pygame.transform.scale(self.image, (100, 100))

        # Position crate on screen
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(110 * col + 50, 10 + row * 110)

        # store the row and column of this crate
        self.row = row
        self.col = col

        # Store the game instance
        self.game = game

        self.colide = True

        # Default core increase if destroyed
        self.scoreOnDestroy = 1

        Crate.Crates.append(self)

        Crate.UsedCoors.add((row, col))


    def hitByBall(self):

        if self in Crate.Crates:
            self.game.score += self.scoreOnDestroy
            Crate.Crates.remove(self)

        if len(Crate.Crates) == 0:
            self.game.currentSpeedMult += 0.1
            self.game.score += 10
            self.game.startNewLevel = True


    def draw(self, screen):
        screen.blit(self.image, self.rect)