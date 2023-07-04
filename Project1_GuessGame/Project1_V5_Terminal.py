import random
import time

# defind colors
RED    = "\033[0;31m"
GREEN = "\033[0;32m"
WHITE = "\033[1;37m"
YELLOW = "\033[1;33m"
NONE   = "\033[0;0m"

class GuessGame():
    def __init__(self,from_:int,to_:int):
        print(f"{WHITE}\nWelcome to Guess Game where you need to guess the number correctly.\n--------------------------------------------------------------------")
        
        self.from_ = from_
        self.to_ = to_

        self.random_number_range = range(self.from_,self.to_)
        self.players = []
        self.scores = []
        self.get_inputs()
        
    def get_inputs(self):
        # get game inputs
        self.attempts = int(input(f"{WHITE}Enter how many attempts: {YELLOW}"))

        # get players input
        self.players_number = int(input(f"{WHITE}Enter players number: {YELLOW}"))
        print(                          f"{NONE}_________________________________")
        for player_index in range(self.players_number):
            player_name = input(f"{WHITE}Player {player_index+1} enter your name: {YELLOW}")
            print(               f"{NONE}---------------------------------------")
            self.players.append(player_name)
        self.start_game()
    
    def start_game(self):
        for index,player in enumerate(self.players):
            print(f"{NONE}\n")
            print(f"{GREEN}{player} Start.")
            player_score = 0
            random_number = random.randint(self.from_,self.to_)
            for i in range(self.attempts):
                print(random_number)
                guess = int(input(f"{WHITE}Guess number ({self.from_},{self.to_}): {YELLOW}"))
                if guess == random_number:
                    print(f"{GREEN}Rgiht!! the number was {random_number}")
                    random_number = random.randint(self.from_,self.to_)
                    player_score += 1
                elif guess < random_number:
                    print(f"{RED}Sory!! the number is higher")
                elif guess > random_number:
                    print(f"{RED}Sory!! the number is lower")
                print(NONE+"---------------------------------------")
            self.scores.append(player_score)
        self.calculte_score()

    def calculte_score(self):
        print(f"{NONE}________|Calculate the scores|_________")
        time.sleep(1.0)
        for index,score in enumerate(self.scores):
            print(f"{WHITE}{self.players[index]} score is :{score}")
            print(f"{NONE}-----------")
        

        max_score = max(self.scores)
        winners = []
        for index,score in enumerate(self.scores):
            if score == max_score:
                winners.append(self.players[index])

        if len(winners) > 1:
            winners_str = ""
            for index,winner in enumerate(winners):
                if index != len(winners)-1:
                    winners_str += winner+","
                else:
                    winners_str += winner
            print(f"{WHITE}Winner: {winners_str}")
        elif len(winners) == 1:
            print(f"{WHITE}Winner: {winners[0]}")
        self.ask_agine()

    def ask_agine(self):
        print(f"{NONE}_______________________________________")
        ask = input(f"Do want to play agine (y,n): {YELLOW}").lower()
        if ask in ["yes","y"]:
            self.start_game()
        elif ask in ["no","n"]:
            exit()
        else:
            self.start_game()
if __name__ == "__main__":
    new_game = GuessGame(1,5)