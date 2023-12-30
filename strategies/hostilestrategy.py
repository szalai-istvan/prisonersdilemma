from strategies.strategybaseclass import Strategy
from game.choices import hostile

class HostileStrategy(Strategy):
    def name(self):
        return 'Hostile strategy'

    def author(self):
        return 'Isti'

    def nextChoice(self):
        return hostile
