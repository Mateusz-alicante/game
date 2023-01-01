from random import random

WHITE=(255,255,255)
BLUE=(0,0,255)

from crates.Default.crate import Crate
from crates.AddBall.crate import AddBallCrate
from crates.Bomb.crate import BombCrate

from Ball import Ball
from bar.Bar import Bar

# Set up game
def setUp(speed, game):

    Ball.reset()
    Ball(speed, game)

    Crate.reset()

    # Init the bar
    game.bar = Bar(game)

    # Create crates
    for row in range(3):
        for col in range(10):
            ranNum = random()
            if ranNum < 0.01:
                AddBallCrate(row, col, game)
            elif ranNum < 0.1:
                BombCrate(row, col, game)
            else:
                Crate(row, col, game)

    # Start game if it was finished
    game.finished = False
