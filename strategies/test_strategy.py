from strategies.strategybaseclass import Strategy
from game.choices import cooperative, hostile
import random

class RandomStrategy(Strategy):
    def __init__(self, gamedata):
        self.gamedata = gamedata

    def name(self):
        return 'Test strategy'

    def author(self):
        return 'Oli'

    def nextChoice(self):
        # This model assumes that the individual thrives for better scores,
        # based on the a priori knowledge
        # Parameters
        # ----------
        # Memory: Number of old generations to cache
        # Bias: Ideological bias from the old (non-cached) generations
        # Mood: Initial decision bias
        # Patience: Number of receiving low scores in a row, without losing interest and quiting


        individualMemory = 10
        individualBias = cooperative
        individualMood = cooperative
        individualPatience = 5

        # Initial choice is based on the mood

        # The choice is based on two components
        # 1, the cached subsequent choices of the opponent
        # 2, the bias of the individual
        # if the bias and the cache is of a different decision, then the recent mood decides
        # if there is not enough games for creating a bias, then ? TODO


        # TODO
        individualDecision = cooperative

        return individualDecision
