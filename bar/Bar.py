
import pygame
from Ball import Ball

class Bar():

    def __init__(self, game):

        # Load the bar image, and get the rect
        self.image = pygame.image.load("bar/bar.png")
        self.rect = self.image.get_rect().move((200, 700))

        self.game = game

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, keys, width):

        if self.game.auto:
            x_pos = Ball.Balls[0].rect.centerx
            self.rect.centerx = x_pos

        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect = self.rect.move(-10, 0)
        if keys[pygame.K_RIGHT] and (self.rect.x + self.rect.width) < width:
            self.rect = self.rect.move(10, 0)
