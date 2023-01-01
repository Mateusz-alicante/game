import pygame

black = 0, 0, 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

from UI.Elements.Button.PauseButton import PauseButton

class BottomBar():

    def __init__(self, game):
        # Load font
        self.smallfont = pygame.font.SysFont('Corbel',35)

        #Load Bottom Bar
        self.woodenBar = pygame.image.load("UI/assets/wood.png").convert_alpha()

        # Initialize pause menu button
        self.pauseButton = PauseButton("Pause", 100 , game.height - 60, 40, (0, 29, 158))
    
    def draw(self, game):

        game.screen.blit(self.woodenBar, (game.width - self.woodenBar.get_width(), game.height - self.woodenBar.get_height() + 70))
        self.scoreText = self.smallfont.render(f'Score: {str(game.score)}' , True , white)
        game.screen.blit(self.scoreText , (game.width - 200, game.height - 50))

        self.pauseButton.draw(game, game.paused)

    def listenForInput(self, game, keys, events, mous_pos):
        self.pauseButton.listenForInput(keys, game, events, mous_pos, lambda : self.togglePause(game))
    
    def togglePause(self, game):
        game.paused = not game.paused


