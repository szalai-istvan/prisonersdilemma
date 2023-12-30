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
            # numberOfRounds = 150 + randint(0, 100)
            numberOfRounds = 250
            game = Game(numberOfRounds=numberOfRounds,
                        gamedata=gamedata,
                        player1=player1(gamedata),
                        player2=player2(gamedata))

            game.play()
            games.append(game)
            correctionFactor = 250 / numberOfRounds
            scores.append([
                (game.player1.nameAndAuthor(), gamedata.player1Score * correctionFactor),
                (game.player2.nameAndAuthor(), gamedata.player2Score * correctionFactor)
            ])
    return games, scores

strategies = allStrategies()
games, scores = playAllMatches(strategies)
ReportGenerator().createReport(games, scores)