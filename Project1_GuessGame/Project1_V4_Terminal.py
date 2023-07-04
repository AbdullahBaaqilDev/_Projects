#Mad with abodi2098
#-----------------------|
import random
import time

#THE COLORS -------
Red    = "\033[0;31m"
BRed    = "\033[1;31m"
Green  = "\033[0;32m"
BGreen = "\033[1;32m"
BBlack = "\033[1;30m"
UBlack = "\033[4;30m"
White  = "\033[0;37m"
BWhite = "\033[1;37m"
Yellow = "\033[0;33m"
Blue   = "\033[0;94m"
no     = "\033[0;0m"


def want_play():
    print("__________________________________________")
    ask = input(BWhite + "Do you want to play agine (yes/no) " + no + "")
    if ask.lower() == "yes":
        start_game()
    elif ask.lower() == "no":
        print(Yellow + "        OK see you soon😉 " + no + "")
        ask2 = input(" ")
        if ask2.lower() == "i meen yes":
            start_game()

def start_game():

    #-------------info of game
    print("__________________________________________")
    how_players = input("How many players? "+Blue )
    attempts = input(no +"How many attempts? "+Blue)
    print(no+"-------------------------------")
    players_names = []
    player_score  = []
    random_numbers = []
    for w in range(int(how_players)):
        player_name = input("Enter your name player " + str(w+1) + " :"+Green)
        players_names.append(player_name)


     #-------------the guesing
        print(no+"-------------------------------")
    for e in range(int(how_players)):

        print((Green + players_names[e] + " You can start") + no + "")

        random_numbers = []
        random_num = random.randint(1,10)
        for o in range(1):
            random_numbers.append(random_num)

        for k in range(int(attempts)):

            gess = input(BWhite + "Print number (1-10):" + no + " ")
            if int(gess) == random_numbers[0]:
                print(Green + "WOOOOOOOOW you got it" + no + " ")
                player_score.append(("win" + str(e)))

                random_numbers = []
                random_num = random.randint(1,10)
                for o in range(int(attempts)):
                    random_numbers.append(random_num)

            elif int(gess) < random_numbers[0]:
                print(Red + "OH the random number is higher" + no + "")
            elif int(gess) > random_numbers[0]:
                print(Red + "OH the random number is lower" + no + "")


    #-------------the score
    higher_score = 0
    winner_player = ""
    the_scores = []


    if int(how_players) == 1:
        for r in range(int(how_players)):

            if player_score == []:
                player_score = [0]
            if the_scores == []:
                the_scores = [0]
            print (BWhite + str(players_names[0]) + " your score is " + str(the_scores[0]) + no + "")

    else:
        print("__________________________________")
        print("The Bot is calculate the scores...")
        time.sleep(0.75)
        for t in range(int(how_players)):

            for p in range(int(how_players)):
                p_s_c = player_score.count("win"+str(p))
                the_scores.append(p_s_c)
            next_score = iter(the_scores)
        for b in range(int(how_players)):
            print(BWhite + players_names[b] + " score is " + str(the_scores[b]) + no + "")
            time.sleep(0.05)
            print("------------------------")
            time.sleep(0.25)
    want_play()
start_game()