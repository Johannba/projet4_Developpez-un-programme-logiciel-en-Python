def get_user_input(message):
    user_input = input(message)
    return user_input


def print_message(message):
    print(message)


def print_classement(players):
    players.sort(key=lambda x: x.elo)
    players.sort(key=lambda x: x.score, reverse=True)
    print("\n\n")
    print("--------------------------------------------------")
    for i in range(8):
        print(f"{i + 1} : {players[i]} | score : {players[i].score}")
    print("--------------------------------------------------")


def print_on_going_tournament(on_going_tournament):
    tournaments = [i[:] for i in on_going_tournament]
    for index, name in enumerate(tournaments):
        print(f"{index + 1} : {name}")
