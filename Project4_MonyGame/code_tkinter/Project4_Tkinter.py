#Mad with abodi2098
#-----------------------|
from tkinter import *
from tkinter import messagebox

app =Tk()
app.title("Mony-Game                           by abodi2098")
app.geometry("400x400")
app.resizable(False,False)
app.config(background="#2E2E2E")


#------------------
up1_color = "#FF2E2E"
up1_color_hover = "#E82A2A"
up1_color_actv = "#BF2222"
up1_price = 25
#------------------
up2_color = "#FF2E2E"
up2_color_hover = "#E82A2A"
up2_color_actv = "#BF2222"
up2_price = 255
#------------------
up3_color = "#FF2E2E"
up3_color_hover = "#E82A2A"
up3_color_actv = "#BF2222"
up3_price = 845
#------------------
up4_color = "#FF2E2E"
up4_color_hover = "#E82A2A"
up4_color_actv = "#BF2222"
up4_price = 1760
#------------------
up5_color = "#FF2E2E"
up5_color_hover = "#E82A2A"
up5_color_actv = "#BF2222"
up5_price = 8760
#------------------

class MoneyGame:
    class UpgradsClass:
        def __init__(self):
            self.ups = Tk()
            self.ups.title("Upgrads")
            self.ups.geometry("300x400+150+200")
            self.ups.resizable(False,False)
            self.ups.config(bg="#2E2E2E")
            global up1_price;global up1_color;global up1_color_hover;global up1_color_actv
            global up2_price;global up2_color;global up2_color_hover;global up2_color_actv
            global up3_price;global up3_color;global up3_color_hover;global up3_color_actv
            global up4_price;global up4_color;global up4_color_hover;global up4_color_actv
            global up5_price;global up5_color;global up5_color_hover;global up5_color_actv
            if App.money >= up1_price :up1_color = "#2AD927";up1_color_hover = "#25BF22";up1_color_actv = "#21A81E"
            else:up1_color = "#FF2E2E";up1_color_hover = "#E82A2A";up1_color_actv = "#BF2222"
            if App.money >= up2_price :up2_color = "#2AD927";up2_color_hover = "#25BF22";up2_color_actv = "#21A81E"
            else:up2_color = "#FF2E2E";up2_color_hover = "#E82A2A";up2_color_actv = "#BF2222"
            if App.up3_active == False:
                if App.money >= up3_price :up3_color = "#2AD927";up3_color_hover = "#25BF22";up3_color_actv = "#21A81E"
                else:up3_color = "#FF2E2E";up3_color_hover = "#E82A2A";up3_color_actv = "#BF2222"
            if App.up4_active == False:
                if App.money >= up4_price :up4_color = "#2AD927";up4_color_hover = "#25BF22";up4_color_actv = "#21A81E"
                else:up4_color = "#FF2E2E";up4_color_hover = "#E82A2A";up4_color_actv = "#BF2222"
            if App.up5_active == False:
                if App.money >= up5_price :up5_color = "#2AD927";up5_color_hover = "#25BF22";up5_color_actv = "#21A81E"
                else:up5_color = "#FF2E2E";up5_color_hover = "#E82A2A";up5_color_actv = "#BF2222"
            def up1_enter(m):
                self.up1_btn["background"] = up1_color_hover
            def up1_leave(m):
                self.up1_btn["background"] = up1_color
            self.up1_btn = Button(self.ups,text="Money(×2)",bg=up1_color,fg="#FFFFFF",
            activebackground=up1_color_actv,activeforeground="#FFFFFF",command=lambda:self.up1_func(),
            relief=GROOVE,font=("Gill Sans",12,"bold"));self.up1_btn.place(x=20,y=25)
            self.up1_btn.bind("<Enter>",up1_enter)
            self.up1_btn.bind("<Leave>",up1_leave)
            self.show_up1_sell = Label(self.ups,text=str(up1_price)+"$",bg=up1_color,fg="#FFFFFF",
            relief=GROOVE,font=("Gill Sans",12,"bold"));self.show_up1_sell.place(x=200,y=25)
            self.show_up1_how_buy = Label(self.ups,text=str(App.up1_how_buy),bg="#2E2E2E",fg="#FFFFFF",
            relief=GROOVE,font=("Gill Sans",12,"bold"));self.show_up1_how_buy.place(x=175,y=25)
            def up2_enter(m):
                self.up2_btn["background"] = up2_color_hover
            def up2_leave(m):
                self.up2_btn["background"] = up2_color
            self.up2_btn = Button(self.ups,text="clicks(×2)",bg=up2_color,fg="#FFFFFF",
            activebackground=up2_color_actv,activeforeground="#FFFFFF",command=lambda:self.up2_func(),
            relief=GROOVE,font=("Gill Sans",12,"bold"));self.up2_btn.place(x=20,y=75)
            self.up2_btn.bind("<Enter>",up2_enter)
            self.up2_btn.bind("<Leave>",up2_leave)
            self.show_up2_sell = Label(self.ups,text=str(up2_price)+"$",bg=up2_color,fg="#FFFFFF",
            relief=GROOVE,font=("Gill Sans",12,"bold"));self.show_up2_sell.place(x=200,y=75)
            self.show_up2_how_buy = Label(self.ups,text=str(App.up2_how_buy),bg="#2E2E2E",fg="#FFFFFF",
            relief=GROOVE,font=("Gill Sans",12,"bold"));self.show_up2_how_buy.place(x=175,y=75)
            def up3_enter(m):
                self.up3_btn["background"] = up3_color_hover
            def up3_leave(m):
                self.up3_btn["background"] = up3_color
            self.up3_btn = Button(self.ups,text="BUF",bg=up3_color,fg="#FFFFFF",
            activebackground=up3_color_actv,activeforeground="#FFFFFF",command=lambda:self.up3_func(),
            relief=GROOVE,font=("Gill Sans",12,"bold"));self.up3_btn.place(x=20,y=125)
            self.up3_btn.bind("<Enter>",up3_enter)
            self.up3_btn.bind("<Leave>",up3_leave)
            self.show_up3_sell = Label(self.ups,text=str(up3_price)+"$",bg=up3_color,fg="#FFFFFF",
            relief=GROOVE,font=("Gill Sans",12,"bold"));self.show_up3_sell.place(x=200,y=125)
            def up4_enter(m):
                self.up4_btn["background"] = up4_color_hover
            def up4_leave(m):
                self.up4_btn["background"] = up4_color
            self.up4_btn = Button(self.ups,text="No Clicks",bg=up4_color,fg="#FFFFFF",
            activebackground=up4_color_actv,activeforeground="#FFFFFF",command=lambda:self.up4_func(),
            relief=GROOVE,font=("Gill Sans",12,"bold"));self.up4_btn.place(x=20,y=175)
            self.up4_btn.bind("<Enter>",up4_enter)
            self.up4_btn.bind("<Leave>",up4_leave)
            self.show_up4_sell = Label(self.ups,text=str(up4_price)+"$",bg=up4_color,fg="#FFFFFF",
            relief=GROOVE,font=("Gill Sans",12,"bold"));self.show_up4_sell.place(x=200,y=175)
            def up5_enter(m):
                self.up5_btn["background"] = up5_color_hover
            def up5_leave(m):
                self.up5_btn["background"] = up5_color
            self.up5_btn = Button(self.ups,text="Super BUF",bg=up5_color,fg="#FFFFFF",
            activebackground=up5_color_actv,activeforeground="#FFFFFF",command=lambda:self.up5_func(),
            relief=GROOVE,font=("Gill Sans",12,"bold"));self.up5_btn.place(x=20,y=225)
            self.up5_btn.bind("<Enter>",up5_enter)
            self.up5_btn.bind("<Leave>",up5_leave)
            self.show_up5_sell = Label(self.ups,text=str(up5_price)+"$",bg=up5_color,fg="#FFFFFF",
            relief=GROOVE,font=("Gill Sans",12,"bold"));self.show_up5_sell.place(x=200,y=225)
            def super_enter(m):
                super_up_btn["background"] = "#BA50BF"
            def super_leave(m):
                super_up_btn["background"] = "#DA5EE0"
            super_up_btn = Button(self.ups,text="Super Upgrad  $25000",bg="#DA5EE0",fg="#FFFFFF",
            activebackground="#A648AB",activeforeground="#FFFFFF",command=lambda:self.super_up_func(),
            relief=GROOVE,font=("Algerian",14,"bold"));super_up_btn.place(x=20,y=275)
            super_up_btn.bind("<Enter>",super_enter)
            super_up_btn.bind("<Leave>",super_leave)
            self.check_color()
        def func_pass(self):
            pass
        def check_color(self):
            global up1_price;global up1_color;global up1_color_hover;global up1_color_actv
            global up2_price;global up2_color;global up2_color_hover;global up2_color_actv
            global up3_price;global up3_color;global up3_color_hover;global up3_color_actv
            global up4_price;global up4_color;global up4_color_hover;global up4_color_actv
            global up5_price;global up5_color;global up5_color_hover;global up5_color_actv
            if App.money >= up1_price :up1_color = "#2AD927";up1_color_hover = "#25BF22";up1_color_actv = "#21A81E"
            else:up1_color = "#FF2E2E";up1_color_hover = "#E82A2A";up1_color_actv = "#BF2222"
            self.up1_btn.config(bg=up1_color,activebackground=up1_color_actv)
            self.show_up1_sell.config(bg=up1_color)
            self.show_up1_how_buy.config(text=App.up1_how_buy)
            if App.money >= up2_price :up2_color = "#2AD927";up2_color_hover = "#25BF22";up2_color_actv = "#21A81E"
            else:up2_color = "#FF2E2E";up2_color_hover = "#E82A2A";up2_color_actv = "#BF2222"
            self.up2_btn.config(bg=up2_color,activebackground=up2_color_actv)
            self.show_up2_sell.config(bg=up2_color)
            self.show_up2_how_buy.config(text=App.up2_how_buy)
            if App.up3_active == False:
                if App.money >= up3_price :up3_color = "#2AD927";up3_color_hover = "#25BF22";up3_color_actv = "#21A81E"
                else:up3_color = "#FF2E2E";up3_color_hover = "#E82A2A";up3_color_actv = "#BF2222"
            else:self.up3_btn.config(bg="#787878");up3_color_hover = "#787878";up3_color = "#787878";self.up3_btn.config(activebackground="#787878");self.show_up3_sell.config(text="bought");self.up3_btn.config(command=self.func_pass)
            self.up3_btn.config(bg=up3_color,activebackground=up3_color_actv)
            self.show_up3_sell.config(bg=up3_color)
            
            if App.up4_active == False:
                if App.money >= up4_price :up4_color = "#2AD927";up4_color_hover = "#25BF22";up4_color_actv = "#21A81E"
                else:up4_color = "#FF2E2E";up4_color_hover = "#E82A2A";up4_color_actv = "#BF2222"
            else:self.up4_btn.config(bg="#787878");up4_color="#787878";up4_color_hover = "#787878";up4_color = "#787878";self.up4_btn.config(activebackground="#787878");self.show_up4_sell.config(text="bought");self.up4_btn.config(command=self.func_pass)
            self.up4_btn.config(bg=up4_color,activebackground=up4_color_actv)
            self.show_up4_sell.config(bg=up4_color)

            if App.up5_active == False:
                if App.money >= up5_price :up5_color = "#2AD927";up5_color_hover = "#25BF22";up5_color_actv = "#21A81E"
                else:up5_color = "#FF2E2E";up5_color_hover = "#E82A2A";up5_color_actv = "#BF2222"
            else:self.up5_btn.config(bg="#787878");up5_color_hover = "#787878";up5_color = "#787878";self.up5_btn.config(activebackground="#787878");self.show_up5_sell.config(text="bought");self.up5_btn.config(command=self.func_pass)
            self.up5_btn.config(bg=up5_color,activebackground=up5_color_actv)
            self.show_up5_sell.config(bg=up5_color)


        def up1_func(self):
            global up1_price;global up1_color;global up1_color_hover;global up1_color_actv
            if App.money >= up1_price:
                App.money_add *= 2
                App.up1_how_buy += 1
                App.money -= up1_price
                up1_price *= 1.65
                #____________________________
                up1_price *= 2 ; up1_price //=2
                App.show_money.config(text = App.money)
                self.show_up1_sell.config(text=str(up1_price)+"$")
                self.check_color()
            elif App.money < up5_price:messagebox.showerror("no money","You do not have money\nhhhh you are boor")



        def up2_func(self):
            global up2_price;global up2_color;global up2_color_hover;global up2_color_actv
            if App.money >= up2_price:
                App.clicks_add *= 2
                App.up2_how_buy += 1
                App.money -= up2_price
                App.show_money.config(text=App.money)
                up2_price *= 2.50
                #___________________________
                up2_price *= 2;up2_price //= 2
                self.show_up2_sell.config(text=str(up2_price)+"$")
                self.check_color()
            elif App.money < up5_price:messagebox.showerror("no money","You do not have money\nhhhh you are boor")
        

        def up3_func(self):
            global up3_price;global up3_color;global up3_color_hover;global up3_color_actv
            if App.money >= up3_price:
                def buf_func():
                    if App.clicks >= 50:
                        def more_time():
                            App.show_money.config(text=str(App.money))
                        for i in range(App.buf_power):
                            App.money += App.money_add
                            app.after(50,more_time)
                        App.clicks -= 50
                        App.show_clicks.config(text=App.clicks)
                self.buf = Button(app,text="BUF",bg="#FF2B2B",fg="#FFFFFF",
                activebackground="#BF2121",activeforeground="#FFFFFF",command=lambda:buf_func(),
                relief=GROOVE,width=12,height=1,pady=2,font=("Gill Sans",10,"bold"));self.buf.place(x=180,y=100)
                App.money -= up3_price
                App.show_money.config(text=App.money)
                App.up3_active = True
                self.check_color()
                messagebox.showinfo("Read Me","BUF, you need 50 click to use 'BUF'\t\t\t\t\t\t\nHow much of money does 'BUF' give you:\n\tBUF button press 'Get Money$$' 20 times\n\t'Super BUF' button press 'Get Money' 50 times")
            elif App.money < up5_price:messagebox.showerror("no money","You do not have money\nhhhh you are boor")

        def up4_func(self):
            global up4_price;global up4_color;global up4_color_hover;global up4_color_actv
            if App.money >= up4_price:
                self.up4_btn.config(command=self.func_pass)
                App.money -= up4_price
                App.show_money.config(text=App.money)
                App.money_btn.bind("<Enter>",App.func_add)
                self.up4_active = True
                up4_color_hover = "#787878";up4_color = "#787878";
                self.up4_btn.config(bg=up4_color)
                self.up4_btn.config(activebackground="#787878");
                self.show_up4_sell.config(text="bought");
                self.up4_btn.config(command=self.func_pass)
                self.up4_btn.config(bg=up4_color,activebackground=up4_color_actv)
                self.show_up4_sell.config(bg=up4_color)
                self.check_color()
            elif App.money < up4_price:messagebox.showerror("no money","You do not have money\nhhhh you are boor")


        def up5_func(self):
            global up5_price;global up5_color;global up5_color_hover;global up5_color_actv
            if App.money >= up5_price and App.up3_active == True:
                self.buf.config(text="Super BUF")
                self.power_buf = 50
                App.money -= up5_price
                self.up5_active = True
                self.check_color()
            elif App.money < up5_price:messagebox.showerror("no money","You do not have money\nhhhh you are boor")
            if App.up3_active == False:
                messagebox.showinfo("can not buy that","You can not buy 'Super BUF'\nbecuse you did not buy 'BUF'")


        def super_up_func(self):
            if self.money >= 25000:
                self.money = 999999999999
                App.show_money.config(text="Press 'Get Money$$'")
                self.ups.destroy()
                messagebox.showinfo("You Won","WOOOOOOOOOOOOOOOW,You are the king of Money-Game")
                win = Label(app,
                text="You Win",
                bg = "#2E2E2E",
                fg = "#FFFFFF",
                font=("Algerian",25,"bold"));win.place(x=140,y=200)
    def __init__(self,money_start,clicks_start,money_add_start,clicks_add_start):
        self.money = money_start# لاني كسول
        self.clicks = clicks_start# لاني كسول2
        self.money_add = money_add_start
        self.clicks_add = clicks_add_start
        self.buf_power = 20
        self.up1_how_buy = 0
        self.up2_how_buy = 0
        self.up3_active = False
        self.up4_active = False
        self.up5_active = False
        self.gray_frame = Frame(app,bg = "#6E6E6E",width=400,height=75);self.gray_frame.place(x=0,y=25)
        TXT = Label(self.gray_frame,text = "Money:-",bg = "#6E6E6E",fg = "#FFFFFF",font = ("Gill Sans",14,"bold"));TXT.place(x=0,y=15)
        self.show_money = Label(self.gray_frame,text=str(self.money),bg="#6e6e6e",fg="#81FF3D",font=("Gill Sans",14,"bold"));self.show_money.place(x=90,y=15)
        TXT = Label(self.gray_frame,text = "Clicks:-",bg = "#6E6E6E",fg = "#FFFFFF",font = ("Gill Sans",12,"bold"));TXT.place(x=0,y=45)
        self.show_clicks = Label(self.gray_frame,text=str(self.clicks),bg="#6e6e6e",fg="#F7DF00",font=("Gill Sans",12,"bold"));self.show_clicks.place(x=70,y=45)
        def mny_enter(m):
            if self.up4_active == True:
                self.func_add()
                self.money_btn["background"] = "#51A127"
            else:
                self.money_btn["background"] = "#51A127"
        def mny_leave(m):
            self.money_btn["background"] = "#5EBA2D"
        self.money_btn = Button(app,text = "Get Money$$",bg = "#5EBA2D",fg = "#FFFFFF",activebackground="#41801F",activeforeground="#FFFFFF",relief=GROOVE,width=20,height=1,pady=2,command=lambda: self.func_add(event=""),font=("Gill Sans",10,"bold"));self.money_btn.place(x=4,y=100)
        self.money_btn.bind("<Enter>",mny_enter)
        self.money_btn.bind("<Leave>",mny_leave)
        self.up_btn = Button(app,text = "Upgrads",bg ="#7D7D7D",fg="#FFFFFF",activebackground="#545454",activeforeground="#FFFFFF",relief=GROOVE,width=12,height=1,pady=2,command=lambda: App.UpgradsClass(),font=("Gill Sans",10,"bold"));self.up_btn.place(x=290,y=100)


    def func_add(self,event):
        self.money += self.money_add
        self.show_money.config(text=str(self.money))
        self.clicks += self.clicks_add
        self.show_clicks.config(text=str(self.clicks))
App = MoneyGame(money_start=25000.0,clicks_start=500,money_add_start=1,clicks_add_start=1)
app.mainloop()