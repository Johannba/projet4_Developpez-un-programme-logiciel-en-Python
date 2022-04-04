def print_match(match):
    print("---------------------------")
    print(f"Player 1 : {match.player1}")
    print(f"Player 2 : {match.player2}")


def score_match(match):
    print_match(match)
    print("Résultat du match : ")
    user_input = input(
        "Tapez 1 pour le joueur 1 | 2 pour joueur 2 | 3 pour un match nul : "
    )
    return user_input
