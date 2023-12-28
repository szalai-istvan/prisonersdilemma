from game.choices import hostile, cooperative, validateChoice

class GameData:
    def __init__(self):
        self.player1Choices = []
        self.player2Choices = []

        self.player1Score = 0
        self.player2Score = 0

    def addPlayer1Choice(self, choice):
        validateChoice(choice)
        self.player1Choices.append(choice)

    def addPlayer2Choice(self, choice):
        validateChoice(choice)
        self.player2Choices.append(choice)

    def getChoices(self, player):
        if player == 1:
            return [x for x in self.player1Choices]
        elif player == 2:
            return [x for x in self.player2Choices]
        raise Exception(f'Unexpected player number: {player}. ')

    def evaluateRound(self):
        player1 = self.player1Choices[-1]
        player2 = self.player2Choices[-1]

        if player1 == hostile and player2 == hostile:
            self.player1Score += 1
            self.player2Score += 1
            return
        if player1 == cooperative and player2 == hostile:
            self.player2Score += 5
            return
        if player1 == hostile and player2 == cooperative:
            self.player1Score += 5
            return
        if player1 == cooperative and player2 == cooperative:
            self.player1Score += 3
            self.player2Score += 3

    def declareWinner(self):
        if self.player1Score > self.player2Score:
            return 1
        if self.player2Score > self.player1Score:
            return 2
        return 0



