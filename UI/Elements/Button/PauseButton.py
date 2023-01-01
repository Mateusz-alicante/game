from UI.Elements.Button.Button import Button
import pygame

class PauseButton(Button):

    def draw(self, game, paused):
        super().draw(game)
        newText = "Resume" if paused else "Pause"
        if not self.rawText == newText:

            # Set new text
            self.rawText = newText
            self.text = self.smallfont.render(newText, True, (255, 255, 255))
            self.text_width, self.text_height = self.smallfont.size(newText)
            self.textChanged = True

            # Adjust size of box
