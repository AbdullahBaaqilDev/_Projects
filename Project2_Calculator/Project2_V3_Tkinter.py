#Mad with abodi2098
#-----------------------|
#grid: (column: int row: int)
from tkinter import *
from tkinter import messagebox


app = Tk()
app.title("Calculator")
app.geometry("350x525+50+10")
app.resizable(True,False)
app.config(background = "#E6E6E6")

inputs = []
math = ""
show_inputs = []
show_math = ""

show_bg_color = "#E6E6E6"
show_fg_color = "#000000"
show_font = "Gill Sans"
show_font_size = 25
show_font_bold = "bold"

btns_bg_color = "#FFFFFF"
btns_bg_color2 = "#F0F0F0"
btns_fg_color = "#000000"
btns_font = "Gill Sans"
btns_font_size = 16
btns_font_bold = ""


clr = ""
def white():
    global clr
    clr = ""
    for g in range(2):
        for c in range(125):
            clr += "                                                                                                "
        clr += "\n"
    show = Label(app,
    text = clr,
    bg = "#E6E6E6",
    font = ("",
    20,
    "",
    )
    ) ; show.place(x=5,y=25)

class other:
    def re_math():
        global math
        global inputs
        global show_math
        global show_inputs
        global white

        math = ""
        for M in inputs:
            math += M

        show_math = ""
        for SM in show_inputs:
            show_math += SM

        white()



