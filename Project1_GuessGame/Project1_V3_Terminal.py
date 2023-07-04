#Mad with abodi2098
#-----------------------|

import random

def how_player():
    how_player = input("How Mach Player You Want?(1-5) ")
    if   int(how_player) == 1:
        start_game1()
    elif int(how_player) == 2:
        start_game2()
    elif int(how_player) == 3:
        start_game3()
    elif int(how_player) == 4:
        start_game4()
    elif int(how_player) == 5:
        start_game5()


"-----------------------------------|1 player|--------------------------------------"

def want_play1():
    play_again = input("Do You Want To Play Again (yes/no): ")
    if play_again.lower() == "yes":
        how_player()
    elif play_again.lower() == "no":
        print("Ok See You Soon 😉")
    else:
        how_player()

def start_game1():
    player1 = input("Enter Your Name: ")
    Attempts = input("How Much Attempts: ")
    print("-------------------------------")
    win1 = []     

    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess1 = input("Enter Number First Player (1-5): ")
        if int(gess1) == random_num:
            print("COOOOOOOL You Got It")
            win1.append("win")
        elif int(gess1) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess1) < random_num:
            print("Oh The Number Was "+str(random_num))
    print("----------------------------------------------")
    
   

    def the_score1():
        player1_score   = len(win1)
        print("Player " + player1 + " Score Is " + str(player1_score))
        want_play2()

    the_score1()

"-----------------------------------|2 players|--------------------------------------"

def want_play2():
    play_again = input("Do You Want To Play Again (yes/no): ")
    if play_again.lower() == "yes":
        how_player()
    elif play_again.lower() == "no":
        print("Ok See You Soon 😉")
    else:
        how_player()

def start_game2():
    player1 = input("Enter Your Name First Player: ")
    player2 = input("Enter Your Name Sacond Player: ")
    Attempts = input("How Much Attempts: ")
    print("-----------------------------------")
    win1 = []     
    win2 = []

    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess1 = input("Enter Number First Player (1-5): ")
        if int(gess1) == random_num:
            print("COOOOOOOL You Got It")
            win1.append("win")
        elif int(gess1) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess1) < random_num:
            print("Oh The Number Was "+str(random_num))
        
    print("-------------|Player 2|-------------")
        
    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess2 = input("Enter Number Sacond Player(1-5): ")
        if int(gess2) == random_num:
            print("COOOOOOOOOL You Got It")
            win2.append("win")
        elif int(gess2) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess2) < random_num:
            print("Oh The Number Was "+str(random_num))
    print("----------------------------------------------")

    def the_score2():
        player1_score   = len(win1)
        player2_score   = len(win2)
        print(player1 + " Score Is " + str(player1_score))
        print(player2 + " Score Is " + str(player2_score))
        if player1_score < player2_score:
            print(player2+" Win")
        elif player1_score == player2_score:
            print("IT'S A DRAW")
        else:
            print(player1+" Win")
        want_play2()

    the_score2()

"-----------------------------------|3 players|--------------------------------------"

def want_play3():
    play_again = input("Do You Want To Play Again (yes/no): ")
    if play_again.lower() == "yes":
        how_player()
    elif play_again.lower() == "no":
        print("Ok See You Soon 😉")
    else:
        how_player()

def start_game3():
    player1 = input("Enter Your Name First Player: ")
    player2 = input("Enter Your Name Sacond Player: ")
    player3 = input("Enter Your Name Third Player: ")
    Attempts = input("How Much Attempts: ")
    print("-----------------------------------")

    win1 = []     
    win2 = []
    win3 = []

    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess1 = input("Enter Number First Player (1-5): ")
        if int(gess1) == random_num:
            print("COOOOOOOOOOOL You Got It")
            win1.append("win")
        elif int(gess1) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess1) < random_num:
            print("Oh The Number Was "+str(random_num))
        
    print("-------------|Player 2|-------------")
        
    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess2 = input("Enter Number Sacond Player(1-5): ")
        if int(gess2) == random_num:
            print("COOOOOL You Got It")
            win2.append("win")
        elif int(gess2) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess2) < random_num:
            print("Oh The Number Was "+str(random_num))

    print("-------------|Player 3|-------------")
        
    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess3 = input("Enter Number Sacond Player(1-5): ")
        if int(gess3) == random_num:
            print("COOOOOOOOOOOL You Got It")
            win3.append("win")
        elif int(gess3) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess3) < random_num:
            print("Oh The Number Was "+str(random_num))
    print("----------------------------------------------")
    
    def the_score3():
        player1_score = len(win1)
        player2_score = len(win2)
        player3_score = len(win3)
        print("Player " + player1 + " Score Is" + str(player1_score))
        print("Player " + player2 + " Score Is" + str(player2_score))
        print("Player " + player3 + " Score Is" + str(player3_score))
        want_play3()
    the_score3()

"-----------------------------------|4 players|--------------------------------------"

def want_play4():
    play_again = input("Do You Want To Play Again (yes/no): ")
    if play_again.lower() == "yes":
        how_player()
    elif play_again.lower() == "no":
        print("Ok See You Soon 😉")
    else:
        how_player()

