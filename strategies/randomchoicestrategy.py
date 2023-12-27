from strategies.strategybaseclass import Strategy
from game.choices import cooperative, hostile
import random

class RandomStrategy(Strategy):
    def __init__(self, gamedata):
        self.gamedata = gamedata

    def name(self):
        return 'Random strategy'

    def author(self):
        return 'Isti'

    def nextChoice(self):
        return cooperative if random.random() > 0.5 else hostile
