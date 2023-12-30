from strategies.strategybaseclass import Strategy
from game.choices import cooperative, hostile
from random import random

class BarksButNotBites(Strategy):
    def name(self):
        return 'Barks but not bites'

    def author(self):
        return 'Isti'

    def nextChoice(self):
        choices = self.getPreviousChoices()
        opponentsChoices = self.getOpponentsPreviousChoices()
        if len(choices) == 0:
            return cooperative

        lastChoice = choices[-1]
        opponentsLastChoice = opponentsChoices[-1]
        peeaceCounter = self.calculatePeaceCounter()
        if peeaceCounter >= 3:
            return hostile
        if lastChoice == hostile and opponentsLastChoice == cooperative:
            return hostile
        if opponentsLastChoice == hostile and lastChoice == cooperative:
            return hostile
        return cooperative

    def calculatePeaceCounter(self):
        choices = self.getPreviousChoices()
        opponentsChoices = self.getOpponentsPreviousChoices()

        index = len(choices) - 1
        while choices[index] == cooperative and opponentsChoices[index] == cooperative and index >= 0:
            index -= 1
        return len(choices) - (index + 1)
