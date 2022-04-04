from tinydb import TinyDB, Query


class Tournament:
    def __init__(self, name, place, date, controller_temp, description, number_tour=4):
        self.name = name
        self.place = place
        self.players = []
        self.rounds = []
        self.date = date
        self.controller_temp = controller_temp
        self.description = description
        self.number_tour = number_tour

    def print_info(self):
        print(self.name, self.place, self.date)
        for player in self.players:
            print(player.first_name, player.elo)

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)

    def serializer(self):

        data = {
            "name": self.name,
            "place": self.place,
            "players": [player.serializer() for player in self.players],
            "rounds": [round.serializer() for round in self.rounds],
            "date": self.date,
            "controller_temp": self.controller_temp,
            "description": self.description,
            "number_tour": self.number_tour,
        }
        return data

    def save(self):
        db = TinyDB("db.json", indent=4)
        table_tournament = db.table("Tournaments")
        table_tournament.insert(self.serializer())
        return table_tournament.all()

    def save_player(self, player):
        db = TinyDB("db.json", indent=4)
        table_tournament = db.table("Players")
        table_tournament.insert(player.serializer_player())

    def update(self, name):
        db = TinyDB("db.json", indent=4)
        tournaments = db.table("Tournaments")
        Tournament = Query()
        tournaments.update(
            {"rounds": [round.serializer() for round in self.rounds]},
            Tournament.name == name,
        )

    @staticmethod
    def get_ongoing_tournament():
        db = TinyDB("db.json", indent=4)
        tournaments = db.table("Tournaments")
        tournaments_ongoing = []
        for tournament in tournaments:
            if len(tournament["rounds"]) < 4:
                tournaments_ongoing.append(tournament["name"])
        return tournaments_ongoing

    @staticmethod
    def get_saved_tournament(name):
        db = TinyDB("db.json", indent=4)
        tournaments = db.table("Tournaments")
        Tournament = Query()
        tournament = tournaments.search(Tournament.name == name)
        return tournament[0]

    @staticmethod
    def get_ongoing_players(players):
        db = TinyDB("db.json", indent=4)
        players = db.table("Players")
        players_ongoing = []
        for player in players:
            players_ongoing.append(player)
        return players_ongoing

    @classmethod
    def get_list_tournaments(Tounament):
        db = TinyDB("db.json", indent=4)
        tournaments = db.table("Tournaments")
        tournaments_list = []
        for tournament in tournaments:
            tournaments_list.append(tournament["name"])
        return tournaments_list, tournament
