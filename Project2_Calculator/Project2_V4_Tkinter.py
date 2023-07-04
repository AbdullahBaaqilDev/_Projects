from tkinter import *;
app = Tk();
app.title("Calculator")    ;
app.geometry("295x535+1+1");app.resizable(False,False);
app.config(bg = "#F0F0F0") ;
class Calculator:
    def __init__(self):
        self.show_inputs         = [];
        self.math_inputs         = [];
        self.math                = "";
        self.show_math           = "";
        self.WINDOW_BG           = "#F0F0F0";
        self.WHITE_BTNS_BG       = "#FFFFFF";
        self.WHITE_BTNS_BG_ACTV  = "#D0D0D0";
        self.WHITE_BTNS_BG_HOVER = "#F0F0F0";
        self.WHITE_BTNS_FG       = "#000000";
        self.GRAY_BTNS_BG        = "#E0E0E0";
        self.GRAY_BTNS_BG_ACTV   = "#B0B0B0";
        self.GRAY_BTNS_BG_HOVER  = "#D0D0D0";
        self.GRAY_BTNS_FG        = "#000000";
        self.scr = Scrollbar(app,orient=HORIZONTAL);self.scr.pack(side=TOP,fill=X)
        self.show = Entry(app,justify=LEFT,width=18,bd=0,bg = self.WINDOW_BG,font=("Gill Sans",20,""),xscrollcommand=self.scr.set(0.5,1));self.show.place(x=10,y=50);
        self.scr.config(command=self.show.xview)
        self.show.insert(END,"0")
        self.show_s = Entry(app,justify=LEFT,width=18,bd=0,bg = self.WINDOW_BG,fg = "Gray",font = ("Gill Sans",10,"",));self.show_s.place(x=10,y=20);
        self.H3 = Label(app,text = "___________________________________________________________________________________________________",bg = self.WINDOW_BG,fg = "Gray",font = ("Gill Sans",16,"",));self.H3.place(x=0,y=105);
        btn0   = Button(app,text = "0",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="0",input_text="0"),font = ("Gill Sans",16,""));btn0.place(x=80,y=465)
        btn1   = Button(app,text = "1",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="1",input_text="1"),font = ("Gill Sans",16,""));btn1.place(x=10,y=400)
        btn2   = Button(app,text = "2",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="2",input_text="2"),font = ("Gill Sans",16,""));btn2.place(x=80,y=400)
        btn3   = Button(app,text = "3",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="3",input_text="3"),font = ("Gill Sans",16,""));btn3.place(x=150,y=400)
        btn4   = Button(app,text = "4",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="4",input_text="4"),font = ("Gill Sans",16,""));btn4.place(x=10,y=335)
        btn5   = Button(app,text = "5",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="5",input_text="5"),font = ("Gill Sans",16,""));btn5.place(x=80,y=335)
        btn6   = Button(app,text = "6",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="6",input_text="6"),font = ("Gill Sans",16,""));btn6.place(x=150,y=335)
        btn7   = Button(app,text = "7",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="7",input_text="7"),font = ("Gill Sans",16,""));btn7.place(x=10,y=270)
        btn8   = Button(app,text = "8",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="8",input_text="8"),font = ("Gill Sans",16,""));btn8.place(x=80,y=270)
        btn9   = Button(app,text = "9",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="9",input_text="9"),font = ("Gill Sans",16,""));btn9.place(x=150,y=270)
        btnN   = Button(app,text = ".",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text=".",input_text="."),font = ("Gill Sans",16,""));btnN.place(x=150,y=465)
        btnE   = Button(app,text = "=",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.funcE(),font = ("Gill Sans",16,""));btnE.place(x=220,y=465)
        btnM   = Button(app,text = "x",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="x",input_text="*"),font = ("Gill Sans",16,""));btnM.place(x=220,y=400)
        btnD   = Button(app,text = "/",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="/",input_text="/"),font = ("Gill Sans",16,""));btnD.place(x=220,y=335)
        btnP   = Button(app,text = "+",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="+",input_text="+"),font = ("Gill Sans",16,""));btnP.place(x=220,y=270)
        btnS   = Button(app,text = "-",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="-",input_text="-"),font = ("Gill Sans",16,""));btnS.place(x=220,y=205)
        btnH   = Button(app,text = "%",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="%",input_text="%"),font = ("Gill Sans",16,""));btnH.place(x=150,y=205)
        btnQ1  = Button(app,text = "(",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.funcQ1(),font = ("Gill Sans",16,""));btnQ1.place(x=10,y=205)
        btnQ2  = Button(app,text = ")",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.funcQ2(),font = ("Gill Sans",16,""));btnQ2.place(x=80,y=205)
        btnX2  = Button(app,text = "X2",bg   = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text="^2",input_text="**2"),font = ("Gill Sans",16,""));btnX2.place(x=80,y=140)
        btnDEL = Button(app,text = "",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.funcDEL(),font = ("Gill Sans",16,""));btnDEL.place(x=220,y=140)
        btnSET = Button(app,text = "",bg  = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.funcSET(),font = ("Gill Sans",16,""));btnSET.place(x=10,y=465)
        btnSQR = Button(app,text = "sqra",bg = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(show_text=":sqra",input_text="**0.5"),font = ("Gill Sans",16,""));btnSQR.place(x=10,y=140)
        btnCLR = Button(app,text = "C",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.funcCLR(),font = ("Gill Sans",16,""));btnCLR.place(x=150,y=140)
        def btn0_enter(mouse):btn0["background"]     = self.WHITE_BTNS_BG_HOVER
        def btn0_leave(mouse):btn0["background"]     = self.WHITE_BTNS_BG
        def btn1_enter(mouse):btn1["background"]     = self.WHITE_BTNS_BG_HOVER
        def btn1_leave(mouse):btn1["background"]     = self.WHITE_BTNS_BG
        def btn2_enter(mouse):btn2["background"]     = self.WHITE_BTNS_BG_HOVER
        def btn2_leave(mouse):btn2["background"]     = self.WHITE_BTNS_BG
        def btn3_enter(mouse):btn3["background"]     = self.WHITE_BTNS_BG_HOVER
        def btn3_leave(mouse):btn3["background"]     = self.WHITE_BTNS_BG
        def btn4_enter(mouse):btn4["background"]     = self.WHITE_BTNS_BG_HOVER
        def btn4_leave(mouse):btn4["background"]     = self.WHITE_BTNS_BG
        def btn4_enter(mouse):btn4["background"]     = self.WHITE_BTNS_BG_HOVER
        def btn4_leave(mouse):btn4["background"]     = self.WHITE_BTNS_BG
        def btn5_enter(mouse):btn5["background"]     = self.WHITE_BTNS_BG_HOVER
        def btn5_leave(mouse):btn5["background"]     = self.WHITE_BTNS_BG
        def btn6_enter(mouse):btn6["background"]     = self.WHITE_BTNS_BG_HOVER
        def btn6_leave(mouse):btn6["background"]     = self.WHITE_BTNS_BG
        def btn7_enter(mouse):btn7["background"]     = self.WHITE_BTNS_BG_HOVER
        def btn7_leave(mouse):btn7["background"]     = self.WHITE_BTNS_BG
        def btn8_enter(mouse):btn8["background"]     = self.WHITE_BTNS_BG_HOVER
        def btn8_leave(mouse):btn8["background"]     = self.WHITE_BTNS_BG
        def btn9_enter(mouse):btn9["background"]     = self.WHITE_BTNS_BG_HOVER
        def btn9_leave(mouse):btn9["background"]     = self.WHITE_BTNS_BG
        def btnN_enter(mouse):btnN["background"]     = self.WHITE_BTNS_BG_HOVER
        def btnN_leave(mouse):btnN["background"]     = self.WHITE_BTNS_BG
        def btnE_enter(mouse):btnE["background"]     = self.GRAY_BTNS_BG_HOVER
        def btnE_leave(mouse):btnE["background"]     = self.GRAY_BTNS_BG
        def btnD_enter(mouse):btnD["background"]     = self.GRAY_BTNS_BG_HOVER
        def btnD_leave(mouse):btnD["background"]     = self.GRAY_BTNS_BG
        def btnM_enter(mouse):btnM["background"]     = self.GRAY_BTNS_BG_HOVER
        def btnM_leave(mouse):btnM["background"]     = self.GRAY_BTNS_BG
        def btnP_enter(mouse):btnP["background"]     = self.GRAY_BTNS_BG_HOVER
        def btnP_leave(mouse):btnP["background"]     = self.GRAY_BTNS_BG
        def btnS_enter(mouse):btnS["background"]     = self.GRAY_BTNS_BG_HOVER
        def btnS_leave(mouse):btnS["background"]     = self.GRAY_BTNS_BG
        def btnH_enter(mouse):btnH["background"]     = self.GRAY_BTNS_BG_HOVER
        def btnH_leave(mouse):btnH["background"]     = self.GRAY_BTNS_BG
        def btnE_enter(mouse):btnE["background"]     = self.GRAY_BTNS_BG_HOVER
        def btnE_leave(mouse):btnE["background"]     = self.GRAY_BTNS_BG
        def btnQ1_enter(mouse):btnQ1["background"]   = self.GRAY_BTNS_BG_HOVER
        def btnQ1_leave(mouse):btnQ1["background"]   = self.GRAY_BTNS_BG
        def btnQ2_enter(mouse):btnQ2["background"]   = self.GRAY_BTNS_BG_HOVER
        def btnQ2_leave(mouse):btnQ2["background"]   = self.GRAY_BTNS_BG
        def btnX2_enter(mouse):btnX2["background"]   = self.GRAY_BTNS_BG_HOVER
        def btnX2_leave(mouse):btnX2["background"]   = self.GRAY_BTNS_BG
        def btnDEL_enter(mouse):btnDEL["background"] = self.GRAY_BTNS_BG_HOVER
        def btnDEL_leave(mouse):btnDEL["background"] = self.GRAY_BTNS_BG
        def btnSET_enter(mouse):btnSET["background"] = self.WHITE_BTNS_BG_HOVER
        def btnSET_leave(mouse):btnSET["background"] = self.WHITE_BTNS_BG
        def btnSQR_enter(mouse):btnSQR["background"] = self.GRAY_BTNS_BG_HOVER
        def btnSQR_leave(mouse):btnSQR["background"] = self.GRAY_BTNS_BG
        def btnCLR_enter(mouse):btnCLR["background"] = self.GRAY_BTNS_BG_HOVER
        def btnCLR_leave(mouse):btnCLR["background"] = self.GRAY_BTNS_BG
        btn0.bind("<Enter>",btn0_enter);btn0.bind("<Leave>",btn0_leave)
        btn1.bind("<Enter>",btn1_enter);btn1.bind("<Leave>",btn1_leave)
        btn2.bind("<Enter>",btn2_enter);btn2.bind("<Leave>",btn2_leave)
        btn3.bind("<Enter>",btn3_enter);btn3.bind("<Leave>",btn3_leave)
        btn4.bind("<Enter>",btn4_enter);btn4.bind("<Leave>",btn4_leave)
        btn5.bind("<Enter>",btn5_enter);btn5.bind("<Leave>",btn5_leave)
        btn6.bind("<Enter>",btn6_enter);btn6.bind("<Leave>",btn6_leave)
        btn7.bind("<Enter>",btn7_enter);btn7.bind("<Leave>",btn7_leave)
        btn8.bind("<Enter>",btn8_enter);btn8.bind("<Leave>",btn8_leave)
        btn9.bind("<Enter>",btn9_enter);btn9.bind("<Leave>",btn9_leave)
        btnN.bind("<Enter>",btnN_enter);btnN.bind("<Leave>",btnN_leave)
        btnD.bind("<Enter>",btnD_enter);btnD.bind("<Leave>",btnD_leave)
        btnM.bind("<Enter>",btnM_enter);btnM.bind("<Leave>",btnM_leave)
        btnP.bind("<Enter>",btnP_enter);btnP.bind("<Leave>",btnP_leave)
        btnS.bind("<Enter>",btnS_enter);btnS.bind("<Leave>",btnS_leave)
        btnH.bind("<Enter>",btnH_enter);btnH.bind("<Leave>",btnH_leave)
        btnE.bind("<Enter>",btnE_enter);btnE.bind("<Leave>",btnE_leave)
        btnX2.bind("<Enter>",btnX2_enter);btnX2.bind("<Leave>",btnX2_leave)
        btnQ1.bind("<Enter>",btnQ1_enter);btnQ1.bind("<Leave>",btnQ1_leave)
        btnQ2.bind("<Enter>",btnQ2_enter);btnQ2.bind("<Leave>",btnQ2_leave)
        btnDEL.bind("<Enter>",btnDEL_enter);btnDEL.bind("<Leave>",btnDEL_leave)
        btnSET.bind("<Enter>",btnSET_enter);btnSET.bind("<Leave>",btnSET_leave)
        btnSQR.bind("<Enter>",btnSQR_enter);btnSQR.bind("<Leave>",btnSQR_leave)
        btnCLR.bind("<Enter>",btnCLR_enter);btnCLR.bind("<Leave>",btnCLR_leave)
        self.white_btns_list = [btn0,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btnN,btnSET]
        self.gray_btns_list  = [btnD,btnM,btnP,btnS,btnH,btnE,btnX2,btnSQR,btnQ1,btnQ2,btnCLR,btnDEL]
    def funcSET(self):
        def dark_light(theme):
            if theme == "Dark":
                self.WINDOW_BG     = "#121212";
                self.WHITE_BTNS_BG = "#3B3B3B";self.WHITE_BTNS_FG = "#F0F0F0";self.WHITE_BTNS_BG_ACTV = "#202020";self.WHITE_BTNS_BG_HOVER = "#151515";
                self.GRAY_BTNS_BG  = "#222222";self.GRAY_BTNS_FG  = "#F0F0F0";self.GRAY_BTNS_BG_ACTV  = "#101010";self.GRAY_BTNS_BG_HOVER  = "#121212";
                app.config(bg = self.WINDOW_BG);
                self.settings.config(bg = self.WINDOW_BG);
                self.theme_info.config(bg=self.WINDOW_BG)
                self.theme_info.config(fg=self.GRAY_BTNS_FG)
                self.dark_btn.config(bg=self.WINDOW_BG)
                self.dark_btn.config(fg=self.GRAY_BTNS_FG)
                self.light_btn.config(bg=self.WINDOW_BG)
                self.light_btn.config(fg=self.GRAY_BTNS_FG)
                self.H3.config(bg=self.WINDOW_BG)
                self.show.config(bg=self.WINDOW_BG,fg=self.GRAY_BTNS_FG)
                self.show_s.config(bg=self.WINDOW_BG,fg=self.GRAY_BTNS_FG)
                self.scr.config(background=self.WINDOW_BG)
                for the_btn1 in self.white_btns_list:the_btn1.config(bg = self.WHITE_BTNS_BG);the_btn1.config(fg = self.WHITE_BTNS_FG);
                for the_btn2 in self.gray_btns_list:the_btn2.config(fg = self.GRAY_BTNS_FG);the_btn2.config(bg = self.GRAY_BTNS_BG);
            else:
                self.WINDOW_BG     = "#F0F0F0";
                self.WHITE_BTNS_BG = "#FFFFFF";self.WHITE_BTNS_FG = "#000000";self.WHITE_BTNS_BG_ACTV = "#D0D0D0";self.WHITE_BTNS_BG_HOVER = "#F0F0F0";
                self.GRAY_BTNS_BG  = "#E0E0E0";self.GRAY_BTNS_FG  = "#000000";self.GRAY_BTNS_BG_ACTV  = "#B0B0B0";self.GRAY_BTNS_BG_HOVER  = "#D0D0D0";
                app.config(bg = self.WINDOW_BG);
                self.settings.config(bg = self.WINDOW_BG);
                self.theme_info.config(bg=self.WINDOW_BG);
                self.theme_info.config(fg=self.GRAY_BTNS_FG);
                self.dark_btn.config(bg=self.WINDOW_BG);
                self.dark_btn.config(fg=self.GRAY_BTNS_FG);
                self.light_btn.config(bg=self.WINDOW_BG);
                self.light_btn.config(fg=self.GRAY_BTNS_FG);
                self.H3.config(bg=self.WINDOW_BG);
                self.show.config(bg=self.WINDOW_BG,fg=self.GRAY_BTNS_FG);
                self.show_s.config(bg=self.WINDOW_BG,fg=self.GRAY_BTNS_FG)
                self.scr.config(background=self.WINDOW_BG)
                for the_btn1 in self.white_btns_list:the_btn1.config(bg = self.WHITE_BTNS_BG);the_btn1.config(fg = self.WHITE_BTNS_FG);
                for the_btn2 in self.gray_btns_list:the_btn2.config(fg  = self.GRAY_BTNS_FG);the_btn2.config(bg  = self.GRAY_BTNS_BG);
        self.settings = Tk();
        self.settings.title("Calculator Settings");
        self.settings.geometry("300x150");self.settings.resizable(False,False);
        self.settings.config(bg = self.WINDOW_BG);
        self.theme_info = Label(self.settings,text = "Color theme",bg = self.WINDOW_BG,fg = self.WHITE_BTNS_FG,font = ("Gill Sans",16,""));self.theme_info.grid(row=0,column=0);
        self.dark_btn  = Radiobutton(self.settings,text = "Dark theme",bg  = self.WINDOW_BG,fg = self.WHITE_BTNS_FG,command = lambda : dark_light(theme="Dark"));self.dark_btn.grid(row=1,column=0);
        self.light_btn = Radiobutton(self.settings,text = "Light theme",bg = self.WINDOW_BG,fg = self.WHITE_BTNS_FG,command = lambda : dark_light(theme="Light"));self.light_btn.grid(row=2,column=0);
        self.settings.mainloop();
    def re_math(self):
        self.math = "";self.show_math = "";
        for m in self.math_inputs: self.math += m;
        for sm in self.show_inputs: self.show_math += sm;
    def funcSE(self):
        try:small_equal = eval(self.math);
        except:small_equal = "";
        return small_equal
    def func0(self):
        if len(self.math_inputs) > 0:self.math_inputs.append("0");self.show_inputs.append("0");self.re_math();self.show.delete(0,END);self.show.insert(END,self.show_math);self.show_s.delete(0,END);self.show_s.insert(END,str(self.funcSE()));
    def add_to_cal(self,show_text,input_text):
        self.show_inputs.append(show_text);self.math_inputs.append(input_text);self.re_math();self.show.delete(0,END);self.show.insert(END,self.show_math);self.show_s.delete(0,END);self.show_s.insert(END,str(self.funcSE()));
    def funcQ1(self):
        if self.math_inputs[-1] != "*" or "/" or "+" or "-" or "%":self.show_inputs.append("(");self.math_inputs.append("*(");self.re_math();self.show.delete(0,END);self.show.insert(END,self.show_math);self.show_s.delete(0,END);self.show_s.insert(END,str(self.funcSE()));
        else:self.show_inputs.append("(");self.math_inputs.append("(");self.re_math();self.show.delete(0,END);self.show.insert(END,self.show_math);self.show_s.delete(0,END);self.show_s.insert(END,str(self.funcSE()));
    def funcQ2(self):
        if self.math_inputs[-1] != "*" or "/" or "+" or "-" or "%":self.show_inputs.append(")");self.show_inputs.append("x");self.math_inputs.append(")");self.math_inputs.append("*");self.re_math();self.show.config(text=self.show_math);self.show_s.delete(0,END);self.show_s.insert(END,str(self.funcSE()));
        else:del(self.show_inputs[-1]);self.show_inputs.append(")");self.show_inputs.append("x");self.math_inputs.append(")");self.math_inputs.append("*");self.re_math();self.show.delete(0,END);self.show.insert(END,self.show_math);self.show_s.delete(0,END);self.show_s.insert(END,str(self.funcSE()))
    def funcDEL(self):
        if len(self.math_inputs) > 0:del(self.show_inputs[-1]);del(self.math_inputs[-1]);self.re_math();self.show.delete(0,END);self.show.insert(END,self.show_math);self.show_s.delete(0,END);self.show_s.insert(END,str(self.funcSE()))
    def funcCLR(self):
        self.math = "";self.show_math = "";self.show_inputs = [];self.math_inputs = [];self.show.delete(0,END);self.show.insert(END,"0");self.show_s.delete(0,END);self.show_s.insert(END," ")
    def funcE(self):
        try:
            the_equal=eval(self.math);
            self.show.delete(0,END);self.show.insert(END,str(the_equal));
            self.show_inputs=[str(the_equal)];
            self.math_inputs=[str(the_equal)];
            self.show_s.delete(0,END);self.show_s.insert(END,"")
        except:self.funcCLR();self.show.config(text="The result is not defind")
