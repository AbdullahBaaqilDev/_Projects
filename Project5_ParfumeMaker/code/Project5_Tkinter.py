"""from tkinter import *
from tkinter import messagebox
import random

app = Tk()
app.title("Parfumes-Maker")
app.geometry("700x400+150+100")
app.resizable(True,False)


clear_text = ""
for i in range(125):
    for i in range(125):
        clear_text += "                                                                     "
    clear_text += "\n"

class ParfumeMaker():
    def clear_all(self):
        clear = Label(app,
        text=clear_text,
        font=("",14,"")
        );clear.place(x=0,y=45)
    def __init__(self):
        self.clear_all()
        self.par_n = Entry(app,justify=CENTER,relief=RAISED,width = 9,font=("Calibri",14,""));self.par_n.place(x=100,y=100)
        TEXT = Label(app,text="Name:",font=("Gill Sans",14,""));TEXT.place(x=0,y=100)
        self.par_q = Entry(app,justify=CENTER,relief=RAISED,width = 9,font=("Gill Sans",14,""));self.par_q.place(x=100,y=170)
        TEXT = Label(app,text="Quntity:",font=("Gill Sans",14,""));TEXT.place(x=0,y=170)
        self.par_s = Entry(app,justify=CENTER,relief=RAISED,width = 9,font=("Gill Sans",14,""));self.par_s.place(x=100,y=200)
        TEXT = Label(app,text="Size:",font=("Gill Sans",14,""));TEXT.place(x=0,y=200)

        self.water_p = Entry(app,justify=CENTER,relief=RAISED,width = 9,font=("Gill Sans",14,""));self.water_p.place(x=300,y=100)
        TEXT = Label(app,text="Water P:",font=("Gill Sans",14,""));TEXT.place(x=220,y=100)
        self.oil_p = Entry(app,justify=CENTER,relief=RAISED,width = 9,font=("Gill Sans",14,""));self.oil_p.place(x=300,y=150)
        TEXT = Label(app,text="Oil P:",font=("Gill Sans",14,""));TEXT.place(x=245,y=150)
        self.ethanol_p = Entry(app,justify=CENTER,relief=RAISED,width = 9,font=("Gill Sans",14,""));self.ethanol_p.place(x=300,y=200)
        TEXT = Label(app,text="Ethanol P:",font=("Gill Sans",14,""));TEXT.place(x=205,y=200)
        def cal_enter(m):
            cal["background"] = "#80C761"
        def cal_leave(m):
            cal["background"] ="#9DF578"
        cal = Button(app,
        text = "Calculate the res",
        bg = "#9DF578",
        fg = "#242424",
        activebackground = "#6BA651",
        activeforeground = "#242424",
        command = lambda: self.calculate_func(),
        font = ("Gill Sans",
        12,
        "",
        )
        );cal.place(x=10,y=350)
        cal.bind("<Enter>",cal_enter)
        cal.bind("<Leave>",cal_leave)
        def cancel_enter(m):
            cancel["background"] = "#C73A3A"
        def cancel_leave(m):
            cancel["background"] ="#E84343"
        cancel = Button(app,
        text = "Cancel",
        bg = "#E84343",
        fg = "#242424",
        activebackground = "#A63030",
        activeforeground = "#242424",
        command = lambda: self.clear_all(),
        font = ("Gill Sans",
        12,
        "",
        )
        );cancel.place(x=150,y=350)
        cancel.bind("<Enter>",cancel_enter)
        cancel.bind("<Leave>",cancel_leave)
    def calculate_func(self):
        try:
            self.oil_l = (float(self.par_q.get())*float(self.par_s.get())/100*float(self.oil_p.get()))/1000
            self.water_l = (float(self.par_q.get())*float(self.par_s.get())/100*float(self.water_p.get()))/1000
            self.ethanol_l = (float(self.par_q.get())*float(self.par_s.get())/100*float(self.ethanol_p.get()))/1000

            self.oil_weight = (self.oil_l*oil_s)
            self.water_weight = (self.water_l*water_s)
            self.ethanol_weight = (self.ethanol_l*ethanol_s)

            self.perc = int(self.oil_p.get())+int(self.water_p.get())+int(self.ethanol_p.get())
            self.l_a = self.oil_l + self.water_l + self.ethanol_l
            self.weight_a = self.oil_weight + self.water_weight + self.ethanol_weight
            if self.perc == 100:
                self.show_res()
            else:
                erorr = messagebox.showerror("Erorr","'make sure the water p, oil p and ethanol p equals %100'")
        except:
            erorr = messagebox.showerror("Erorr","You must fill all inputs correctly\n'if you did that make sure the water p and oil p and ethanol p equals %100'")
    def show_res(self):
        self.clear_all()
        title_size = Label(app,text = "______|السعة|______",font=("Gill Sans",16,"bold"));title_size.place(x=0,y=50)
        show_water_l = Label(app,text="الماء باللترات= {}".format(str(self.water_l)),font=("Calibri"));show_water_l.place(x=0,y=80)
        show_oil_l = Label(app,text="الزيت باللترات= {}".format(str(self.oil_l)),font=("Calibri"));show_oil_l.place(x=0,y=105)
        show_ethanol_l = Label(app,text="الإثانول باللترات= {}".format(str(self.ethanol_l)),font=("Calibri"));show_ethanol_l.place(x=0,y=130)

        title_weight = Label(app,text = "______|الوزن كجم|______",font=("Gill Sans",16,"bold"));title_weight.place(x=250,y=50)
        show_water_weight = Label(app,text="الماء بالكيلو= {}".format(str(self.water_weight)),font=("Calibri"));show_water_weight.place(x=250,y=80)
        show_oil_weight = Label(app,text="الزيت بالكيلو= {}".format(str(self.oil_weight)),font=("Calibri"));show_oil_weight.place(x=250,y=105)
        show_ethanol_weight = Label(app,text="الإثانول بالكيلو= {}".format(str(self.ethanol_weight)),font=("Calibri"));show_ethanol_weight.place(x=250,y=130)

        title_w = Label(app,text = "______|الاجمالي|______",font=("Calibri",16,"bold"));title_w.place(x=500,y=50)
        show_water_w = Label(app,text="اجمالي النسب= {}".format(str(self.perc)),font=("Calibri"));show_water_w.place(x=500,y=80)
        show_oil_w = Label(app,text="اجمالي اللترات= {}".format(str(self.l_a)),font=("Calibri"));show_oil_w.place(x=500,y=105)
        show_ethanol_w = Label(app,text="اجمالي الوزن= {}".format(str(self.weight_a)),font=("Calibri"));show_ethanol_w.place(x=500,y=130)
        def clear_enter(m):
            clear_btn["background"] = "#C73A3A"
        def clear_leave(m):
            clear_btn["background"] ="#E84343"
        clear_btn = Button(app,
        text = "Clear",
        bg = "#E84343",
        fg = "#242424",
        activebackground = "#A63030",
        activeforeground = "#242424",
        command = lambda: self.clear_all(),
        font = ("Gill Sans",
        12,
        "",
        )
        );clear_btn.place(x=10,y=350)
        clear_btn.bind("<Enter>",clear_enter)
        clear_btn.bind("<Leave>",clear_leave)

def start_promgram():
    App = ParfumeMaker()
def make_enter(m):
    make_par["background"] = "#B5B5B5"
def make_leave(m):
    make_par["background"] = "#D6D6D6"
make_par = Button(app,
text = "Make a Parfume",
bg = "#D6D6D6",
fg = "#474747",
activebackground = "#999999",
activeforeground = "#474747",
command = lambda: start_promgram(),
font = ("Gill Sans",
14,
"",
)
);make_par.pack()
make_par.bind("<Enter>",make_enter)
make_par.bind("<Leave>",make_leave)
app.mainloop()
"""

