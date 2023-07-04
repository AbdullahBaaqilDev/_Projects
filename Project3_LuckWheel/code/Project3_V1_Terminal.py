#Mad with abodi2098
#-----------------------|
import random
import time
def agine():
    time.sleep(0.50)
    agine = input("agine?\033[0;30m(y/n):\033[0;0m ")
    if agine.lower() == "y":
        start()
    elif agine.lower() == "n":
        quit()
    else:
        start()
print("This program will choose a random Things \njust type his name with Enter")
print("\033[0;0m--------------------------------------")
time.sleep(2.25)
def start():
    user = input("How many Things you want:\033[0;32m ")
    print("\033[0;0m-------------------------------")
    if user == "1":
        print("Waaaaoooooooooow you are sooooo\033[1;31m SMART \033[0;0m ")
        print("sorry you are so smart to test my projact")
        print("quit()")
        quit()
    elif user >= "99":
        print("This is not funy")
    elif user == "2":
        Time = 2.30
    elif user == "3":
        Time = 2.10
    elif user == "4":
        Time = 1.80
    elif user == "5":
        Time = 1.50
    elif user == "6":
        Time = 1.20
    elif int(user) > 6:
        Time = 1.00
    names = []
    for o in range(int(user)):
        name = input(o+":")
        names.append(name)
    v = len(names)
    random_num = random.randint(0,v-1)
    color = "\033[1;96m"
    print("\033[0;36m--------|Choosing...|--------")
    #    sleep(<seconds>) floot
    time.sleep(Time)
    print("\033[0;36mTHE BOT CHOOSE " + color + names[random_num])
    time.sleep(0.25)
    print("\033[0;36m-----------------------------\033[0;0m")
    agine()

start()
