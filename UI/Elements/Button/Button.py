import pygame
import math

class Button():

    def __init__(self, text, left, top, size, color):

        # Save position of text for later use
        self.left = left
        self.top = top
        self.size = size
        self.rawText = text
        self.color = color
        self.textChanged = True

        # Load font and render button text
        self.smallfont = pygame.font.SysFont('Corbel', size)
        self.text = self.smallfont.render(text, True, (255, 255, 255))

        # Set size for text
        self.text_width, self.text_height = self.smallfont.size(text)

        # Generate rect for text surface
        self.backgroundRect = pygame.Rect(self.left, self.top, self.text_width + 10, self.text_height + 5)

        self.hover = False

    def draw(self, game):
        pygame.draw.rect(game.screen, self.color, self.backgroundRect)
        game.screen.blit(self.text, (self.textLeft, self.textTop))

    def listenForInput(self, game, keys, events, mous_pos, clickFunc):

        # Listen for hover on this button
        hover = self.backgroundRect.collidepoint(mous_pos)

        if not hover == self.hover or self.textChanged:

            # Adjust variable
            self.hover = hover

            
            # Change button size according to state 
            if hover:

                # Bigger Font
                self.smallfont = pygame.font.SysFont('Corbel', self.size + 10)
                self.text = self.smallfont.render(self.rawText, True, (255, 255, 255))

                self.text_width, self.text_height = self.smallfont.size(self.rawText)

                # Bigger button
                self.backgroundRect = pygame.Rect(self.left - 20, self.top - 5, self.text_width + 20, self.text_height + 10)

                

                # Set position of text
                self.textLeft = self.backgroundRect.left + 10
                self.textTop = self.backgroundRect.top + 10
            
            else:

                # Smaller Font
                self.smallfont = pygame.font.SysFont('Corbel', self.size)
                self.text = self.smallfont.render(self.rawText, True, (255, 255, 255))

                self.text_width, self.text_height = self.smallfont.size(self.rawText)

                # Smaller button
                self.backgroundRect = pygame.Rect(self.left, self.top, self.text_width + 10, self.text_height + 5)

        
                # Set position of text
                self.textLeft = self.backgroundRect.left + 5
                self.textTop = self.backgroundRect.top + 5
            
             

            self.textChanged = False


        # Check for click on this button
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Left click
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if self.backgroundRect.collidepoint(event.pos):
                        # execute function
                        clickFunc()