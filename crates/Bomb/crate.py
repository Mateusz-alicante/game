import json

import pygame

from crates.Default.crate import Crate
from utils.SpriteSheet import SpriteSheet

class BombCrate(Crate):

    AnimationFrames = []

    def setFrames():
        spritesheetURL = "crates/Bomb/spritesheet.png"
        spriteSheet = SpriteSheet(spritesheetURL)
        with open('crates/Bomb/spritesheet.json') as f:
            meta = json.load(f)
        for i in range(33):
            spriteMeta = meta["frames"][f"1_{str(i)}.png"]['frame']
            image = spriteSheet.image_at((spriteMeta["x"], spriteMeta["y"], spriteMeta["w"], spriteMeta["h"]), -1)
            BombCrate.AnimationFrames.append(pygame.transform.scale(image, (350, 350)))

    def __init__(self, row, num, game):
        super(BombCrate, self).__init__(row, num, game, "crates/images/Bomb.png")
        self.exploding = False
        self.explosionRect = None
    
    def hitByBall(self):
        self.exploding = True
        self.colide = False

        self.game.shake = 25

        # Position explosion on screen
        self.currentExplosionFrame = -1
        self.explsionImage = BombCrate.AnimationFrames[self.currentExplosionFrame]
        self.explsionRect = self.explsionImage.get_rect()
        self.explsionRect = self.explsionRect.move(self.rect.left - 120, self.rect.top - 180)

        for crate in Crate.Crates[:]:
            if crate.colide and abs(self.row - crate.row) <= 1 and abs(self.col - crate.col) <= 1:
                crate.hitByBall()

    def draw(self, screen):
        if not self.exploding:
            super().draw(screen)
        elif self.currentExplosionFrame + 1 < len(BombCrate.AnimationFrames):

            self.currentExplosionFrame += 1
            self.explsionImage = BombCrate.AnimationFrames[self.currentExplosionFrame]

            screen.blit(self.explsionImage, self.explsionRect)
        else:
            super().hitByBall()





        
        