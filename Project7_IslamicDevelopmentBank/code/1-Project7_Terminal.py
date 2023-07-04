import json as J
import time as T
import datetime as DT
import getpass as G
class IslamicDevelopmentBank():
    class NewUser:
        def __init__(self,user_name,user_birth,user_money,user_nationality,user_password,file_name):
            self.user_name        = user_name
            self.user_birth       = user_birth
            self.user_money       = user_money
            self.user_nationality = user_nationality
            self.user_password    = user_password
            self.file_name        = file_name
            with open("D:\\Abdullah\\PROGRAMS\\Coding\\_PYTHON\\_Projects\\Project7_IslamicDevelopmentBank\\"+file_name,"r") as file:
                data_dect = J.load(file)
            if self.user_name not in data_dect["names_list"]:
                user_dect = {"name":self.user_name,"birth":self.user_birth,"money":self.user_money,"nationality":self.user_nationality,"password":self.user_password,"request":[]}
                data_dect[self.user_name] = user_dect
                data_dect["names_list"].append(self.user_name)
                data_dect["passwords_list"].append(self.user_password)
                data_dect["births_list"].append(self.user_birth)
                data_dect["money_list"].append(self.user_money)
                data_dect["nationalitys_list"].append(self.user_nationality)
                with open("D:\\Abdullah\\PROGRAMS\\Coding\\_PYTHON\\_Projects\\Project7_IslamicDevelopmentBank\\"+file_name,"w") as file:
                    data = J.dump(data_dect,file,indent=4)
                print("Sign up was successful")
                IslamicDevelopmentBank.BuySheep(self.user_name,self.user_birth,self.user_money,self.user_nationality,self.user_password,"Data.json")
            else:
                print("You are already Sign up.")
                IslamicDevelopmentBank().print_user_infos(self.user_name,self.user_birth,self.user_money,self.user_nationality,self.user_password,"Data.json")
    class BuySheep:
        def __init__(self,user_name,user_birth,user_money,user_nationality,user_password,file_name):
            self.user_name = user_name
            self.user_birth       = user_birth
            self.user_money       = user_money
            self.user_nationality = user_nationality
            self.user_password    = user_password
            self.file_name        = file_name
            options = """Press (1) to buy sheep\nPress (2) to show Your informations\nPress (3) to Log out"""
            print("------------------------------------")
            print(options)
            user_option = input("Enter number: ")
            if user_option == "1":
                how_many_sheeps = input("How many sheeps: ")
                self.buy_sheep(int(how_many_sheeps),user_name,user_birth,user_money,user_nationality,user_password,"Data.json")
            elif user_option == "2":
                IslamicDevelopmentBank().print_user_infos(user_name,user_birth,user_money,user_nationality,user_password,"Data.json")
            elif user_option == "3":
                person = IslamicDevelopmentBank()
        def buy_sheep(self,how_many_sheeps,user_name,user_birth,user_money,user_nationality,user_password,file_name):
            with open("D:\\Abdullah\\PROGRAMS\\Coding\\_PYTHON\\_Projects\\Project7_IslamicDevelopmentBank\\"+file_name,"r") as file:
                data_dect = J.load(file)
            the_cost = how_many_sheeps * 1000
            if data_dect[self.user_name]["money"] >= the_cost:
                data_dect[self.user_name]["money"] =- the_cost
                date_now = DT.datetime.now()
                year_now = date_now.year
                month_now = date_now.month
                day_now = date_now.day
                hour_now = date_now.hour
                date_now_string = "{}/{}/{}-H:{}".format(year_now,month_now,day_now,hour_now)
                data_dect[self.user_name]["requests_list"].append("({}) bought {} sheep the cost was {}".format(date_now_string,how_many_sheeps,the_cost))
                print("-------------------------------")
                print("You have successfully bought {} sheep".format(how_many_sheeps))
                with open("D:\\Abdullah\\PROGRAMS\\Coding\\_PYTHON\\_Projects\\Project7_IslamicDevelopmentBank\\"+file_name,"w") as file:
                    data = J.dump(data_dect,file,indent=4)
                IslamicDevelopmentBank.BuySheep(user_name,user_birth,user_money,user_nationality,user_password,"Data.json")
            elif data_dect[self.user_name]["money"] < the_cost:
                print("Sorry, but you are POOR.")
                App = IslamicDevelopmentBank().reception()
    def reception(self):
        print("--------------------------------------")
        print("Welcome to Adahi app:")
        options = """Press (1) to Log in\nPress (2) to Sign up\nPress (3) to Exit"""
        print(options)
        user_option = input("Enter number: ")
        if user_option == "1":
            self.log_in("Data.json")
        elif user_option == "2":
            print("-----------------------------")
            self.user_name = input("Enter Your name: ")
            self.user_birth = input("Enter Your birth: ")
            self.user_money = int(input("Enter Your money: "))
            self.user_nationality = input("Enter Your nationality: ")
            self.user_password = G.getpass(prompt="Enter password: ")
            print("------------------------------")
            person = IslamicDevelopmentBank.NewUser(self.user_name,self.user_birth,self.user_money,self.user_nationality,self.user_password,"Data.json")
        elif user_option == "3":
            exit()
    def log_in(self,file_name):
        with open("D:\\Abdullah\\PROGRAMS\\Coding\\_PYTHON\\_Projects\\Project7_IslamicDevelopmentBank\\"+file_name,"r") as file:
            data_dect = J.load(file)
        self.get_name = input("Enter Your name: ")
        if self.get_name in data_dect["names_list"]:
            index_number = 0
            for name in data_dect["names_list"]:
                if name == self.get_name:
                    self.name_index = index_number
                else:index_number += 1
            global how_many_wrong_password
            global how_many_wrong_birth
            how_many_wrong_birth = 0
            how_many_wrong_password = 0
            def ask_for_birth():
                global how_many_wrong_birth
                self.get_birth = input("Enter Your birth: ")
                if self.get_birth == data_dect["births_list"][self.name_index]:
                    self.print_user_infos(data_dect[self.get_name]["name"],data_dect[self.get_name]["birth"],data_dect[self.get_name]["money"],data_dect[self.get_name]["nationality"],data_dect[self.get_name]["password"],"Data.json")
                else:
                    if how_many_wrong_birth < 2:
                        print("Wrong birth!!")
                        how_many_wrong_birth += 1
                        ask_for_birth()
                    elif how_many_wrong_birth >= 2 and how_many_wrong_birth < 3:
                        print("Wrong birth wait 3 Seconds!!")
                        T.sleep(3)
                        how_many_wrong_birth += 1
                        ask_for_birth()
                    elif how_many_wrong_birth >= 3 and how_many_wrong_birth < 4:
                        print("Wrong birth wait 5 Seconds!!")
                        T.sleep(5)
                        how_many_wrong_birth += 1
                        ask_for_birth()
                    elif how_many_wrong_birth >= 4 and how_many_wrong_birth < 5:
                        print("Wrong birth wait 10 Seconds!!")
                        T.sleep(10)
                        how_many_wrong_birth += 1
                        ask_for_birth()
                    else:
                        print("Wrong birth Please sign up")
                        self.user_name = input("Enter Your name: ")
                        self.user_birth = input("Enter Your birth: ")
                        self.user_money = int(input("Enter Your money: "))
                        self.user_nationality = input("Enter Your nationality: ")
                        self.user_password = G.getpass(prompt="Enter password: ")
                        print("------------------------------")
                        person = IslamicDevelopmentBank.NewUser(self.user_name,self.user_birth,self.user_money,self.user_nationality,self.user_password,"Data.json")
            def ask_for_password():
                global how_many_wrong_password
                self.get_password = G.getpass(prompt="Enter password: ")
                if self.get_password == data_dect["passwords_list"][self.name_index]:
                    buy_operation = IslamicDevelopmentBank.BuySheep(data_dect[self.get_name]["name"],data_dect[self.get_name]["birth"],data_dect[self.get_name]["money"],data_dect[self.get_name]["nationality"],data_dect[self.get_name]["password"],"Data.json")
                else:
                    if how_many_wrong_password < 2:
                        print("Wrong pssword!!")
                        how_many_wrong_password += 1
                        ask_for_password()
                    elif how_many_wrong_password >= 2 and how_many_wrong_password < 3:
                        print("Wrong pssword wait 30 Seconds!!")
                        T.sleep(30)
                        how_many_wrong_password += 1
                        ask_for_password()
                    elif how_many_wrong_password >= 3 and how_many_wrong_password < 4:
                        print("Wrong pssword wait 40 Seconds!!")
                        T.sleep(40)
                        how_many_wrong_password += 1
                        ask_for_password()
                    elif how_many_wrong_password >= 4 and how_many_wrong_password < 5:
                        print("Wrong pssword wait 1 minute!!")
                        T.sleep(60)
                        how_many_wrong_password += 1
                        ask_for_password()
                    else:
                        print("Wrong pssword Please enter Your birth day")
                        ask_for_birth()
            ask_for_password()
        else:
            wrong_name_option = input("This nams is not defind do You want to sgin up(write 1) or try agien(write 2): ")
            if wrong_name_option == "1":
                self.user_name = input("Enter Your name: ")
                self.user_birth = input("Enter Your birth: ")
                self.user_money = int(input("Enter Your money: "))
                self.user_nationality = input("Enter Your nationality: ")
                self.user_password = G.getpass(prompt="Enter password: ")
                print("------------------------------")
                person = IslamicDevelopmentBank.NewUser(self.user_name,self.user_birth,self.user_money,self.user_nationality,self.user_password,"Data.json")
            elif wrong_name_option == "2":
                self.log_in("Data.json")
            else:
                print("Sorry, i didn't understand you i will restart log in operation")
                self.log_in("Data.json")
    def print_user_infos(self,user_name,user_birth,user_money,user_nationality,user_password,file_name):
        with open("D:\\Abdullah\\PROGRAMS\\Coding\\_PYTHON\\_Projects\\Project7_IslamicDevelopmentBank\\"+file_name,"r") as file:
            data_dect = J.load(file)
        print("----------------------------------")
        print("{} Informations:-\nBirth: {}\nCurrint money: {}\nNationality: {}\nPassword: {}".format(user_name,user_birth,user_money,user_nationality,user_password))
        print("Buy history:")
        for i in range(len(data_dect[user_name]["requests_list"])):
            print(data_dect[user_name]["requests_list"][i])
        App = IslamicDevelopmentBank.BuySheep(user_name,user_birth,user_money,user_nationality,user_password,file_name)
IslamicDevelopmentBank().reception()