from strategies.strategybaseclass import Strategy
from game.choices import cooperative, hostile
from random import random

class EyeForEyeStrategy(Strategy):
    def name(self):
        return 'Eye for eye, but provocative'

    def author(self):
        return 'Isti'

    def nextChoice(self):
        opponentsChoices = self.getOpponentsPreviousChoices()
        if len(opponentsChoices) == 0 or opponentsChoices[-1] == cooperative:
            return hostile if random() > 0.85 else cooperative
        return hostile
