from models.tournament import Tournament
from views.tournament_view import (
    get_user_input,
    print_message,
    print_classement,
    print_on_going_tournament,
)
from models.player import Player
from controllers.utils import is_date, is_sexe, is_time
from models.round import Round
from models.match import Match
from views.matchs_view import score_match
import datetime


class TournamentController:
    def __init__(self):
        self.tournament = None

    def run_new_tournament(self):
        name = self.get_and_check_user_text_input(
            "Entrez le nom du tournoi : ")
        place = self.get_and_check_user_text_input(
            "Entrez le lieu du tournoi : ")
        date_string = self.get_and_check_date_input("Entrer la date: ")
        controller_temp = self.get_and_check_controller_temp(
            "Entrer le type de tournois: ")
        description = self.get_and_check_user_text_input(
            "Entrer description : ")
        self.tournament = Tournament(
            name, place, date_string, controller_temp, description
        )
        for i in range(8):
            print_message(f"------------------------------------")
            print_message(f"Entrez information du joueur {i+1} :")
            last_name = self.get_and_check_user_text_input(
                "Entrez le nom de famille du joueur : ")
            first_name = self.get_and_check_user_text_input(
                "Entrer le prenom du joueur: ")
            birthday = self.get_and_check_date_input(
                "Entrer date de naissance du joueur : ")
            sex = self.get_and_check_sex_input("Entrer le sexe du joueur: ")
            elo = self.get_and_check_elo_input("Entrez elo du joueur : ")
            player = Player(last_name, first_name, birthday, sex, elo)
            self.tournament.add_player(player)
            self.tournament.save_player(player)

        self.run_first_round()
        if self.is_stop_and_save_tournament("voulez vous areter le tournoi ? : "):
            return
        for i in range(2, 5):
            self.run_other_round(i)
            if self.is_stop_and_save_tournament("voulez vous areter le tournoi ? : "):
                return
        print_classement(self.tournament.players)
        self.tournament.save()

    def is_stop_and_save_tournament(self, message):
        user_input = self.get_and_check_save_tournament(message)
        user_input = user_input.lower()
        if user_input == "oui":
            self.tournament.save()
            return True
        return False

    def is_stop_and_update_tournament(self, message, name):
        user_input = self.get_and_check_save_tournament(message)
        user_input = user_input.lower()
        if user_input == "oui":
            self.tournament.update(name)
            return True
        return False

    def get_and_check_save_tournament(self, message):
        user_input = get_user_input(message)
        while user_input not in ["oui", "non"]:
            user_input = get_user_input(f"ERROR: {message}")
        return user_input

    def run_reload_tournament(self):
        name = self.get_tournament_to_reload()
        tournament = Tournament.get_saved_tournament(name)
        self.deserializer(tournament)
        round_to_run = 4 - len(tournament["rounds"])
        if round_to_run == 4 or round_to_run == 0:
            self.run_first_round()
            if self.is_stop_and_update_tournament(
                "voulez vous areter le tournoi ? : ", name
            ):
                return
        else:
            for i in range(round_to_run):
                self.run_other_round(4 - (round_to_run - i) + 1)
                if self.is_stop_and_update_tournament(
                    "voulez vous areter le tournoi ? : ", name
                ):
                    return

        self.tournament.update(name)
        print_classement(self.tournament.players)
        self.tournament.update(name)

    def deserializer(self, tournament):
        self.tournament = Tournament(
            tournament["name"],
            tournament["place"],
            tournament["date"],
            tournament["controller_temp"],
            tournament["description"],
            tournament["number_tour"],
        )
        for player in tournament["players"]:
            player_to_add = Player(
                player["last_name"],
                player["first_name"],
                player["birthday"],
                player["sex"],
                player["elo"],
                player["score"],
            )
            self.tournament.add_player(player_to_add)

        for round in tournament["rounds"]:
            reload_round = Round(
                round["number"], round["start_time"], round["end_time"]
            )
            for match in round["matchs"]:
                player1 = Player(
                    match["player1"]["last_name"],
                    match["player1"]["first_name"],
                    match["player1"]["birthday"],
                    match["player1"]["sex"],
                    match["player1"]["elo"],
                    match["player1"]["score"],
                )
                player2 = Player(
                    match["player2"]["last_name"],
                    match["player2"]["first_name"],
                    match["player2"]["birthday"],
                    match["player2"]["sex"],
                    match["player2"]["elo"],
                    match["player2"]["score"],
                )

                reload_match = Match(
                    player1, player2, match["score_player1"], match["score_player2"]
                )

                reload_round.add_match(reload_match)

            self.tournament.add_round(reload_round)

    def get_tournament_to_reload(self):
        message = "Quel tournoi souhaitez vous reprendre ?"
        on_going_tournament = Tournament.get_ongoing_tournament()
        print_on_going_tournament(on_going_tournament)
        user_input = get_user_input(message).capitalize()
        while user_input not in on_going_tournament:
            user_input = get_user_input(f"Error : {message}").capitalize()
        return user_input

    def get_and_check_user_text_input(self, message):
        user_input = get_user_input(message).capitalize()
        while not user_input.isalpha():
            user_input = get_user_input(f"Error : {message}")
        return user_input

    def get_and_check_elo_input(self, message):
        elo_input = get_user_input(message)
        while not elo_input.isnumeric():
            elo_input = get_user_input(f"Error : {message}")
        return int(elo_input)

    def get_and_check_date_input(self, message):

        date_input = get_user_input(message)
        while not is_date(date_input):
            date_input = get_user_input(f"Error : {message}")
        return date_input

    def get_and_check_controller_temp(self, message):
        controller_temp_input = get_user_input(message)
        controller_temp_input = controller_temp_input.lower()
        if (
            controller_temp_input == "bullet"
            or controller_temp_input == "blitz"
            or controller_temp_input == "coup rapide"
        ):
            return True
        else:
            controller_temp_input = get_user_input(f"Error : {message}")
        return controller_temp_input

    def get_and_check_sex_input(self, message):
        sex_input = get_user_input(message)
        while not is_sexe(sex_input):
            sex_input = get_user_input(f"Error : {message}")
        return sex_input

    def print_tournament_infos(self):
        self.tournament.print_info()

    def get_and_check_time_input(self, message):
        time_input = get_user_input(message)
        while not is_time(time_input):
            time_input = get_user_input(f"Error : {message}")
        return time_input

    def get_and_check_score_match(self, match):
        user_input = score_match(match)
        while user_input not in ["1", "2", "3"]:
            user_input = score_match(match)
        return user_input

    def save_score(self, match, user_input):
        if user_input == "1":
            match.score_player1 = 1
            match.player1.score += 1
        elif user_input == "2":
            match.score_player2 = 1
            match.player2.score += 1
        else:
            match.score_player1 = 0.5
            match.player1.score += 0.5
            match.score_player2 = 0.5
            match.player2.score += 0.5

    def run_first_round(self):
        number = "Round 1"
        round = Round(number)
        print_message(number)
        round.star_time = datetime.datetime.now()
        self.tournament.add_round(round)
        list_player = self.tournament.players
        list_player.sort(key=lambda x: x.elo)
        for superior, inferior in zip(list_player[:4], list_player[4:]):
            match = Match(superior, inferior)
            round.add_match(match)

        for match in round.matchs:
            user_input = self.get_and_check_score_match(match)
            self.save_score(match, user_input)
        round.end_time = datetime.datetime.now()

    def run_other_round(self, number):
        number = f"Round {number}"
        round = Round(number)
        print_message("\n\n")
        print_message(number)
        round.star_time = datetime.datetime.now()
        self.tournament.add_round(round)
        self.tournament.players.sort(key=lambda x: x.elo)
        self.tournament.players.sort(key=lambda x: x.score, reverse=True)

        for i in range(0, 8, 2):
            match = Match(self.tournament.players[i], self.tournament.players[i + 1])
            round.add_match(match)

        for match in round.matchs:
            user_input = self.get_and_check_score_match(match)
            self.save_score(match, user_input)
        round.end_time = datetime.datetime.now()