class App:
    def __init__(self):
        zero = Label(app,
        text="0",
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; zero.place(x=5,y=45)


    def funcINFO(self):
        info = Tk()
        info.title("Program INFO")
        info.geometry("325x250")
        info.resizable(False,False)

        INFO = Label(info,
        text="This APP is V3 from Project2\n\nI made it to see how mach I upgrade my self in one month\nand for FUN also\n\n\nDouble ÷ Means Floor Division\n\n\n\n\n\n\n\nmade by Abdullah Baaqeil\ndate 2022/10/18"
        ) ; INFO.pack()


        info.mainloop()
    def funcCLR(self):
        global inputs
        global show_inputs
        global math
        global show_math
        global white

        inputs = ["0"]
        math = "0"
        show_inputs = ["0"]
        show_math = "0"
        white()
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        inputs = []
        math = ""
        show_inputs = []
        show_math = ""

    def funcDEL(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        del(inputs[-1])
        del(show_inputs[-1])
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)

    def funcSE(self):
        global clr
        global math
        global show_math
        global app
        clr = ""
        for c in range(125):
            clr += "                                                                                                "
        try:
            small_equal = eval(math)
            show = Label(app,
            text=clr,
            fg = "Gray",
            bg = "#E6E6E6",
            font = ("",
            9,
            ""
            )
            ) ; show.place(x=20,y=100)
            other.re_math()
            show = Label(app,
            text = show_math,
            bg = show_bg_color,
            fg = show_fg_color,
            font = (show_font,
            show_font_size,
            show_font_bold,
            )
            ) ; show.place(x=5,y=45)
            small_equal = eval(math)
            show = Label(app,
            text=small_equal,
            fg = "Gray",
            bg = "#E6E6E6",
            font = ("",
            9,
            ""
            )
            ) ; show.place(x=20,y=100)
        except:
            show = Label(app,
            text=clr,
            fg = "Gray",
            bg = "#E6E6E6",
            font = ("",
            9,
            ""
            )
            ) ; show.place(x=20,y=100)
            show = Label(app,
            text="Result is undefined",
            fg = "Gray",
            bg = "#E6E6E6",
            font = ("",
            9,
            ""
            )
            ) ; show.place(x=20,y=100)

    def func0(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        if len(inputs) >= 1:
            inputs.append("0")
            show_inputs.append("0")
            other.re_math()
            show = Label(app,
            text = show_math,
            bg = show_bg_color,
            fg = show_fg_color,
            font = (show_font,
            show_font_size,
            show_font_bold,
            )
            ) ; show.place(x=5,y=45)
            self.funcSE()


    def func1(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("1")
        show_inputs.append("1")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def func2(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("2")
        show_inputs.append("2")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def func3(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("3")
        show_inputs.append("3")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def func4(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("4")
        show_inputs.append("4")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def func5(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("5")
        show_inputs.append("5")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def func6(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("6")
        show_inputs.append("6")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def func7(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("7")
        show_inputs.append("7")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def func8(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("8")
        show_inputs.append("8")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def func9(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("9")
        show_inputs.append("9")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def funcP(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("+")
        show_inputs.append("+")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def funcS(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("-")
        show_inputs.append("-")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def funcD(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("/")
        show_inputs.append("÷")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def funcM(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("*")
        show_inputs.append("×")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def funcH(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("%")
        show_inputs.append("%")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def funcQ1(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        if inputs[-1] != "*" or "-" or "+" or "/" or "%":
            inputs.append("*(")
            show_inputs.append("(")
        else:
            inputs.append("(")
            show_inputs.append("(")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def funcQ2(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append(")")
        inputs.append("*")
        show_inputs.append(")")
        show_inputs.append("×")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def funcN(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append(".")
        show_inputs.append(".")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()


    def funcX2(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        inputs.append("**2")
        show_inputs.append("^2")
        other.re_math()
        show = Label(app,
        text = show_math,
        bg = show_bg_color,
        fg = show_fg_color,
        font = (show_font,
        show_font_size,
        show_font_bold,
        )
        ) ; show.place(x=5,y=45)
        self.funcSE()

    def funcNP(self):
        global app
        global inputs
        global show_inputs
        global show_math
        global math
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        if inputs[-1] != "*" or "-" or "+" or "/" or "%" or "(" or ")":
            inputs.append("*-1")
            show_inputs.append("×-1")
            inputs.append("+")
            show_inputs.append("+")
            other.re_math()
            show = Label(app,
            text = show_math,
            bg = show_bg_color,
            fg = show_fg_color,
            font = (show_font,
            show_font_size,
            show_font_bold,
            )
            ) ; show.place(x=5,y=45)
            self.funcSE()
        else:
            pass


    def funcE(self):
        global math
        global show_math
        global show_inputs
        global inputs
        global app
        global show_bg_color
        global show_fg_color
        global show_font
        global show_font_size
        global show_font_bold
        try:
            other.re_math()
            equal = eval(math)
            show = Label(app,
            text = equal,
            bg = show_bg_color,
            fg = show_fg_color,
            font = (show_font,
            show_font_size,
            show_font_bold,
            )
            ) ; show.place(x=5,y=45)
            math = str(equal)
            show_math = str(equal)
            inputs = [str(equal)]
            show_inputs = [str(equal)]
            self.funcSE()
        except:
            erorr = messagebox.showerror("Erorr","Result is undefined")
            self.funcCLR()
run = App()

def btn0_enter(mouse):
        btn0["background"] = "#CFCFCF"
def btn0_leave(mouse):
        btn0["background"] = "#FFFFFF"

def btn1_enter(mouse):
        btn1["background"] = "#CFCFCF"
def btn1_leave(mouse):
        btn1["background"] = "#FFFFFF"

def btn2_enter(mouse):
        btn2["background"] = "#CFCFCF"
def btn2_leave(mouse):
        btn2["background"] = "#FFFFFF"

def btn3_enter(mouse):
        btn3["background"] = "#CFCFCF"
def btn3_leave(mouse):
        btn3["background"] = "#FFFFFF"

def btn4_enter(mouse):
        btn4["background"] = "#CFCFCF"
def btn4_leave(mouse):
        btn4["background"] = "#FFFFFF"

def btn5_enter(mouse):
        btn5["background"] = "#CFCFCF"
def btn5_leave(mouse):
        btn5["background"] = "#FFFFFF"

def btn6_enter(mouse):
        btn6["background"] = "#CFCFCF"
def btn6_leave(mouse):
        btn6["background"] = "#FFFFFF"

def btn7_enter(mouse):
        btn7["background"] = "#CFCFCF"
def btn7_leave(mouse):
        btn7["background"] = "#FFFFFF"

def btn8_enter(mouse):
        btn8["background"] = "#CFCFCF"
def btn8_leave(mouse):
        btn8["background"] = "#FFFFFF"

def btn9_enter(mouse):
        btn9["background"] = "#CFCFCF"
def btn9_leave(mouse):
        btn9["background"] = "#FFFFFF"

def btnP_enter(mouse):
        btnP["background"] = "#CFCFCF"
def btnP_leave(mouse):
        btnP["background"] = "#F0F0F0"

def btnS_enter(mouse):
        btnS["background"] = "#CFCFCF"
def btnS_leave(mouse):
        btnS["background"] = "#F0F0F0"

def btnM_enter(mouse):
        btnM["background"] = "#CFCFCF"
def btnM_leave(mouse):
        btnM["background"] = "#F0F0F0"

def btnD_enter(mouse):
        btnD["background"] = "#CFCFCF"
def btnD_leave(mouse):
        btnD["background"] = "#F0F0F0"

def btnX2_enter(mouse):
        btnX2["background"] = "#CFCFCF"
def btnX2_leave(mouse):
        btnX2["background"] = "#F0F0F0"

def btnQ1_enter(mouse):
        btnQ1["background"] = "#CFCFCF"
def btnQ1_leave(mouse):
        btnQ1["background"] = "#F0F0F0"

def btnQ2_enter(mouse):
        btnQ2["background"] = "#CFCFCF"
def btnQ2_leave(mouse):
        btnQ2["background"] = "#F0F0F0"

def btnNP_enter(mouse):
        btnNP["background"] = "#CFCFCF"
def btnNP_leave(mouse):
        btnNP["background"] = "#FFFFFF"

def btnN_enter(mouse):
        btnN["background"] = "#CFCFCF"
def btnN_leave(mouse):
        btnN["background"] = "#FFFFFF"

def btnH_enter(mouse):
        btnH["background"] = "#CFCFCF"
def btnH_leave(mouse):
        btnH["background"] = "#F0F0F0"

def btnDEL_enter(mouse):
        btnDEL["background"] = "#CFCFCF"
def btnDEL_leave(mouse):
        btnDEL["background"] = "#F0F0F0"

def btnCLR_enter(mouse):
        btnCLR["background"] = "#CFCFCF"
def btnCLR_leave(mouse):
        btnCLR["background"] = "#F0F0F0"

def btnINFO_enter(mouse):
        btnINFO["background"] = "#CFCFCF"
def btnINFO_leave(mouse):
        btnINFO["background"] = "#F0F0F0"

def btnE_enter(mouse):
        btnE["background"] = "#CFCFCF"
def btnE_leave(mouse):
        btnE["background"] = "#F0F0F0"

btn0 = Button(app,
    text = "0",
    fg = btns_fg_color,
    bg = btns_bg_color,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.func0,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btn0.place(x=100,y=455)


btn1 = Button(app,
    text = "1",
    fg = btns_fg_color,
    bg = btns_bg_color,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.func1,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btn1.place(x=20,y=390)

btn2 = Button(app,
    text = "2",
    fg = btns_fg_color,
    bg = btns_bg_color,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.func2,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btn2.place(x=100,y=390)


btn3 = Button(app,
    text = "3",
    fg = btns_fg_color,
    bg = btns_bg_color,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.func3,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btn3.place(x=180,y=390)


btn4 = Button(app,
    text = "4",
    fg = btns_fg_color,
    bg = btns_bg_color,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.func4,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btn4.place(x=20,y=325)


btn5 = Button(app,
    text = "5",
    fg = btns_fg_color,
    bg = btns_bg_color,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.func5,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btn5.place(x=100,y=325)


btn6 = Button(app,
    text = "6",
    fg = btns_fg_color,
    bg = btns_bg_color,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.func6,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btn6.place(x=180,y=325)


btn7 = Button(app,
    text = "7",
    fg = btns_fg_color,
    bg = btns_bg_color,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.func7,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btn7.place(x=20,y=260)


btn8 = Button(app,
    text = "8",
    fg = btns_fg_color,
    bg = btns_bg_color,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.func8,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btn8.place(x=100,y=260)


btn9 = Button(app,
    text = "9",
    fg = btns_fg_color,
    bg = btns_bg_color,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.func9,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btn9.place(x=180,y=260)


btnN = Button(app,
    text = ".",
    fg = btns_fg_color,
    bg = btns_bg_color,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcN,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnN.place(x=180,y=455)


btnNP = Button(app,
    text = "-|+",
    fg = btns_fg_color,
    bg = btns_bg_color,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcNP,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnNP.place(x=20,y=455)


btnP = Button(app,
    text = "+",
    fg = btns_fg_color,
    bg = btns_bg_color2,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcP,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnP.place(x=260,y=390)


btnS = Button(app,
    text = "-",
    fg = btns_fg_color,
    bg = btns_bg_color2,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcS,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnS.place(x=260,y=325)


btnM = Button(app,
    text = "×",
    fg = btns_fg_color,
    bg = btns_bg_color2,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcM,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnM.place(x=260,y=260)


btnD = Button(app,
    text = "÷",
    fg = btns_fg_color,
    bg = btns_bg_color2,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcD,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnD.place(x=260,y=195)


btnH = Button(app,
    text = "%",
    fg = btns_fg_color,
    bg = btns_bg_color2,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcH,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnH.place(x=180,y=195)


btnQ1 = Button(app,
    text = "(",
    fg = btns_fg_color,
    bg = btns_bg_color2,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcQ1,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnQ1.place(x=20,y=195)


btnQ2 = Button(app,
    text = ")",
    fg = btns_fg_color,
    bg = btns_bg_color2,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcQ2,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnQ2.place(x=100,y=195)


btnDEL = Button(app,
    text = "<<",
    fg = btns_fg_color,
    bg = btns_bg_color2,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcDEL,
    compound = TOP,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnDEL.place(x=260,y=130)

btnCLR = Button(app,
    text = "C",
    fg = btns_fg_color,
    bg = btns_bg_color2,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcCLR,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnCLR.place(x=180,y=130)


btnX2 = Button(app,
    text = "X2",
    fg = btns_fg_color,
    bg = btns_bg_color2,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcX2,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnX2.place(x=100,y=130)

btnINFO = Button(app,
    text = "INFO",
    fg = btns_fg_color,
    bg = btns_bg_color2,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcINFO,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnINFO.place(x=20,y=130)


btnE = Button(app,
    text = "=",
    fg = btns_fg_color,
    bg = btns_bg_color2,
    activebackground = "#A3A3A3",
    width = 6,
    height = 2,
    bd = 0,
    cursor = "hand2",
    command = run.funcE,
    font = (btns_font,
    btns_font_size,
    btns_font_bold,
    )
    ) ; btnE.place(x=260,y=455)

btn0.bind("<Enter>",btn0_enter)
btn0.bind("<Leave>",btn0_leave)
btn1.bind("<Enter>",btn1_enter)
btn1.bind("<Leave>",btn1_leave)
btn2.bind("<Enter>",btn2_enter)
btn2.bind("<Leave>",btn2_leave)
btn3.bind("<Enter>",btn3_enter)
btn3.bind("<Leave>",btn3_leave)
btn4.bind("<Enter>",btn4_enter)
btn4.bind("<Leave>",btn4_leave)
btn5.bind("<Enter>",btn5_enter)
btn5.bind("<Leave>",btn5_leave)
btn6.bind("<Enter>",btn6_enter)
btn6.bind("<Leave>",btn6_leave)
btn7.bind("<Enter>",btn7_enter)
btn7.bind("<Leave>",btn7_leave)
btn8.bind("<Enter>",btn8_enter)
btn8.bind("<Leave>",btn8_leave)
btn9.bind("<Enter>",btn9_enter)
btn9.bind("<Leave>",btn9_leave)
btnN.bind("<Enter>",btnN_enter)
btnN.bind("<Leave>",btnN_leave)
btnNP.bind("<Enter>",btnNP_enter)
btnNP.bind("<Leave>",btnNP_leave)
btnP.bind("<Enter>",btnP_enter)
btnP.bind("<Leave>",btnP_leave)
btnS.bind("<Enter>",btnS_enter)
btnS.bind("<Leave>",btnS_leave)
btnM.bind("<Enter>",btnM_enter)
btnM.bind("<Leave>",btnM_leave)
btnD.bind("<Enter>",btnD_enter)
btnD.bind("<Leave>",btnD_leave)
btnH.bind("<Enter>",btnH_enter)
btnH.bind("<Leave>",btnH_leave)
btnQ1.bind("<Enter>",btnQ1_enter)
btnQ1.bind("<Leave>",btnQ1_leave)
btnQ2.bind("<Enter>",btnQ2_enter)
btnQ2.bind("<Leave>",btnQ2_leave)
btnDEL.bind("<Enter>",btnDEL_enter)
btnDEL.bind("<Leave>",btnDEL_leave)
btnCLR.bind("<Enter>",btnCLR_enter)
btnCLR.bind("<Leave>",btnCLR_leave)
btnX2.bind("<Enter>",btnX2_enter)
btnX2.bind("<Leave>",btnX2_leave)
btnINFO.bind("<Enter>",btnINFO_enter)
btnINFO.bind("<Leave>",btnINFO_leave)
btnE.bind("<Enter>",btnE_enter)
btnE.bind("<Leave>",btnE_leave)

app.mainloop()
