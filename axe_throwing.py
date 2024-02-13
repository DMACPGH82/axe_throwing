from random import choice

def get_player_input(player_name, round_number, throw_number):
    return int(input(f"{player_name} SCORES A: "))

def print_round_score(player_name, round_total):
    print(f"The score is {player_name} {round_total}")

def play_round(player_one, player_two, round_number):
    round_total = [0, 0]
    for throw in range(5):
        print(f"ROUND NUMBER {round_number}, THROW NUMBER {throw + 1}")
        scores = [get_player_input(player_one, round_number, throw + 1),
                  get_player_input(player_two, round_number, throw + 1)]
        round_total = [round_total[i] + scores[i] for i in range(2)]
        print_round_score(player_one, round_total[0])
        print_round_score(player_two, round_total[1])
    return round_total

def print_round_winner(player, round_total):
    print(f"{player} TAKES THE ROUND!!!")

def print_round_tie():
    print("ROUND ENDS IN A TIE!!!")

def print_match_winner(winner, scores):
    print(f"AND THE WINNER IS: {winner} WITH A SCORE OF {scores[winner]} TO {scores[1 - winner]}")

def print_match_tie(scores):
    print(f"THE MATCH ENDS WITH {scores[0]} SCORING {scores[0]}, AND {scores[1]} SCORING {scores[1]}, WHICH IS A TIE")

def main():
    print("WELCOME TO THE HOUSE OF AXE THROWING!!!!")
    player_one = input("PLEASE ENTER THE NAME OF THE FIRST PLAYER: ").strip().upper()
    player_two = input("PLEASE ENTER THE NAME OF THE SECOND PLAYER: ").strip().upper()
    intro_choices = ["LET US PREPARE TO WATCH THESE TWO TITANS BATTLE IT OUT: ",
                     "TONIGHT IS ANOTHER CHAPER IN THE IMMORTAL BATTLE BETWEEN: ",
                     "GATHER AROUND BECAUSE IT WILL BE A BLOOD BATH WHEN IT IS: ",
                     "MARVEL AT THE AWESOMENESS WHEN YOU SEE THESE TWO FIGHT TO THE DEATH!!!: ",
                     "GATHER AROUND AND BE A WITNESS TO THE UNDOING OF ALL YOU KNOW, WHEN IT IS: "]
    match_intro = choice(intro_choices)
    print(match_intro)
    print("{} VERSUS {}!!!!".format(player_one, player_two))

    player_scores = [[0, 0], [0, 0], [0, 0]]  # [round][player]

    for round_number in range(3):
        round_scores = play_round(player_one, player_two, round_number + 1)
        player_scores[round_number] = round_scores
        round_winner = player_one if round_scores[0] > round_scores[1] else (player_two if round_scores[1] > round_scores[0] else None)
        if round_winner:
            print_round_winner(round_winner, round_scores)
        else:
            print_round_tie()

    total_scores = [sum(scores) for scores in zip(*player_scores)]
    match_winner = player_one if total_scores[0] > total_scores[1] else (player_two if total_scores[1] > total_scores[0] else None)
    if match_winner:
        print_match_winner(match_winner, total_scores)
    else:
        print_match_tie(total_scores)

if __name__ == "__main__":
    main()