water_s = 1
oil_s = 0.925
ethanol_s = 0.789

name = input("Parfume Name: ")
print("------------------")
how_par = input("Parfume Quntity: ")
print("------------------")
size = input("Parfume Size: ")
print("------------------")
water_p = input("Parfume water %")
print("------------------")
oil_p = input("Parfume oil %")
print("------------------")
ethanol_p = input("Parfume ethanol %")

oil_l = (float(how_par)*float(size)/100*float(oil_p))/1000
water_l = (float(how_par)*float(size)/100*float(water_p))/1000
ethanol_l = (float(how_par)*float(size)/100*float(ethanol_p))/1000

oil_g = (oil_l*oil_s)
water_g = (water_l*water_s)
ethanol_g = (ethanol_l*ethanol_s)

perc = int(oil_p)+int(water_p)+int(ethanol_p)
l_a = oil_l+water_l+ethanol_l
g_a = oil_g+water_g+ethanol_g

print("----------|Sizes|-------------")
print("oil size = "+str(oil_l))
print("water size = "+str(water_l))
print("ethanol size = "+str(ethanol_l))

print("------------|KG|--------------")
print("oil KG = "+str(oil_g))
print("water KG = "+str(water_g))
print("ethanol KG = "+str(ethanol_g))

print("----------|ALL|---------------")
print("percent = "+str(perc))
print("Size = "+str(l_a))
print("KG = "+str(g_a))
print("Name = {}".format(name))
