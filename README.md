# Prisoner's dilemma

This project's idea came after watching Veritasium's video on the topic: https://youtu.be/mScpHTIi-kM?si=MrPZC6TQCur8EtfO

In The Prisoner's dilemma two players are competing in a number of rounds. Each round, each player chooses between being cooperative or hostile without knowing the other player's choice, and then they get some points. The scoring goes as follows:
- cooperative-cooperative: 3-3 points
- hostile-hostile: 1-1 points
- cooperative-hostile: 0-5 points
- hostile-cooperative: 5-0 points

In 1980 Robert Axelrod conducted an experiment where game theorists submitted programs playing the game with different strategies. At that experiment they concluded that an eye-for-eye approach works best, at which we start as cooperative, and every round we mimic the last choice of our opponent. We only act hostile, if we have been treated hostile in the previous round. 
What I would like to figure out is whether we can come up with an approach beating eye-for-eye. 
The Python program in this repository when executed will contest every strategy against every strategy (including itself) twice and export the results into a .csv file. The ranking is based on a strategy's average score among all its games. The .csv also contains the details of all games played. 

When making a decision a strategy has access to all its and all its opponent's previous choices. From the length of the choice arrays the current round's number can be deducted, but the total number of rounds is unknown to the player. Every game's length is random between 150 and 250. 

To submit a new strategy, create a new .py file in the ./strategies directory, and create a class which extends strategies.strategybaseclass.Strategy. Below is a template that can be used for creating new strategy classes. 
Two strategies have already been added. One that chooses randomly every time, to serve as an origin. We expect a well made strategy to perform better than the random selector. The other is the 1980 winner eye-for-eye strategy, so we can compare our ones to it. 

```
from strategies.strategybaseclass import Strategy
from game.choices import cooperative, hostile

class name_of_your_class(Strategy):
    def name(self):
        return the name you have given toyour strategy.

    def author(self):
        return your name or nickname.

    def nextChoice(self):
        opponentsChoices = self.getOpponentsPreviousChoices()
        myChoices = self.getPreviousChoices()
        Your implementation of your strategy here
        in the end you need to return game.choices.cooperative, or game.choices.hostile. If you copy-paste the imports, you only need to type cooperative or hostile. 
```
