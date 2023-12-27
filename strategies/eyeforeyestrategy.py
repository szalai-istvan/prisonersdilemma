from strategies.strategybaseclass import Strategy
from game.choices import cooperative

class EyeForEyeStrategy(Strategy):
    def name(self):
        return 'Eye for eye strategy'

    def author(self):
        return 'Isti'

    def nextChoice(self): # We are cooperative, unless our opponent was hostile last round
        opponentsChoices = self.getOpponentsPreviousChoices()
        if len(opponentsChoices) == 0:
            return cooperative
        return opponentsChoices[-1]
