class Player:
    def __init__(self, last_name, first_name, birthday, sex, elo, score=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.sex = sex
        self.elo = elo
        self.score = score
        self.opponents = []

    def add_opponent(self, elo):
        self.opponents.append(elo)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def serializer(self):
        data = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "sex": self.sex,
            "elo": self.elo,
            "score": self.score,
            "opponents": self.opponents,
        }
        return data

    def serializer_player(self):
        data = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "sex": self.sex,
            "elo": self.elo,
        }
        return data
