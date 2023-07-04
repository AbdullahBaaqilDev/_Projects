import random

def want_play():
    play_again = input("do you want to play again (yes/no): ")
    if play_again.lower() == "yes":
        start_game()
    elif play_again.lower() == "no":
        print("ok see you soon 😉")

def start_game():
    player_name = input("Enter Your Name: ")
    attempts = input("How Much attempts: ")
    wins = 0
     
    while wins != int(attempts):
        random_num = int(random.randint(1,5))
        guess = input("Enter Number (1-5): ")
        if int(guess) == random_num:
            print("Cooooooooool you got it")
            wins += 1
        elif int(guess) > random_num:
            print("oh the number is lower than "+guess)
        elif int(guess) < random_num:
            print("oh the numder is higher than "+guess)
        if wins == int(attempts):
            print("Congratulation "+ player_name +" you win")
    else:
        want_play()
start_game()