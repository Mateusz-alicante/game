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

from utils.getFrames import loadGIF

from crates.Default.crate import Crate
import pygame

black = 0, 0, 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

class Ball():

    Balls = []
    Frames = None

    def reset():
        Ball.Balls = []

    def setFrames():
        Ball.Frames = loadGIF("ball2.gif", pygame, (100, 100))

    def update(game):
        for ball in Ball.Balls:
            ball.move()
            ball.handleCollisions(game.width, game.height)

            # Finish game if no balls left
            if len(Ball.Balls) == 0:
                if game.score > game.highScore:
                    game.highScore = game.score
                game.finished = True
        
            # for crate in Crate.Crates:
            #         if ball.rect.colliderect(crate.rect) and crate.colide:
            #             crate.hitByBall()
            #             game.score += 1
            #             ball.crateCollision(crate)
                        
            #             if len(Crate.Crates) == 0:
            #                 game.currentSpeedMult += 0.1
            #                 game.score += 10
            #                 setUp(game.currentSpeedMult, game)

    def __init__(self, speed, game):
        self.game = game
        self.image_index = 0
        self.sinceFrameChange = 0
        self.image = Ball.Frames[self.image_index]
        ballrect = self.image.get_rect()
        ballrect = ballrect.move(0, 600)
        self.rect = ballrect
        self.speed = [4 * speed, -4 * speed]
        Ball.Balls.append(self)

    def move(self):
        # adjust texture for animation
        if self.sinceFrameChange > 3:
            self.image_index += 1
            if self.image_index >= len(Ball.Frames):
                self.image_index = 0
            self.image = Ball.Frames[self.image_index]
            self.sinceFrameChange = 0
        else:
            self.sinceFrameChange += 1

        # move ball X
        self.rect = self.rect.move((self.speed[0], 0))

        # Check collsions X
        self.barCollisionX()
        self.crateCollisionX()

        # move ball Y
        self.rect = self.rect.move((0, self.speed[1]))

        # Check collsions Y
        self.barCollisionY()
        self.crateCollisionY()
        
       
    def barCollisionX(self):
        # Collisions with bar
        if self.rect.colliderect(self.game.bar.rect):
            if self.rect.centerx < self.game.bar.rect.centerx:
                overlap = self.rect.right - self.game.bar.rect.left + 5
                self.rect.right -= overlap
                self.speed[0] = -self.speed[0]
            elif self.rect.centerx > self.game.bar.rect.centerx:
                overlap = self.game.bar.rect.right - self.rect.left + 5
                self.rect.right += overlap
                self.speed[0] = -self.speed[0]

    def barCollisionY(self):
        # Collisions with bar
        if self.rect.colliderect(self.game.bar.rect):
            if (self.rect.bottom) > self.game.bar.rect.top:
                overlap = self.rect.bottom - self.game.bar.rect.top
                self.rect.top -= overlap
                self.speed[1] = -self.speed[1]

    def crateCollisionX(self):
        for crate in Crate.Crates:
            if self.rect.colliderect(crate.rect) and crate.colide:
                if self.rect.centerx < crate.rect.centerx:
                    overlap = self.rect.right - crate.rect.left
                    self.rect.right -= overlap
                    self.speed[0] = -self.speed[0]
                elif self.rect.centerx > crate.rect.centerx:
                    overlap = crate.rect.right - self.rect.left
                    self.rect.right += overlap
                    self.speed[0] = -self.speed[0]
                self.crateCollision(crate)

    def crateCollisionY(self):
        for crate in Crate.Crates:
            if self.rect.colliderect(crate.rect) and crate.colide:
                if (self.rect.centery) > crate.rect.centery:
                    overlap = crate.rect.bottom - self.rect.top 
                    self.rect.top += overlap
                    self.speed[1] = -self.speed[1]
                else:
                    overlap = self.rect.top - crate.rect.bottom 
                    self.rect.top -= overlap
                    self.speed[1] = -self.speed[1]
                self.crateCollision(crate)

    def crateCollision(self, crate):
        crate.hitByBall()
    
    def handleCollisions(self, width, height):

        # Remove ball below bar
        if self.rect.bottom > self.game.height - 50:
            Ball.Balls.remove(self)

        # Edge collisions
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
            
        for ball in Ball.Balls:
            if self != ball:
                if self.rect.colliderect(ball.rect):
                    self.speed[0] = -self.speed[0]
                    ball.speed[0] = -ball.speed[0]
        
