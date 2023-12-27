class Scores:
    def __init__(self):
        self.scores = {}

    def append(self, nameAndAuthor, score):
        if nameAndAuthor in self.scores:
            self.scores[nameAndAuthor].append(score)
        else:
            self.scores[nameAndAuthor] = [score]

    def calculateAverageScores(self):
        averaged = {}
        for key in self.scores.keys():
            values = self.scores[key]
            averaged[key] = sum(values) / len(values)
        return averaged

    def csvData(self):
        averageScores = self.calculateAverageScores()
        sortedByValue = sorted(averageScores, key=lambda x: x[1])[::-1]
        rows = []
        for value in sortedByValue:
            rows.append([value[0], value[1]])
        return rows