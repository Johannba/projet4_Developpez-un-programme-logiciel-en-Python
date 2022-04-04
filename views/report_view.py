def print_menu_report():
    print("--------------------------------------------------\n")
    print("Rapports:\n")
    print("1 : Afficher les acteurs par ordre alphabétique ")
    print("2 : Afficher les acteurs par ordre de elo ")
    print("3 : Infos d'un tournoi ")


def print_report_players_and_elo(players):
    for player in players:
        print(
            f"{player['first_name']} {player['last_name']} : elo = {player['last_name']} {player['elo']}"
        )


def print_tournament_name(tournaments):
    print("--------------------------------------------------\n")
    print("Tapez le tournoi:\n")
    for tournament in tournaments:
        print(f"{tournament}\n")


def print_tournament_players(players):
    print("--------------------------------------------------\n")
    print("Menu tournoi:\n")
    for player in players:
        print(f"{player['last_name']} {player['first_name']} : elo = {player['elo']} ")


def print_tournaments_menu():
    print("--------------------------------------------------\n")
    print("Infos d'un tournoi:\n")
    print("1 : Afficher les joueurs du tournoi par ordre alphabétique ")
    print("2 : Afficher les joueurs du tournoi par ordre elo ")
    print("3 : Liste de tous les tours d'un tournoi ")
    print("4 : Liste de tous les matchs d'un tournoi \n")


def print_tournament_rounds(rounds):
    print("--------------------------------------------------\n")
    print("Menu tournoi:\n")
    for round in rounds:
        print(
            f"{round['number']} : start : {round['start_time']} : end : {round['end_time']}"
        )


def print_tournament_matchs(rounds):
    print("--------------------------------------------------\n")
    print("Menu tournoi:\n")
    for round in rounds:
        print("---------------------------------------")
        print(f"{round['number']} :")
        for match in round["matchs"]:
            print("------------------")
            print(
                f"{match['player1']['first_name']} VS {match['player2']['first_name']}"
            )
            print(f"Score : {match['player1']['score']} : {match['player2']['score']}")
