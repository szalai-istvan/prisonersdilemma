import uuid
import csv
from datetime import datetime
from game.game import Game
from game.scores import Scores
import os

class ReportGenerator:
    def __init__(self):
        if not os.path.exists('./reports'):
            os.mkdir('./reports')

    def createFilename(self):
        now = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        return 'reports/' + now + '-' + str(uuid.uuid4()) + '.csv'

    def createReport(self, games: list[Game], scores: Scores):
        filename = self.createFilename()
        with open(filename, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Description of strategy', 'Average score'])
            scores = scores.csvData()
            for score in scores:
                writer.writerow(score)

            writer.writerows([[''], ['']])
            for game in games:
                firstrow,secondrow = game.csvdata()
                writer.writerow(['Description of strategy', 'Final score', 'Choices'])
                writer.writerow(firstrow)
                writer.writerow(secondrow)
                writer.writerow([''])