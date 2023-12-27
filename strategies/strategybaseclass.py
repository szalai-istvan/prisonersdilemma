def allStrategies():
    return Strategy.__subclasses__()

class Strategy:
    def __init__(self, gamedata):
        self.gamedata = gamedata
        self.player = 0

    def playAsPlayer(self, player):
        self.player = player
        return self

    def description(self):
        return f'{self.name()} as player {self.player}'

    def name(self):
        raise Exception('Name unspecified')

    def author(self):
        raise Exception('Author unspecified')

    def nextChoice(self):
        raise Exception('Strategy is not implemented')

    def getPreviousChoices(self):
        return self.gamedata.getChoices(self.player)

    def getOpponentsPreviousChoices(self):
        return self.gamedata.getChoices(3 - self.player)


