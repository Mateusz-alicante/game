import pygame

black = 0, 0, 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

class FinishScreen():

    def __init__(self):
        # Load font
        self.smallfont = pygame.font.SysFont('Corbel',35)

    
    def draw(self, game):
        
         # Restart Text
        textRestart = self.smallfont.render('To restart the game press Return' , True , blue)
        game.screen.blit(textRestart , (game.width/2 - textRestart.get_width() / 2, game.height/2))

        #Current Score Text
        textCurrentScore = self.smallfont.render('You finished with a socre of ' + str(game.score) , True , white)
        game.screen.blit(textCurrentScore , (game.width/2 - textCurrentScore.get_width() / 2,game.height/2 + 50))

        # High Score Text
        textHighScore = self.smallfont.render('Your high score in this session is ' + str(game.highScore) , True , black)
        game.screen.blit(textHighScore , (game.width/2 - textHighScore.get_width() / 2, game.height/2 + 100)) 

