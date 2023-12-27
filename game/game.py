from strategies.strategybaseclass import Strategy
from game.gamedata import GameData

class Game:
    def __init__(self, numberOfRounds: int, gamedata: GameData, player1: Strategy, player2: Strategy):
        self.gamedata = gamedata
        self.numberOfRounds = numberOfRounds
        self.player1 = player1
        self.player2 = player2
        self.winner: Strategy = None

    def play(self):
        player1 = self.player1.playAsPlayer(1)
        player2 = self.player2.playAsPlayer(2)
        gamedata = self.gamedata
        for _ in range(self.numberOfRounds):
            p1Choice = player1.nextChoice()
            p2Choice = player2.nextChoice()
            gamedata.addPlayer1Choice(p1Choice)
            gamedata.addPlayer2Choice(p2Choice)
            gamedata.evaluateRound()

        winner = gamedata.declareWinner()
        if winner == 1:
            self.winner = player1
        elif winner == 2:
            self.winner = player2
        else:
            print('Draw')

    def getWinner(self):
        return self.winner

    def csvdata(self):
        firstrow = [self.player1.description()]
        secondrow = [self.player2.description()]
        [firstrow.append(choice) for choice in self.gamedata.getChoices(1)]
        [secondrow.append(choice) for choice in self.gamedata.getChoices(2)]
        firstrow.append(self.gamedata.player1Score)
        secondrow.append(self.gamedata.player2Score)
        return firstrow,secondrow