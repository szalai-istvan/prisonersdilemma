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
        return f'{self.nameAndAuthor()} as player {self.player}'

    def nameAndAuthor(self):
        return f'{self.name()} (by {self.author()})'

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


