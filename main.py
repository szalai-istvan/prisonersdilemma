from game.game import Game
from game.gamedata import GameData
from strategies.strategybaseclass import allStrategies

games = []

def playAllMatches(strategies):
    for player1 in strategies:
        for player2 in strategies:
            gamedata = GameData()
            game = Game(200,
                        gamedata,
                        player1(gamedata),
                        player2(gamedata))
            game.play()
            games.append(game)

strategies = allStrategies()
playAllMatches(strategies)
