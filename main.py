from game.game import Game
from game.gamedata import GameData
from game.scores import Scores
from strategies.strategybaseclass import allStrategies
from report.report import ReportGenerator
from random import randint

def playAllMatches(strategies):
    games = []
    scores = Scores()
    for player1 in strategies:
        for player2 in strategies:
            gamedata = GameData()
            game = Game(numberOfRounds=150 + randint(0, 100),
                        gamedata=gamedata,
                        player1=player1(gamedata),
                        player2=player2(gamedata))
            game.play()

            games.append(game)
            scores.append(nameAndAuthor=game.player1.nameAndAuthor(), score=gamedata.player1Score)
            scores.append(nameAndAuthor=game.player2.nameAndAuthor(), score=gamedata.player2Score)
    return games, scores

strategies = allStrategies()
games, scores = playAllMatches(strategies)
ReportGenerator().createReport(games, scores)