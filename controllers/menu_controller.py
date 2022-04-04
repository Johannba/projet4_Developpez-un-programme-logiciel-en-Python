from controllers.tournament_controller import TournamentController
from views.menu_view import print_menu_home
from views.report_view import (
    print_menu_report,
    print_report_players_and_elo,
    print_tournament_name,
    print_tournaments_menu,
    print_tournament_players,
    print_tournament_rounds,
    print_tournament_matchs,
)
from models.tournament import Tournament
from views.tournament_view import get_user_input


class MenuController:
    def __init__(self):
        self.controller = TournamentController()

    def run(self):
        self.menu_home()
        # self.tournament.get_list_tournaments()
        # self.controller.run_reload_tournament()
        # self.controller.run_reload_tournament()

    def menu_home(self):
        while True:
            menu = print_menu_home()
            chosen_option = self.get_and_check_menu_home(menu)
            if chosen_option == "1":
                self.controller.run_new_tournament()
            elif chosen_option == "2":
                self.controller.run_reload_tournament()
            elif chosen_option == "3":
                self.menu_report(menu)
            else:
                exit()

    def get_and_check_menu_home(self, message):
        user_input = input("Tapez ici :")
        while user_input not in ["1", "2", "3", "4"]:
            user_input = input(f"Error : {message}")
        return user_input

    def menu_report(self, players):
        menu_report = print_menu_report()
        chosen_option = self.get_and_check_menu_report(menu_report)
        if chosen_option == "1":
            self.get_alphabetic_actors(players)
        elif chosen_option == "2":
            self.get_try_elo(players)
        elif chosen_option == "3":
            self.list_tournaments_name()
        else:
            exit()

    def get_and_check_menu_report(self, message):
        user_input = input("Tapez ici :")
        while user_input not in ["1", "2", "3"]:
            user_input = input(f"Error : {message}")
        return user_input

    def get_alphabetic_actors(self, players):
        alphabetic_actors = Tournament.get_ongoing_players(players)
        alphabetic_actors.sort(key=lambda x: x["last_name"])
        print_report_players_and_elo(alphabetic_actors)

    def get_try_elo(self, players):
        try_elo = Tournament.get_ongoing_players(players)
        try_elo.sort(key=lambda x: x["elo"])
        print_report_players_and_elo(try_elo)

    def list_tournaments_name(self):
        message = "Quel tournoi souhaitez vous avoir des infos ?"
        list_name = Tournament.get_list_tournaments()[0]
        print_tournament_name(list_name)
        user_input = get_user_input(message).capitalize()
        while user_input not in list_name:
            user_input = get_user_input(f"Error : {message}").capitalize()
        return self.menu_tournaments()

    def menu_tournaments(self):
        menu_tournament = print_tournaments_menu()
        chosen_option = self.get_and_check_menu_tournaments(menu_tournament)
        if chosen_option == "1":
            self.tournament_players()
        elif chosen_option == "2":
            self.tournament_players_elos()
        elif chosen_option == "3":
            self.list_round_tournament()
        elif chosen_option == "4":
            self.list_matchs_tournament()
        else:
            exit()

    def get_and_check_menu_tournaments(self, message):
        user_input = input("Tapez ici :")
        while user_input not in ["1", "2", "3", "4"]:
            user_input = input(f"Error : {message}")
        return user_input

    def tournament_players(self):
        players = Tournament.get_list_tournaments()[1]["players"]
        players.sort(key=lambda x: x["last_name"])
        print_tournament_players(players)

    def tournament_players_elos(self):
        elos = Tournament.get_list_tournaments()[1]["players"]
        elos.sort(key=lambda x: x["elo"])
        print_tournament_players(elos)

    def list_round_tournament(self):
        round = Tournament.get_list_tournaments()[1]["rounds"]
        print_tournament_rounds(round)

    def list_matchs_tournament(self):
        round = Tournament.get_list_tournaments()[1]["rounds"]
        print_tournament_matchs(round)
