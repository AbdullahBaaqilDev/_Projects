import json as J
import random as R
import datetime as DT
import tkinter as TK
main_window = TK.Tk()
main_window.title("Islamic Development Bank (IDB)")
main_window.geometry("900x500+200+50")#;main_window.resizable(False,False)
main_window.config(bg="#F0F0F0")

logo_photo = TK.PhotoImage(file="D:\\Abdullah\\PROGRAMS\\Coding\\_PYTHON\\_Projects\\Project7_IslamicDevelopmentBank\\AdahiLogo.png")
logo_label = TK.Label(main_window,image=logo_photo,bg="#F0F0F0");logo_label.pack(ipady=0)

FILE_NAME = "Data.json"
FILE_PATH = "D:\\Abdullah\\PROGRAMS\\Coding\\_PYTHON\\_Projects\\Project7_IslamicDevelopmentBank\\"

class IslamicDevelopmentBank():
    class AppColors:
        WINDOW_BG      = "#F0F0F0";
        
        LIGHT_BG       = "#07B7A7";
        LIGHT_BG_ACTV  = "#039D8F";
        LIGHT_FG       = "#FFFFFF";
        LIGHT_DID_BG   = "#FFFFFF";

        GRAY_FG        = "#434343";
        GRAY_DID_BG    = "#F3F3F3";

        BLUE_BG        = "#4989F3"
        BLUE_BG_ACTV   = "#73A9FF"

        DARK_BG        = "#069C8F";
        DARK_BG_ACTV   = "#05A89B";
        DARK_FG        = "#FFFFFF";
        DARK_DID_BG    = "#404040";
    
    class LogInSignUp:
        def sign_up(self,user_name,user_birth,user_money,user_nationality,user_password,):
            self.user_id = str(R.randint(1000,9999))
            self.user_name = user_name
            self.user_birth = user_birth
            self.user_money = user_money
            self.user_nationality = user_nationality
            self.user_password = user_password
            data_dect = IslamicDevelopmentBank.load_from_json()
            user_dect = {
                "id":"{}".format(self.user_id),
                "name":self.user_name,
                "birth":self.user_birth,
                "money":self.user_money,
                "nationality":self.user_nationality,
                "password":self.user_password,
                "requests":[],
                "settings":{
                    "theme":"light"
                }
            }
            data_dect[self.user_name+"#"+self.user_id] = user_dect
            data_dect["ids_list"].append(self.user_id)
            data_dect["names_list"].append(self.user_name)
            data_dect["births_list"].append(self.user_birth)
            data_dect["money_list"].append(self.user_money)
            data_dect["nationalitys_list"].append(self.user_nationality)
            data_dect["passwords_list"].append(self.user_password)
            IslamicDevelopmentBank.load_to_json(data_dect)
            main_window.unbind("<Return>")
            self.input_frame.destroy() 
        
        def log_in(user_index):
            IslamicDevelopmentBank().load_interface(user_index=user_index)
        def log_out(self,user_index):
            pass

        def load_btns(self):
            self.log_in_btn  = TK.Button(main_window,text="Log In",cursor="hand2",bg=IslamicDevelopmentBank.AppColors.LIGHT_BG,fg=IslamicDevelopmentBank.AppColors.LIGHT_FG,activebackground=IslamicDevelopmentBank.AppColors.LIGHT_BG_ACTV,activeforeground=IslamicDevelopmentBank.AppColors.LIGHT_FG,width=10,justify=TK.CENTER,relief=TK.FLAT,command=lambda:self.get_log_in_info(),font=("Arial Black",12,""));self.log_in_btn.place(x=325,y=175)
            self.sign_up_btn = TK.Button(main_window,text="Sign Up",cursor="hand2",bg=IslamicDevelopmentBank.AppColors.LIGHT_BG,fg=IslamicDevelopmentBank.AppColors.LIGHT_FG,activebackground=IslamicDevelopmentBank.AppColors.LIGHT_BG_ACTV,activeforeground=IslamicDevelopmentBank.AppColors.LIGHT_FG,width=10,justify=TK.CENTER,relief=TK.FLAT,command=lambda:self.get_sign_up_info(),font=("Arial Black",12,""));self.sign_up_btn.place(x=450,y=175)
        
        def get_sign_up_info(self):
            global logo_label
            self.input_frame = TK.Frame(main_window,bg=IslamicDevelopmentBank.AppColors.LIGHT_DID_BG,width=450,height=420);self.input_frame.place(x=220,y=30)
            logo_label = TK.Label(self.input_frame,image=logo_photo,bg="#FFFFFF");logo_label.place(x=120,y=5)

            comments_text = "1-  Enter Your triple name,\n2-  Enter Your birthday like*1990/10/23*,\n3-  Enter Your money amount,\n4-  Enter Your nationality *from where you are*,\n5-  Enter Your password and recommend a strong password."
            comments_label = TK.Label(self.input_frame,text=comments_text,bg=IslamicDevelopmentBank.AppColors.LIGHT_DID_BG,fg=IslamicDevelopmentBank.AppColors.DARK_DID_BG,justify=TK.LEFT,font=("Arial",7,""));comments_label.place(x=10,y=75)
            
            self.what_this_input = TK.Label(self.input_frame,text="1-Enter Your triple name.",bg=IslamicDevelopmentBank.AppColors.LIGHT_DID_BG,fg=IslamicDevelopmentBank.AppColors.DARK_DID_BG,justify=TK.CENTER,font=("Arial",10,""));self.what_this_input.place(x=40,y=200)
            self.steps_list = ["1-Enter Your triple name","2-Enter Enter Your birthday","3-Enter Enter Your money amount","4-Enter Enter Your nationality","5-Enter Enter password"]

            self.user_name_entry = TK.Entry(self.input_frame,bg=IslamicDevelopmentBank.AppColors.GRAY_DID_BG,fg=IslamicDevelopmentBank.AppColors.GRAY_FG,bd=1,relief=TK.GROOVE,width=25,font=("Arial Black",15,""));self.user_name_entry.place(x=40,y=225);self.user_name_entry.focus()
            self.user_birth_entry = TK.Entry(self.input_frame,bg=IslamicDevelopmentBank.AppColors.GRAY_DID_BG,fg=IslamicDevelopmentBank.AppColors.GRAY_FG,bd=1,relief=TK.GROOVE,width=25,font=("Arial Black",15,""));
            self.user_money_entry = TK.Entry(self.input_frame,bg=IslamicDevelopmentBank.AppColors.GRAY_DID_BG,fg=IslamicDevelopmentBank.AppColors.GRAY_FG,bd=1,relief=TK.GROOVE,width=25,font=("Arial Black",15,""));
            self.user_nationality_entry = TK.Entry(self.input_frame,bg=IslamicDevelopmentBank.AppColors.GRAY_DID_BG,fg=IslamicDevelopmentBank.AppColors.GRAY_FG,bd=1,relief=TK.GROOVE,width=25,font=("Arial Black",15,""));
            self.user_password_entry = TK.Entry(self.input_frame,bg=IslamicDevelopmentBank.AppColors.GRAY_DID_BG,fg=IslamicDevelopmentBank.AppColors.GRAY_FG,bd=1,relief=TK.GROOVE,width=25,font=("Arial Black",15,""));
            
            self.next_entry_btn = TK.Button(self.input_frame,text="Next ",cursor="hand2",bg=IslamicDevelopmentBank.AppColors.BLUE_BG,fg=IslamicDevelopmentBank.AppColors.LIGHT_FG,activebackground=IslamicDevelopmentBank.AppColors.BLUE_BG_ACTV,activeforeground=IslamicDevelopmentBank.AppColors.LIGHT_FG,width=10,justify=TK.CENTER,relief=TK.FLAT,command=lambda:self.next_entry_function(event=""),font=("Arial Black",12,""));self.next_entry_btn.place(x=315,y=365)
            self.cancel_btn = TK.Button(self.input_frame,text=" Cancel",cursor="hand2",bg=IslamicDevelopmentBank.AppColors.BLUE_BG,fg=IslamicDevelopmentBank.AppColors.LIGHT_FG,activebackground=IslamicDevelopmentBank.AppColors.BLUE_BG_ACTV,activeforeground=IslamicDevelopmentBank.AppColors.LIGHT_FG,width=10,justify=TK.CENTER,relief=TK.FLAT,command=lambda:self.cancel_sign_up_function(event=""),font=("Arial Black",12,""));self.cancel_btn.place(x=10,y=365)
            main_window.bind("<Return>",self.next_entry_function)
            self.entrys_list = [self.user_name_entry,self.user_birth_entry,self.user_money_entry,self.user_nationality_entry,self.user_password_entry]
            self.entry_number = 0
        def next_entry_function(self,event):
            if self.entry_number < 4:
                if self.entrys_list[self.entry_number].get() != "":
                    self.entry_number += 1
                    self.what_this_input.config(text=self.steps_list[self.entry_number])
                    self.entrys_list[self.entry_number].place(x=40,y=225)
                    self.entrys_list[self.entry_number].focus()
                if self.entry_number == 4:
                    self.next_entry_btn.config(text="Sign Up ",command=lambda:self.sign_up(self.user_name_entry.get(),self.user_birth_entry.get(),self.user_money_entry.get(),self.user_notionality_entry.get(),self.user_password_entry.get()))
            elif self.entry_number == 4:
                main_window.unbind("<Return>")
                main_window.bind("<Return>",self.sign_up(self.user_name_entry.get(),self.user_birth_entry.get(),self.user_money_entry.get(),self.user_notionality_entry.get(),self.user_password_entry.get()))
        def cancel_sign_up_function(self,event):
            self.input_frame.destroy() 

        def get_log_in_info(self):
            global logo_label
            self.input_frame = TK.Frame(main_window,bg=IslamicDevelopmentBank.AppColors.LIGHT_DID_BG,width=450,height=320);self.input_frame.place(x=220,y=50)
            logo_label = TK.Label(self.input_frame,image=logo_photo,bg="#FFFFFF");logo_label.place(x=120,y=5)

            comments_text = "1-  Enter user name,\n2-  Enter Your password."
            comments_label = TK.Label(self.input_frame,text=comments_text,bg=IslamicDevelopmentBank.AppColors.LIGHT_DID_BG,fg=IslamicDevelopmentBank.AppColors.DARK_DID_BG,justify=TK.LEFT,font=("Arial",7,""));comments_label.place(x=10,y=100)

            user_name_entry = TK.Entry(self.input_frame,bg=IslamicDevelopmentBank.AppColors.GRAY_DID_BG,fg=IslamicDevelopmentBank.AppColors.GRAY_FG,bd=1,relief=TK.GROOVE,width=25,font=("Arial Black",15,""));user_name_entry.place(x=40,y=180)
            user_password_entry = TK.Entry(self.input_frame,bg=IslamicDevelopmentBank.AppColors.GRAY_DID_BG,fg=IslamicDevelopmentBank.AppColors.GRAY_FG,bd=1,relief=TK.GROOVE,width=25,font=("Arial Black",15,""));user_password_entry.place(x=40,y=225)

            self.log_in_btn = TK.Button(self.input_frame,text="Log In ",cursor="hand2",bg=IslamicDevelopmentBank.AppColors.BLUE_BG,fg=IslamicDevelopmentBank.AppColors.LIGHT_FG,activebackground=IslamicDevelopmentBank.AppColors.BLUE_BG_ACTV,activeforeground=IslamicDevelopmentBank.AppColors.LIGHT_FG,width=10,justify=TK.CENTER,relief=TK.FLAT,command=lambda:self.verify_inputs(name=user_name_entry.get(),password=user_password_entry.get(),event=""),font=("Arial Black",12,""));self.log_in_btn.place(x=315,y=275)
            self.cancel_btn = TK.Button(self.input_frame,text=" Cancel",cursor="hand2",bg=IslamicDevelopmentBank.AppColors.BLUE_BG,fg=IslamicDevelopmentBank.AppColors.LIGHT_FG,activebackground=IslamicDevelopmentBank.AppColors.BLUE_BG_ACTV,activeforeground=IslamicDevelopmentBank.AppColors.LIGHT_FG,width=10,justify=TK.CENTER,relief=TK.FLAT,command=lambda:self.cancel_log_in_function(event=""),font=("Arial Black",12,""));self.cancel_btn.place(x=10,y=275)        
            main_window.bind("Return",self.verify_inputs)
        def verify_inputs(self,name,password,event):
            data_dect = IslamicDevelopmentBank.load_from_json()
            if name in data_dect["names_list"]:
                index = 0
                for i in data_dect["names_list"]:
                    if i == name:
                        break
                    index += 1
                if password == data_dect["passwords_list"][index]:
                    self.log_in(index)
        def cancel_log_in_function(self,event):
            self.input_frame.destroy() 


    def load_from_json():
        with open(FILE_PATH+FILE_NAME,"r") as file:
            data_dect = J.load(file)
        return data_dect
    
    def load_to_json(data):
        with open(FILE_PATH+FILE_NAME,"w") as file:
            variable = J.dump(data,file,indent=4)

    def show_user_infos(self,user_index):
        data_dect = IslamicDevelopmentBank.load_from_json()
        user_object_path = data_dect[data_dect["names_list"][user_index]+"#"+data_dect["ids_list"][user_index]]
        info_birth = "\nBirth: {}\n".format(user_object_path["birth"],)
        info_money = "\nMoney: {}\n".format(user_object_path["money"],)
        info_nationality = "\nNationality: {}\n".format(user_object_path["nationality"],)
        info_password = "\nPassword: {}".format("*********",)
        self.show_frame = TK.Frame(main_window,bg=self.AppColors.LIGHT_DID_BG,width=680,height=400);self.show_frame.place(x=10,y=75)
        self.name_label = TK.Label(self.show_frame,text=user_object_path["name"],bg=IslamicDevelopmentBank.AppColors.LIGHT_DID_BG,fg=IslamicDevelopmentBank.AppColors.DARK_DID_BG,font=("Arial",15,"bold"));self.name_label.place(x=25,y=50)
        self.infos_textura = TK.Listbox(self.show_frame,bd=0,bg=IslamicDevelopmentBank.AppColors.LIGHT_DID_BG,fg=IslamicDevelopmentBank.AppColors.DARK_DID_BG,width=75,height=7,font=("Arial",10,""));self.infos_textura.place(x=50,y=100)
        self.infos_textura.insert(TK.END,info_birth)
        self.infos_textura.insert(TK.END,info_money)
        self.infos_textura.insert(TK.END,info_nationality)
        self.infos_textura.insert(TK.END,info_password)
        self.infos_textura.insert(TK.END," ")
        self.infos_textura.insert(TK.END,"Join Date: {}".format())
        self.infos_textura.config(state=TK.DISABLED)
        show_password_btn = TK.Button(self.show_frame,text="Show password ",cursor="hand2",bg=IslamicDevelopmentBank.AppColors.LIGHT_BG,fg=IslamicDevelopmentBank.AppColors.LIGHT_FG,activebackground=IslamicDevelopmentBank.AppColors.LIGHT_BG_ACTV,activeforeground=IslamicDevelopmentBank.AppColors.LIGHT_FG,justify=TK.CENTER,relief=TK.GROOVE,command=lambda:IslamicDevelopmentBank().show_user_password(user_index,self.infos_textura),font=("Arial Black",10,""));show_password_btn.place(x=10,y=250)
    def show_user_password(self,user_index,textura):
        self.infos_textura = textura
        data_dect = IslamicDevelopmentBank.load_from_json()
        user_object_path = data_dect[data_dect["names_list"][user_index]+"#"+data_dect["ids_list"][user_index]]
        info_birth = "\nBirth: {}\n".format(user_object_path["birth"],)
        info_money = "\nMoney: {}\n".format(user_object_path["money"],)
        info_nationality = "\nNationality: {}\n".format(user_object_path["nationality"],)
        info_password = "\nPassword: {}".format(user_object_path["password"],)
        self.infos_textura.config(state=TK.NORMAL)
        self.infos_textura.delete(0,"end")#promlem
        self.infos_textura.insert(TK.END,info_birth)
        self.infos_textura.insert(TK.END,info_money)
        self.infos_textura.insert(TK.END,info_nationality)
        self.infos_textura.insert(TK.END,info_password)
        self.infos_textura.config(state=TK.DISABLED)
    def send_request(self,user_index):
        self.show_frame = TK.Frame(main_window,bg=self.AppColors.LIGHT_DID_BG,width=680,height=400);self.show_frame.place(x=10,y=75)
    def show_request_history(self,user_index):
        self.show_frame = TK.Frame(main_window,bg=self.AppColors.LIGHT_DID_BG,width=680,height=400);self.show_frame.place(x=10,y=75)
    def about_developer(self):
        self.show_frame = TK.Frame(main_window,bg=self.AppColors.LIGHT_DID_BG,width=680,height=400);self.show_frame.place(x=10,y=75)

    def load_interface(self,user_index):
        try:
            global logo_label
            logo_label.destroy()
        except:
            pass
        global logo_photo
        logo_label = TK.Label(main_window,image=logo_photo,bg="#F0F0F0");logo_label.place(x=265,y=0)

        self.menu_frame = TK.Frame(main_window,bg=self.AppColors.LIGHT_BG,width=200,height=1500);self.menu_frame.place(x=700,y=0)
        self.show_frame = TK.Frame(main_window,bg=self.AppColors.LIGHT_DID_BG,width=680,height=400);self.show_frame.place(x=10,y=75)

        show_user_info_btn = TK.Button(self.menu_frame,text=" Show Your INFOs",padx=22,pady=5,cursor="hand2",bg=IslamicDevelopmentBank.AppColors.LIGHT_BG,fg=IslamicDevelopmentBank.AppColors.LIGHT_FG,activebackground=IslamicDevelopmentBank.AppColors.LIGHT_BG_ACTV,activeforeground=IslamicDevelopmentBank.AppColors.LIGHT_FG,justify=TK.CENTER,relief=TK.GROOVE,command=lambda:IslamicDevelopmentBank().show_user_infos(user_index),font=("Arial Black",10,""));show_user_info_btn.place(x=0,y=150)
        get_request_btn = TK.Button(self.menu_frame,text=" Send Request",padx=42,pady=5,cursor="hand2",bg=IslamicDevelopmentBank.AppColors.LIGHT_BG,fg=IslamicDevelopmentBank.AppColors.LIGHT_FG,activebackground=IslamicDevelopmentBank.AppColors.LIGHT_BG_ACTV,activeforeground=IslamicDevelopmentBank.AppColors.LIGHT_FG,justify=TK.CENTER,relief=TK.GROOVE,command=lambda:IslamicDevelopmentBank().send_request(user_index),font=("Arial Black",10,""));get_request_btn.place(x=0,y=190)
        buy_history_btn = TK.Button(self.menu_frame,text=" Request History",padx=33,pady=5,cursor="hand2",bg=IslamicDevelopmentBank.AppColors.LIGHT_BG,fg=IslamicDevelopmentBank.AppColors.LIGHT_FG,activebackground=IslamicDevelopmentBank.AppColors.LIGHT_BG_ACTV,activeforeground=IslamicDevelopmentBank.AppColors.LIGHT_FG,justify=TK.CENTER,relief=TK.GROOVE,command=lambda:IslamicDevelopmentBank().show_request_history,font=("Arial Black",10,""));buy_history_btn.place(x=0,y=230)
        log_out_btn = TK.Button(self.menu_frame,text=" Log out",padx=57,pady=5,cursor="hand2",bg=IslamicDevelopmentBank.AppColors.LIGHT_BG,fg=IslamicDevelopmentBank.AppColors.LIGHT_FG,activebackground=IslamicDevelopmentBank.AppColors.LIGHT_BG_ACTV,activeforeground=IslamicDevelopmentBank.AppColors.LIGHT_FG,justify=TK.CENTER,relief=TK.GROOVE,command=lambda:IslamicDevelopmentBank.LogInSignUp().log_out(user_index),font=("Arial Black",10,""));log_out_btn.place(x=0,y=270)
        about_btn = TK.Button(self.menu_frame,text=" About",padx=63,pady=5,cursor="hand2",bg=IslamicDevelopmentBank.AppColors.LIGHT_BG,fg=IslamicDevelopmentBank.AppColors.LIGHT_FG,activebackground=IslamicDevelopmentBank.AppColors.LIGHT_BG_ACTV,activeforeground=IslamicDevelopmentBank.AppColors.LIGHT_FG,justify=TK.CENTER,relief=TK.GROOVE,command=lambda:IslamicDevelopmentBank().about_developer(),font=("Arial Black",10,""));about_btn.place(x=0,y=310)
        settings_btn = TK.Button(self.menu_frame,text=" Settings",padx=55,pady=5,cursor="hand2",bg=IslamicDevelopmentBank.AppColors.LIGHT_BG,fg=IslamicDevelopmentBank.AppColors.LIGHT_FG,activebackground=IslamicDevelopmentBank.AppColors.LIGHT_BG_ACTV,activeforeground=IslamicDevelopmentBank.AppColors.LIGHT_FG,justify=TK.CENTER,relief=TK.GROOVE,font=("Arial Black",10,""));settings_btn.place(x=0,y=460)
        
IslamicDevelopmentBank().load_interface(1)

main_window.mainloop()