def start_game4():
    player1 = input("Enter Your Name First Player: ")
    player2 = input("Enter Your Name Sacond Player: ")
    player3 = input("Enter Your Name Therd Player: ")
    player4 = input("Enter Your Name fourth Player: ")
    Attempts = input("How Much Attempts: ")
    print("-----------------------------------")

    win1 = []     
    win2 = []
    win3 = []
    win4 = []

    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess1 = input("Enter Number First Player (1-5): ")
        if int(gess1) == random_num:
            print("COOOOOOOOOOOL You Got It")
            win1.append("win")
        elif int(gess1) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess1) < random_num:
            print("Oh The Number Was "+str(random_num))
        
    print("-------------|Player 2|-------------")
        
    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess2 = input("Enter Number Sacond Player(1-5): ")
        if int(gess2) == random_num:
            print("COOOOOOOL You Got It")
            win2.append("win")
        elif int(gess2) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess2) < random_num:
            print("Oh The Number Was "+str(random_num))

    print("-------------|Player 3|-------------")
        
    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess3 = input("Enter Number Sacond Player(1-5): ")
        if int(gess3) == random_num:
            print("COOOOOOOOOOL You Got It")
            win3.append("win")
        elif int(gess3) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess3) < random_num:
            print("Oh The Number Was "+str(random_num))

    print("-------------|Player 4|-------------")
        
    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess4 = input("Enter Number Sacond Player(1-5): ")
        if int(gess4) == random_num:
            print("COOOOOOL You Got It")
            win4.append("win")
        elif int(gess4) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess4) < random_num:
            print("Oh The Number Was "+str(random_num))
    print("----------------------------------------------")

    def the_score4():
        player1_score = len(win1)
        player2_score = len(win2)
        player3_score = len(win3)
        player4_score = len(win4)
        print("Player " + player1 + " Score Is" + str(player1_score))
        print("Player " + player2 + " Score Is" + str(player2_score))
        print("Player " + player3 + " Score Is" + str(player3_score))
        print("Player " + player4 + " Score Is" + str(player4_score))
        want_play4()
    the_score4()

"-----------------------------------|5 players|--------------------------------------"

def want_play5():
    play_again = input("Do You Want To Play Again (yes/no): ")
    if play_again.lower() == "yes":
        how_player()
    elif play_again.lower() == "no":
        print("Ok See You Soon 😉")
    else:
        how_player()

def start_game5():
    player1 = input("Enter Your Name First Player: ")
    player2 = input("Enter Your Name Sacond Player: ")
    player3 = input("Enter Your Name Therd Player: ")
    player4 = input("Enter Your Name Fourth Player: ")
    player5 = input("Enter Your Name Fifth Player: ")
    Attempts = input("How Much Attempts: ")
    print("-----------------------------------")

    win1 = []     
    win2 = []
    win3 = []
    win4 = []
    win5 = []

    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess1 = input("Enter Number First Player (1-5): ")
        if int(gess1) == random_num:
            print("COOOOOOOOOOOOOL You Got It")
            win1.append("win")
        elif int(gess1) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess1) < random_num:
            print("Oh The Number Was "+str(random_num))
        
    print("-------------|Player 2|-------------")
        
    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess2 = input("Enter Number Sacond Player(1-5): ")
        if int(gess2) == random_num:
            print("COOOOOOOOOOOL You Got It")
            win2.append("win")
        elif int(gess2) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess2) < random_num:
            print("Oh The Number Was "+str(random_num))

    print("-------------|Player 3|-------------")
        
    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess3 = input("Enter Number Sacond Player(1-5): ")
        if int(gess3) == random_num:
            print("COOOOOOOOOOOL You Got It")
            win3.append("win")
        elif int(gess3) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess3) < random_num:
            print("Oh The Number Was "+str(random_num))

    print("-------------|Player 4|-------------")
        
    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess4 = input("Enter Number Sacond Player(1-5): ")
        if int(gess4) == random_num:
            print("COOOOOL You Got It")
            win4.append("win")
        elif int(gess4) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess4) < random_num:
            print("Oh The Number Was "+str(random_num))

    print("-------------|Player 5|-------------")
        
    for l in range(int(Attempts)):
        random_num = int(random.randint(1,5))
        gess5 = input("Enter Number Sacond Player(1-5): ")
        if int(gess5) == random_num:
            print("COOOOOOOOL You Got It")
            win5.append("win")
        elif int(gess5) > random_num:
            print("Oh The Number Was "+str(random_num))
        elif int(gess5) < random_num:
            print("Oh The Number Was "+str(random_num))
    print("----------------------------------------------")
    
    def the_score5():
        player1_score = len(win1)
        player2_score = len(win2)
        player3_score = len(win3)
        player4_score = len(win4)
        player5_score = len(win5)
        print("Player " + player1 + " Score Is " + str(player1_score))
        print("Player " + player2 + " Score Is " + str(player2_score))
        print("Player " + player3 + " Score Is " + str(player3_score))
        print("Player " + player4 + " Score Is " + str(player4_score))
        print("Player " + player5 + " Score Is " + str(player5_score))
       
        want_play4()
    the_score5()
how_player()