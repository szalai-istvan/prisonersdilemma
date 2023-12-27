from game.game import Game
from game.gamedata import GameData
from game.scores import Scores
from strategies.strategybaseclass import allStrategies

def playAllMatches(strategies):
    games = []
    scores = Scores()
    for player1 in strategies:
        for player2 in strategies:
            gamedata = GameData()
            game = Game(200,
                        gamedata,
                        player1(gamedata),
                        player2(gamedata))
            game.play()

            games.append(game)
            scores.append(nameAndAuthor=game.player1.nameAndAuthor(), score=gamedata.player1Score)
            scores.append(nameAndAuthor=game.player2.nameAndAuthor(), score=gamedata.player2Score)
    return games, scores

strategies = allStrategies()
games, scores = playAllMatches(strategies)