calculator = Calculator()
app.bind("<BackSpace>",lambda event:calculator.funcDEL())
app.bind("<c>",lambda event:calculator.funcCLR())
app.bind("=",lambda event:calculator.funcE())
app.bind("(",lambda event:calculator.funcQ1())
app.bind(")",lambda event:calculator.funcQ2())
app.bind("/",lambda event:calculator.add_to_cal("/","/"))
app.bind("*",lambda event:calculator.add_to_cal("x","*"))
app.bind("<x>",lambda event:calculator.add_to_cal("x","*"))
app.bind("+",lambda event:calculator.add_to_cal("+","+"))
app.bind("-",lambda event:calculator.add_to_cal("-","-"))
app.bind("0",lambda event:calculator.add_to_cal("0","0"))
app.bind("1",lambda event:calculator.add_to_cal("1","1"))
app.bind("2",lambda event:calculator.add_to_cal("2","2"))
app.bind("3",lambda event:calculator.add_to_cal("3","3"))
app.bind("4",lambda event:calculator.add_to_cal("4","4"))
app.bind("5",lambda event:calculator.add_to_cal("5","5"))
app.bind("6",lambda event:calculator.add_to_cal("6","6"))
app.bind("7",lambda event:calculator.add_to_cal("7","7"))
app.bind("8",lambda event:calculator.add_to_cal("8","8"))
app.bind("9",lambda event:calculator.add_to_cal("9","9"))
app.mainloop()