class Match:
    def __init__(self, player1, player2, score_player1=0, score_player2=0):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2
        self.player1.add_opponent(self.player2.elo)
        self.player2.add_opponent(self.player1.elo)

    def serializer(self):
        data = {
            "player1": self.player1.serializer(),
            "player2": self.player2.serializer(),
            "score_player1": self.score_player1,
            "score_player2": self.score_player2,
            "opponent1": self.player1.add_opponent(self.player2.elo),
            "opponent2": self.player2.add_opponent(self.player1.elo),
        }
        return data
