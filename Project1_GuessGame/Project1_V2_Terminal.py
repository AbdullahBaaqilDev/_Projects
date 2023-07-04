#Mad with abodi2098
#-----------------------|

import random


def want_play():
    play_again = input("Do You Want To Play Again (yes/no): ")
    if play_again.lower() == "yes":
        start_game()
    elif play_again.lower() == "no":
        print("Ok See You Soon 😉")

def start_game():
    attempts = input("How Much Attempts: ")
    player1 = input("Enter Your Name First Player: ")
    player2 = input("Enter Your Name Sacond Player: ")

    win1 = []     
    win2 = []

    for l in range(int(attempts)):
        random_num = int(random.randint(1,5))
        guess1 = input("Enter Number First Player (1-5): ")
        if int(guess1) == random_num:
            print("COOOOOOOL You Got It")
            win1.append("win")
        elif int(guess1) > random_num:
            print("Oh The Number Is Lower Than "+guess1)
        elif int(guess1) < random_num:
            print("Oh The Numder Is Higher Than "+guess1)
            print("The Number Was "+str(random_num))
        
    print("-------------Player 2-------------")
        
    for l in range(int(attempts)):
        random_num = int(random.randint(1,5))
        guess2 = input("Enter Number Sacond Player(1-5): ")
        if int(guess2) == random_num:
            print("COOOOOOOL You Got It")
            win2.append("win")
        elif int(guess2) > random_num:
            print("Oh The Number Is Lower Than "+guess2)
        elif int(guess2) < random_num:
            print("Oh The Numder Is Higher Than "+guess2)
            print("The Number Was "+str(random_num))

    def the_score():
        player1_score   = len(win1)
        player2_score   = len(win2)
        print("Player " + player1 + " Score Is")
        print(player1_score)
        print(player2 + " Score Is")
        print("Player " + str(player2_score))
        if player1_score < player2_score:
            print(player2+" Win")
        elif player1_score < player2_score: 
            print(player1+" Win")
        elif player1_score == player2_score:
            print("Draw")
        want_play()
    the_score()
start_game()