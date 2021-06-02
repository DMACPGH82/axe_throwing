from random import choice
rounds = 1
throws = 1
player_one_score = 0
player_two_score = 0
player_one_round_one_total = 0
player_two_round_one_total = 0
player_one_round_two_total = 0
player_two_round_two_total = 0
player_one_round_three_total = 0
player_two_round_three_total = 0
player_one_match_total = 0
player_two_match_total = 0

print("WELCOME TO THE HOUSE OF AXE THROWING!!!!")

player_one = input(
    "PLEASE ENTER THE NAME OF THE FIRST PLAYER: ").strip().upper()

player_two = input(
    "PLEASE ENTER THE NAME OF THE SECOND PLAYER: ").strip().upper()

intro_choices = ["LET US PREPARE TO WATCH THESE TWO TITANS BATTLE IT OUT: ",
                 "TONIGHT IS ANOTHER CHAPER IN THE IMMORTAL BATTLE BETWEEN: ",
                 "GATHER AROUND BECAUSE IT WILL BE A BLOOD BATH WHEN IT IS: ",
                 "MARVEL AT THE AWESOMENESS WHEN YOU SEE THESE TWO FIGHT TO THE DEATH!!!: ",
                 "GATHER AROUND AND BE A WITNESS TO THE UNDOING OF ALL YOU KNOW, WHEN IT IS: "]

match_intro = choice(intro_choices)
print(match_intro)
print("{} VERSUS {}!!!!".format(
    player_one, player_two))

# round one
while rounds == 1 and throws <= 5:
    print("ROUND NUMBER {}, THROW NUMBER {}".format(rounds, throws))
    player_one_score = input("{} SCORES A: ".format(player_one))
    player_two_score = input("{} SCORES A: ".format(player_two))
    player_one_score_int = int(player_one_score)
    player_two_score_int = int(player_two_score)
    player_one_round_one_total = player_one_round_one_total + player_one_score_int
    player_two_round_one_total = player_two_round_one_total + player_two_score_int
    print("The score is {} {} AND {} {}".format(player_one,
                                                player_one_round_one_total, player_two, player_two_round_one_total))
    throws = throws + 1
    if throws == 6:
        p1_rd1_total = player_one_round_one_total
        p2_rd1_total = player_two_round_one_total
        if p1_rd1_total > p2_rd1_total:
            print("{} TAKES ROUND ONE!!!".format(player_one))
        if p2_rd1_total > p1_rd1_total:
            print("{} TAKES ROUND ONE!!!)".format(player_two))
        if p1_rd1_total == p2_rd1_total:
            print("ROUND ONE ENDS IN A TIE!!!")
        rounds = rounds + 1
        while rounds == 2 and throws <= 10:
            print("ROUND NUMBER {}, THROW NUMBER {}".format(rounds, throws-5))
            player_one_score = input("{} SCORES A: ".format(player_one))
            player_two_score = input("{} SCORES A: ".format(player_two))
            player_one_score_int = int(player_one_score)
            player_two_score_int = int(player_two_score)
            player_one_round_two_total = player_one_round_two_total + player_one_score_int
            player_two_round_two_total = player_two_round_two_total + player_two_score_int
            print("The score is {} {} AND {} {}".format(player_one,
                                                        player_one_round_two_total, player_two, player_two_round_two_total))
            throws = throws + 1
            if throws == 11:
                p1_rd2_total = player_one_round_two_total
                p2_rd2_total = player_two_round_two_total
                if p1_rd2_total > p2_rd2_total:
                    print("{} TAKES ROUND TWO!!!".format(player_one))
                if p2_rd2_total > p1_rd2_total:
                    print("{} TAKES ROUND TWO!!!)".format(player_two))
                if p1_rd2_total == p2_rd2_total:
                    print("ROUND TWO ENDS IN A TIE!!!")
                rounds = rounds + 1
            while rounds == 3 and throws < 16:
                print("ROUND NUMBER {}, THROW NUMBER {}".format(rounds, throws-10))
                player_one_score = input("{} SCORES A: ".format(player_one))
                player_two_score = input("{} SCORES A: ".format(player_two))
                player_one_score_int = int(player_one_score)
                player_two_score_int = int(player_two_score)
                player_one_round_three_total = player_one_round_three_total + player_one_score_int
                player_two_round_three_total = player_two_round_three_total + player_two_score_int
                print("The score is {} {} AND {} {}".format(player_one,
                                                            player_one_round_three_total, player_two, player_two_round_three_total))
                throws = throws + 1
                if throws == 16:
                    p1_rd3_total = player_one_round_two_total
                    p2_rd3_total = player_two_round_two_total
                    if p1_rd3_total > p2_rd3_total:
                        print("{} TAKES ROUND THREE!!!".format(player_one))
                    if p2_rd3_total > p1_rd3_total:
                        print("{} TAKES ROUND THREE!!!)".format(player_two))
                    if p1_rd3_total == p2_rd3_total:
                        print("ROUND THREE ENDS IN A TIE!!!")
                    print("THE MATCH IS OVER!!!")
                    player_one_match_total = p1_rd1_total + p1_rd2_total + p1_rd3_total
                    player_two_match_total = p2_rd1_total + p2_rd2_total + p2_rd3_total
                    if player_one_match_total > player_two_match_total:
                        print("AND THE WINNER IS: {} WITH A SCORE OF {} TO {}".format(
                            player_one, player_one_match_total, player_two_match_total))
                    if player_two_match_total > player_one_match_total:
                        print("AND THE WINNER IS: {}!!! WITH A SCORE OF {} TO {}".format(
                            player_two, player_two_match_total, player_one_match_total))
                    if player_one_match_total == player_two_match_total:
                        print("THE MATCH ENDS WITH {} SCORING {}, AND {} SCORING {}, WHICH IS A TIE... YOU KNOW WHAT THAT MEANS?! BIG AXE TIME!!!".format(
                            player_one, player_one_match_total, player_two, player_two_match_total))
