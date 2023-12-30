class Scores:
    def __init__(self):
        self.scores = {}
        self.numberOfWins = {}

    def append(self, results):
        self.registerScores(results)
        self.registerWinner(results)

    def registerScores(self, results):
        for result in results:
            nameAndAuthor = result[0]
            score = result[1]
            if nameAndAuthor in self.scores:
                self.scores[nameAndAuthor].append(score)
            else:
                self.scores[nameAndAuthor] = [score]

    def registerWinner(self, results):
        player1NameAndAuthor = results[0][0]
        player1Score = results[0][1]
        player2NameAndAuthor = results[1][0]
        player2Score = results[1][1]

        if player1Score > player2Score:
            winner = player1NameAndAuthor
        elif player2Score > player1Score:
            winner = player2NameAndAuthor
        else:
            return

        if winner not in self.numberOfWins:
            self.numberOfWins[winner] = 1
        else:
            self.numberOfWins[winner] = self.numberOfWins[winner] + 1

    def calculateAverageScores(self):
        averaged = {}
        for key in self.scores.keys():
            values = self.scores[key]
            averaged[key] = sum(values) / len(values)
        return averaged

    def csvData(self):
        averageScores = self.calculateAverageScores()
        sortedByValue = sorted(averageScores.items(), key=lambda x: x[1])[::-1]
        rows = []
        for value in sortedByValue:
            rows.append([value[0], value[1], self.numberOfWins[value[0]] if value[0] in self.numberOfWins else 0])
        return rows