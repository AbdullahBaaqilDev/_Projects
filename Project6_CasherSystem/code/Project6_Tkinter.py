from tkinter import *
from tkinter import messagebox
app = Tk()
app.title("Casher system")
app.geometry("710x540+10+25")
app.resizable(False,False)
class CasherSystem():
    class Calculator():
        def __init__(self):
            self.calculator_frame    = Frame(app,width=300,height=540,bg = "#F0F0F0",bd=4,relief=GROOVE,);self.calculator_frame.place(x=710,y=0)
            self.calculator_frame_2  = Frame(app,width=300);self.calculator_frame_2.place(x=715,y=5)
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
            self.scrollbar           = Scrollbar(self.calculator_frame_2,orient=HORIZONTAL,width=10,background=self.WHITE_BTNS_BG,);self.scrollbar.pack(side=TOP,fill=X)
            self.show                = Entry(master=self.calculator_frame,justify=LEFT,width=14,bd=0,bg=self.WINDOW_BG,font=("Gill Sans",25,""),xscrollcommand=self.scrollbar.set(0,0));self.show.place(x=10,y=60);
            self.show_s              = Entry(self.calculator_frame,width=25,bd=0,justify=LEFT,bg=self.WINDOW_BG,fg = "Gray",font = ("Gill Sans",15,"",));self.show_s.place(x=10,y=15);
            self.scrollbar.config(command=self.show.xview)
            self.show.insert(END,"0")

            self.H3 = Label(self.calculator_frame,text = "_______________________",bg = self.WINDOW_BG,fg = "Gray",font = ("Gill Sans",16,"",));self.H3.place(x=0,y=115);
            btn0   = Button(self.calculator_frame,text = "0",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="0",input_text="0"),font = ("Gill Sans",16,""));btn0.place(x=80,y=465)
            btn1   = Button(self.calculator_frame,text = "1",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="1",input_text="1"),font = ("Gill Sans",16,""));btn1.place(x=10,y=400)
            btn2   = Button(self.calculator_frame,text = "2",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="2",input_text="2"),font = ("Gill Sans",16,""));btn2.place(x=80,y=400)
            btn3   = Button(self.calculator_frame,text = "3",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="3",input_text="3"),font = ("Gill Sans",16,""));btn3.place(x=150,y=400)
            btn4   = Button(self.calculator_frame,text = "4",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="4",input_text="4"),font = ("Gill Sans",16,""));btn4.place(x=10,y=335)
            btn5   = Button(self.calculator_frame,text = "5",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="5",input_text="5"),font = ("Gill Sans",16,""));btn5.place(x=80,y=335)
            btn6   = Button(self.calculator_frame,text = "6",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="6",input_text="6"),font = ("Gill Sans",16,""));btn6.place(x=150,y=335)
            btn7   = Button(self.calculator_frame,text = "7",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="7",input_text="7"),font = ("Gill Sans",16,""));btn7.place(x=10,y=270)
            btn8   = Button(self.calculator_frame,text = "8",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="8",input_text="8"),font = ("Gill Sans",16,""));btn8.place(x=80,y=270)
            btn9   = Button(self.calculator_frame,text = "9",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="9",input_text="9"),font = ("Gill Sans",16,""));btn9.place(x=150,y=270)
            btnN   = Button(self.calculator_frame,text = ".",bg    = self.WHITE_BTNS_BG,activebackground = self.WHITE_BTNS_BG_ACTV,fg = self.WHITE_BTNS_FG,bd = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text=".",input_text="."),font = ("Gill Sans",16,""));btnN.place(x=10,y=465)
            btnE   = Button(self.calculator_frame,text = "=",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 10,padx=6,height = 2,command = lambda : calculator.funcE(),font = ("Gill Sans",16,""));btnE.place(x=150,y=465)
            btnM   = Button(self.calculator_frame,text = "x",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="x",input_text="*"),font = ("Gill Sans",16,""));btnM.place(x=220,y=400)
            btnD   = Button(self.calculator_frame,text = "/",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="/",input_text="/"),font = ("Gill Sans",16,""));btnD.place(x=220,y=335)
            btnP   = Button(self.calculator_frame,text = "+",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="+",input_text="+"),font = ("Gill Sans",16,""));btnP.place(x=220,y=270)
            btnS   = Button(self.calculator_frame,text = "-",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.add_to_cal(event="",show_text="-",input_text="-"),font = ("Gill Sans",16,""));btnS.place(x=220,y=205)
            btnDEL = Button(self.calculator_frame,text = "",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 5,height = 2,command = lambda : calculator.funcDEL(),font = ("Gill Sans",16,""));btnDEL.place(x=150,y=205)
            btnCLR = Button(self.calculator_frame,text = "C",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 10,padx=6,height = 2,command = lambda : calculator.funcCLR(),font = ("Gill Sans",16,""));btnCLR.place(x=10,y=205)
            btnSP  = Button(self.calculator_frame,text = "Paid up",bg    = self.GRAY_BTNS_BG,activebackground  = self.GRAY_BTNS_BG_ACTV,fg  = self.GRAY_BTNS_FG,bd  = 0,width = 45,height = 1,command = lambda : casher.rest_func(),font = ("Gill Sans",8,""));btnSP.place(x=10,y=180)
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
            def btnSP_enter(mouse):btnSP["background"]     = self.GRAY_BTNS_BG_HOVER
            def btnSP_leave(mouse):btnSP["background"]     = self.GRAY_BTNS_BG
            def btnE_enter(mouse):btnE["background"]     = self.GRAY_BTNS_BG_HOVER
            def btnE_leave(mouse):btnE["background"]     = self.GRAY_BTNS_BG
            def btnDEL_enter(mouse):btnDEL["background"] = self.GRAY_BTNS_BG_HOVER
            def btnDEL_leave(mouse):btnDEL["background"] = self.GRAY_BTNS_BG
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
            btnSP.bind("<Enter>",btnSP_enter);btnSP.bind("<Leave>",btnSP_leave)
            btnE.bind("<Enter>",btnE_enter);btnE.bind("<Leave>",btnE_leave)
            btnDEL.bind("<Enter>",btnDEL_enter);btnDEL.bind("<Leave>",btnDEL_leave)
            btnCLR.bind("<Enter>",btnCLR_enter);btnCLR.bind("<Leave>",btnCLR_leave)
            self.white_btns_list = [btn0,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btnN]
            self.gray_btns_list  = [btnD,btnM,btnP,btnS,btnSP,btnE,btnCLR,btnDEL]
        def funcSE(self):
            try:small_equal = (eval(self.math)//2)*2+1;
            except:small_equal = "";
            return small_equal;
        def re_math(self):
            self.math = "";self.show_math = "";
            for m in self.math_inputs: self.math += m;
            for sm in self.show_inputs: self.show_math += sm;
        def func0(self):
            if len(self.math_inputs) > 0:self.math_inputs.append("0");self.show_inputs.append("0");self.re_math();self.show.delete(0,END);self.show.insert(END,self.show_math);self.show_s.delete(0,END);self.show_s.insert(END,str(self.funcSE()));
        def add_to_cal(self,show_text,input_text,event):
            self.event = event
            self.show_inputs.append(show_text);self.math_inputs.append(input_text);self.re_math();self.show.delete(0,END);self.show.insert(END,self.show_math);self.show_s.delete(0,END);self.show_s.insert(END,str(self.funcSE()));
        def funcDEL(self):
            if len(self.math_inputs) > 0 and float(eval(self.math_inputs[-1])) not in casher.price_list:
                del(self.show_inputs[-1]);del(self.math_inputs[-1]);self.re_math();self.show.delete(0,END);self.show.insert(END,self.show_math);self.show_s.delete(0,END);self.show_s.insert(END,str(self.funcSE()));
            elif len(self.math_inputs) > 0 and float(eval(self.math_inputs[-1])) in casher.price_list:
                for i in range(2):casher.invoice.delete(first=END,last=END);
                del(self.show_inputs[-1]);del(self.math_inputs[-1]);self.re_math();self.show.delete(0,END);self.show.insert(END,self.show_math);self.show_s.delete(0,END);self.show_s.insert(END,str(self.funcSE()));
        def funcCLR(self):
            casher.invoice.delete(first=0,last=END);
            self.math = "";self.show_math = "";self.show_inputs = [];self.math_inputs = [];self.re_math();self.show.delete(0,END);self.show.insert(END,"0");self.show_s.delete(0,END);self.show_s.insert(END,str(self.funcSE()));
        def funcE(self):
            try:
                self.re_math();
                the_equal=eval(self.math);
                self.show_s.delete(0,END);
                self.show.delete(0,END);self.show_s.delete(0,END)
                self.show.insert(END,str(the_equal))
                self.show_inputs=[str(the_equal)];
                self.math_inputs=[str(the_equal)];
            except:
                self.funcCLR();self.show.delete(0,END);self.show.insert(END,"The resulte is not defind")

    def __init__(self,__version__,__data__):
        self.codes_list          = []
        self.price_list          = []
        self.names_list          = []
        self.hidden              = True# Is Calculator frame hidden
        self.paid_up_var         = ""
        self.color_theme_var     = ""# Change by color theme radiobutton
        self.goods_quantity      = 0
        self.paid_up_label       = Label(calculator.calculator_frame,text=" ",bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",10,""));self.paid_up_label.place(x=160,y=155)
        self.show_goods_quantity = Label(calculator.calculator_frame,text="Goods Quantity: {}".format(str(self.goods_quantity)),bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",10,""));self.show_goods_quantity.place(x=10,y=115)
        self.show_goods_price    = Label(calculator.calculator_frame,text="Goods Price: {}".format(str(0)),bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",10,""));self.show_goods_price.place(x=145,y=115)
        self.invoice_label       = Label(app,text="                   ID                                      Price                               Name",bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",15,""));self.invoice_label.place(x=5,y=25)
        self.paid_up             = Entry(calculator.calculator_frame,textvariable=self.paid_up_var,width=18,bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",10,""));self.paid_up.place(x=10,y=155)
        self.invoice             = Listbox(app,relief=SUNKEN,justify=RIGHT,width=64,height=15,font=("Calibri",14,"",));self.invoice.place(x=55,y=75)
        self.bar_frame           = Frame(app,width=50,height=1080,bg=calculator.WHITE_BTNS_BG,);self.bar_frame.place(x=0,y=0)

        # Leftbar buttons
        def enter_enter(event):self.enter_code_with_id.config(fg=calculator.WHITE_BTNS_FG)
        def enter_leave(event):self.enter_code_with_id.config(fg=calculator.WHITE_BTNS_BG_ACTV)
        self.enter_code_with_id = Button(self.bar_frame,text="  ",bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_BG_ACTV,activebackground=calculator.WHITE_BTNS_BG_ACTV,activeforeground=calculator.WHITE_BTNS_FG,bd=0,command=lambda: self.func_enter_code(event=""),font=("Gill Sans",18,""));self.enter_code_with_id.place(x=0,y=5)
        self.enter_code_with_id.bind("<Enter>",enter_enter);self.enter_code_with_id.bind("<Leave>",enter_leave)
        
        self.change_color = Menubutton(self.bar_frame,text="  ",bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_BG_ACTV,activebackground=calculator.WHITE_BTNS_BG,activeforeground=calculator.WHITE_BTNS_FG,bd=0,font=("Gill Sans",20,""));self.change_color.place(x=0,y=50)
        
        def add_enter(event):self.add_goods_btn.config(fg=calculator.WHITE_BTNS_FG)
        def add_leave(event):self.add_goods_btn.config(fg=calculator.WHITE_BTNS_BG_ACTV)
        self.add_goods_btn = Button(self.bar_frame,text="  ",bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_BG_ACTV,activebackground=calculator.WHITE_BTNS_BG,activeforeground=calculator.WHITE_BTNS_FG,bd=0,command=lambda: self.func_add_code(),font=("Gill Sans",18,""));self.add_goods_btn.place(x=0,y=100)
        self.add_goods_btn.bind("<Enter>",add_enter);self.add_goods_btn.bind("<Leave>",add_leave)
        
        def show_enter(event):self.show_goods_btn.config(fg=calculator.WHITE_BTNS_FG)
        def show_leave(event):self.show_goods_btn.config(fg=calculator.WHITE_BTNS_BG_ACTV)
        self.show_goods_btn = Button(self.bar_frame,text="  ",bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_BG_ACTV,activebackground=calculator.WHITE_BTNS_BG,activeforeground=calculator.WHITE_BTNS_FG,bd=0,command=lambda: self.func_show_goods(),font=("Gill Sans",18,""));self.show_goods_btn.place(x=0,y=150)
        self.show_goods_btn.bind("<Enter>",show_enter);self.show_goods_btn.bind("<Leave>",show_leave)
        # Color themes menu
        themes = Menu(self.change_color)
        self.change_color.config(menu=themes)# The Leftbar button
        themes.add_radiobutton(label = "Default light",command = lambda : Settings.color_theme_func(theme="Light"))
        themes.add_radiobutton(label = "Quiet light",command = lambda : Settings.color_theme_func(theme="QULight"))
        themes.add_radiobutton(label = "Sand light",command = lambda : Settings.color_theme_func(theme="SALight"))
        themes.add_radiobutton(label = "Solarized light",command = lambda : Settings.color_theme_func(theme="SOLight"))
        themes.add_separator()
        themes.add_radiobutton(label = "Default dark",command = lambda : Settings.color_theme_func(theme="Dark"))
        themes.add_radiobutton(label = "Abyss dark",command = lambda : Settings.color_theme_func(theme="ADark"))
        themes.add_radiobutton(label = "Kimbie dark",command = lambda : Settings.color_theme_func(theme="KDark"))
        themes.add_radiobutton(label = "Monokai dark",command = lambda : Settings.color_theme_func(theme="MDDark"))
        themes.add_separator()
        colors_inputs = Menu(themes)
        colors_inputs.add_command(label="Window color",command = lambda : Settings.color_theme_func(theme="W|C"))
        colors_inputs.add_separator()
        colors_inputs.add_command(label="Buttons background color",command = lambda : Settings.color_theme_func(theme="B|B|C"))
        colors_inputs.add_command(label="Buttons background color(light)",command = lambda : Settings.color_theme_func(theme="B|B|C|L"))
        colors_inputs.add_separator()
        colors_inputs.add_command(label="Buttons hover background color",command = lambda : Settings.color_theme_func(theme="B|H|B|C"))
        colors_inputs.add_command(label="Buttons bover background color(light)",command = lambda : Settings.color_theme_func(theme="B|H|B|C|L"))
        colors_inputs.add_separator()
        colors_inputs.add_command(label="Buttons active background color",command = lambda : Settings.color_theme_func(theme="B|A|B|C"))
        colors_inputs.add_command(label="Buttons active background color(light)",command = lambda : Settings.color_theme_func(theme="B|A|B|C|L"))
        colors_inputs.add_separator()
        colors_inputs.add_command(label="Buttons foreground color",command = lambda : Settings.color_theme_func(theme="B|F|C"))
        themes.add_cascade(label="Custome color",menu=colors_inputs)

        self.options = Menu(app)# The menubar
        file_menu = Menu(self.options)
        file_menu.add_command(label="Coming soon")
        self.options.add_cascade(label="File",menu=file_menu)
        self.options.add_command(label="About",command=lambda :self.func_about(version=__version__,data=__data__))
        self.options.add_command(label="Help",command=self.func_help)
        app.config(menu=self.options)
        
        self.invoice.config(bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG)
        
        def remove_label(event):# Paid up entry-Label
            if self.paid_up.get() == "Paid up":self.paid_up.delete(0,END)
        self.paid_up.insert(END,"Paid up")
        self.paid_up.bind("<Button-1>",lambda event:remove_label(event=""))# When user click paid entry remove text

        def hide_show_enter(mouse):self.hide_show_btn.config(bg=calculator.GRAY_BTNS_BG_HOVER)
        def hide_show_leave(mouse):self.hide_show_btn.config(bg=calculator.WINDOW_BG)
        self.hide_show_btn = Button(app,text="",bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,bd=0,activebackground=calculator.WHITE_BTNS_BG_ACTV,activeforeground=calculator.WHITE_BTNS_FG,padx=3,command=lambda: self.func_show_hide(event=""),font=("",14,"bold"));self.hide_show_btn.place(x=670,y=18)
        self.hide_show_btn.bind("<Enter>",hide_show_enter);self.hide_show_btn.bind("<Leave>",hide_show_leave);
        app.bind("<Control-b>",lambda event: self.func_show_hide(event=""));self.func_show_hide(event="")

        #    goods = {<id>:[<price>,<name>]}
        self.goods = {
            "05541" :[10.0,"لبن المراعي 1.5 لتر"],
            "05542" :[15.0,"لبنة المراعي 700 جم"],
            "05543" :[7.0,"زبادي المراعي كامل الدسم"],
            "05544" :[3.0,"جبنة البقرة الضاحكة"],
            "05545" :[1.5,"عصير المراعي مانجو 150 مل"],
            "05546" :[1.5,"عصير المراعي تفاح 150 مل"],
            "05547" :[1.5,"عصير المراعي برتقال 150 مل"],
            "05548" :[1.5,"عصير المراعي فراولة 150 مل"],
            "05549" :[17.20,"المراعي زبدة 350 جم"],
            "055410":[4.0,"خبز توست ابيض 600 جم"],
            "055411":[4.0,"خبز توست اسمر 600 جم"],
            "055412":[3.5,"علبة تونة كبيرة"],
            "055413":[1.5,"فطيرة لوزين 200 جم"],
            "055414":[1.25,"جمبري ليز بالفلفل"],
            "055415":[2.5,"مرندا ليمون"],
            "055416":[0.5,"حلاوة مصاص"],
            "055417":[2.0,"الربيع برتقال"],
            "055418":[30.0,"حفاظات بامبيرز"],
            "055419":[9.0,"باونتي جوز الهند"],
            "055420":[15.0,"فيري ليمون 1.25 لتر"],
            "055421":[3.0,"بسكوت ابو ولد"],
            "055422":[1.75,"اوريو"],
            "055423":[1.5,"ايسكريم بابو"],
            "055424":[1.25,"ليز كتشب"],
            "055425":[2.0,"مرامي حار"],
            "055426":[22.0,"بطاريات كويسة"],
            "055427":[2.5,"بيبسي 400 لتر"],
            "055428":[2.5,"سيفين 400 لتر"],
            "055429":[3.0,"كوكيز"],
            "055430":[5.0,"صابون لكس 10 جم"],
            "055431":[3.5,"اندومي خضار"],
            "055432":[3.5,"تويكس"],
            "055433":[4.0,"جالكسي"],
            "055434":[8.0,"بطاريات تعبانة"],
            "055435":[18.0,"هيداندشولدير 400 مل"],
            "055436":[18.5,"دجاج فقيه 1000 جم"],
            "055437":[24.0,"طبق بيض مغلف 30 حبة"],
            "055438":[3.75,"تايد 100 جم"],
            "055439":[19.00,"تايد 1.5 كجم"],
            "055440":[11.5,"كلوركس 1.90 لتر"],
            "055441":[81.0,"نيدو 1800 جم"],
            "055442":[32.0,"نوتيلا 750 جم"],
            "055443":[11.5,"بخاخ حشرات 400 مل"],
            "055444":[34.0,"جبنة كريمة المراعي 900 مل"],
        }
    def func_enter_code(self,event):
        app.unbind("<Return>")
        self.enter_frame = Frame(app,width=200,height=350,bg=calculator.WINDOW_BG,bd=1,relief=RAISED);self.enter_frame.place(x=75,y=175)
        
        self.code_entry_info = Label(self.enter_frame,text="Goods id:",bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",20,"italic"));self.code_entry_info.place(x=5,y=5)
        self.code_entry = Entry(self.enter_frame,bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG,width=9,relief=GROOVE,justify=CENTER,font=("Gill Sans",16,""));self.code_entry.place(x=45,y=45)
        info_label = Label(self.enter_frame,text="You can enter (all) or (0554)",bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",10,""));info_label.place(x=5,y=85)
        casher.re_fill()
        def enter():
            index = 0
            if casher.code_entry.get() in ["All","all","ALL","05540","0554","All goods","all goods","All Goods"]:
                for indexA in range(len(casher.goods.items())):
                    if len(calculator.math_inputs) != 0 and calculator.math_inputs[-1] != "+":
                        calculator.math_inputs.append("+"+str(casher.price_list[indexA]));
                        calculator.show_inputs.append("+"+str(casher.price_list[indexA]));
                    elif len(calculator.math_inputs) == 0 :
                        calculator.math_inputs.append(str(casher.price_list[indexA]));
                        calculator.show_inputs.append(str(casher.price_list[indexA]));
                    elif len(calculator.math_inputs) != 0 and calculator.math_inputs[-1] == "+":
                        calculator.math_inputs.append(str(casher.price_list[indexA]));
                        calculator.show_inputs.append(str(casher.price_list[indexA]));
                    calculator.re_math();
                    calculator.show.delete(0,END);calculator.show.insert(END,calculator.show_math)
                    calculator.show_s.delete(0,END);calculator.show_s.insert(END,str(calculator.funcSE()))
                    SP = ""
                    if len(casher.names_list[indexA]) < 18:
                        for i in range(0,18-len(casher.names_list[indexA])):
                            SP += "  "
                    casher.invoice.insert(END,"{}                                                       {}{}                                {}".format(casher.codes_list[indexA],casher.price_list[indexA],SP,casher.names_list[indexA]))
                    casher.invoice.insert(END,"---------------------------------------------------------------------------------------------------------------")
                    casher.goods_quantity += 1
                    casher.show_goods_quantity.config(text="Goods quantity: {}".format(str(casher.goods_quantity)))
                    casher.show_goods_price.config(text="Goods price: {}".format(str(calculator.funcSE())))
            elif casher.code_entry.get() in casher.codes_list:
                for code_ in casher.codes_list:#search opration
                    if code_ == casher.code_entry.get():
                        if len(calculator.math_inputs) != 0 and calculator.math_inputs[-1] != "+":
                            calculator.math_inputs.append("+"+str(casher.price_list[index]));
                            calculator.show_inputs.append("+"+str(casher.price_list[index]));
                        elif len(calculator.math_inputs) == 0 :
                            calculator.math_inputs.append(str(casher.price_list[index]));
                            calculator.show_inputs.append(str(casher.price_list[index]));
                        elif len(calculator.math_inputs) != 0 and calculator.math_inputs[-1] == "+":
                            calculator.math_inputs.append(str(casher.price_list[index]));
                            calculator.show_inputs.append(str(casher.price_list[index]));
                        calculator.re_math();
                        calculator.show.delete(0,END);calculator.show.insert(END,calculator.show_math)
                        calculator.show_s.delete(0,END);calculator.show_s.insert(END,str(calculator.funcSE()))
                        SP = ""
                        if len(casher.names_list[index]) < 18:
                            for i in range(0,18-len(casher.names_list[index])):
                                SP += "  "
                        casher.invoice.insert(END,"{}                                                       {}{}                                {}".format(casher.codes_list[index],casher.price_list[index],SP,casher.names_list[index]))
                        casher.invoice.insert(END,"----------------------------------------------------------------------------------------------------------")
                        casher.goods_quantity += 1
                        casher.show_goods_quantity.config(text="Goods quantity: {}".format(str(casher.goods_quantity)))
                        casher.show_goods_price.config(text="Goods price: {}".format(str(calculator.funcSE())))
                        break
                    else:index += 1
            else:
                messagebox.showerror("Error","There is no goods have {} as ID".format(casher.code_entry.get()))
        def destroy_frame(event):self.enter_frame.destroy();app.bind("<Return>",self.func_enter_code)
        def close_enter(event):close_btn.config(bg=calculator.WHITE_BTNS_BG_HOVER)
        def close_leave(event):close_btn.config(bg=calculator.WHITE_BTNS_BG)
        close_btn = Button(self.enter_frame,text="Close",width=12,height=1,bd=1,relief=GROOVE,bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG,activebackground=calculator.WHITE_BTNS_BG_ACTV,command=lambda:destroy_frame(event=""),font=("Gill Sans",12,""));close_btn.place(x=45,y=285)
        close_btn.bind("<Enter>",close_enter)
        close_btn.bind("<Leave>",close_leave)
        def enter_enter(event):enter_btn.config(bg=calculator.WHITE_BTNS_BG_HOVER)
        def enter_leave(event):enter_btn.config(bg=calculator.WHITE_BTNS_BG)
        enter_btn = Button(self.enter_frame,text="Enter ",width=15,height=1,bd=1,relief=GROOVE,bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG,activebackground=calculator.WHITE_BTNS_BG_ACTV,command=enter,font=("Gill Sans",12,""));enter_btn.place(x=35,y=175)
        enter_btn.bind("<Enter>",enter_enter)
        enter_btn.bind("<Leave>",enter_leave)
    app.bind("<Return>",lambda event:casher.func_enter_code(event=""))
    def rest_func(self):
        if len(calculator.math_inputs) != 0 and self.paid_up.get() not in ["","Paid up"]:
            calculator.re_math();equal=calculator.funcSE()
            self.paid_up_label.config(text=str(eval(self.paid_up.get())-equal))
    def func_about(self,version,data):
        """Project Info"""
        self.about_frame = Frame(app,width=450,height=200,bg=calculator.WINDOW_BG,bd=1,relief=RAISED,);self.about_frame.place(x=300,y=5)
        about_text = """
            This is Casher system app
            Made by : Abdullah Baaqeil
            Made With : Python.tkinter
            Version : {}
            Data : {}
            ----------------------
            I made it for fun and to learn more about Python.
        """.format(version,data)
        about_label = Label(self.about_frame,text=about_text,bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",10,""),);about_label.place(x=0,y=0)
        def destroy_frame(event):self.about_frame.destroy();app.bind("<Return>",self.func_enter_code)
        
        def close_enter(event):close_btn.config(bg=calculator.WHITE_BTNS_BG_HOVER)
        def close_leave(event):close_btn.config(bg=calculator.WHITE_BTNS_BG)
        close_btn = Button(self.about_frame,text="Close",width=15,height=1,bd=1,relief=GROOVE,bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG,activebackground=calculator.WHITE_BTNS_BG_ACTV,command=lambda:destroy_frame(event=""),font=("Gill Sans",12,""));close_btn.place(x=0,y=165)
        close_btn.bind("<Enter>",close_enter)
        close_btn.bind("<Leave>",close_leave)
        
        label = Label(self.about_frame,text="You can press Enter also",bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",10,""));label.place(x=145,y=165)
        
        app.unbind("<Return>",)
        app.bind("<Return>",destroy_frame)
    def func_help(self):
        self.help_frame = Frame(app,width=450,height=200,bg=calculator.WINDOW_BG,bd=1,relief=RAISED,);self.help_frame.place(x=320,y=5)
        help_text_pas_hide = """
            Developer Email: ambaaqeil@gmail.com
            Developer Email Password: {}
            Developer Descord: Abodi#0887
        """.format("*********")
        help_text_pas_show = """
            Developer Email: ambaaqeil@gmail.com
            Developer Email Password: {}
            Developer Descord: Abodi#0887
        """.format("No password, LOL")
        help_label = Label(self.help_frame,text=help_text_pas_hide,bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",10,""),);help_label.place(x=-10,y=0)
        
        def func_show():help_label.config(text=help_text_pas_show)
        
        pass_btn   = Button(self.help_frame,text=" Show password",bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,command=func_show,font=("Gill Sans",10,""));pass_btn.place(x=5,y=75)
        def destroy_frame(event):self.help_frame.destroy();app.bind("<Return>",self.func_enter_code)
        
        def close_enter(event):close_btn.config(bg=calculator.WHITE_BTNS_BG_HOVER)
        def close_leave(event):close_btn.config(bg=calculator.WHITE_BTNS_BG)
        close_btn = Button(self.help_frame,text="Close",width=15,height=1,bd=1,relief=GROOVE,bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG,activebackground=calculator.WHITE_BTNS_BG_ACTV,command=lambda:destroy_frame(event=""),font=("Gill Sans",12,""));close_btn.place(x=5,y=165)
        close_btn.bind("<Enter>",close_enter)
        close_btn.bind("<Leave>",close_leave)
        
        label = Label(self.help_frame,text="You can press Enter also",bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",10,""));label.place(x=145,y=165)
        
        app.unbind("<Return>",)
        app.bind("<Return>",destroy_frame)

    def func_add_code(self):
        try:
            casher.show_win.destroy()
        except:pass
        self.add_win = Tk()
        self.add_win.title("Add-Code")
        self.add_win.geometry("400x200")
        self.add_win.resizable(False,False)
        self.add_win.config(bg=calculator.WINDOW_BG)
        self.add_win.lift()
        try:
            self.show_win.destroy()
        except:pass
        self.goods_name_label = Label(self.add_win,text="Goods name:",bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",14,""));self.goods_name_label.place(x=0,y=0)
        self.goods_name = Entry(self.add_win,bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG,relief=GROOVE,justify=CENTER,font=("Gill Sans",14,""));self.goods_name.place(x=125,y=0)
            
        self.goods_price_label = Label(self.add_win,text="Goods price:",bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",14,""));self.goods_price_label.place(x=0,y=50)
        self.goods_price = Entry(self.add_win,bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG,relief=GROOVE,justify=CENTER,font=("Gill Sans",14,""));self.goods_price.place(x=125,y=50)
        def add():
            name = "Unnamed-"+str(len(casher.goods.items()))
            if self.goods_name.get().isspace():name = "Unnamed-"+str(len(casher.goods.items()))
            else                              :name = self.goods_name.get()
            if self.goods_price.get().isspace(): price = 0.0
            else                               : price = self.goods_price.get()
            casher.goods["0554"+str(len(casher.goods)+1)] = [price,name]
            TEXT = Label(self.add_win,text="You added ({})".format(name),bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",14,""));TEXT.place(x=20,y=160)
            def del_TEXT():TEXT.destroy()
            self.add_btn.config(state=DISABLED)
            self.add_win.after(500,del_TEXT)
            self.add_win.after(500,lambda:self.add_btn.config(state=NORMAL))
        self.add_btn = Button(self.add_win,text="Add",bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG,relief=GROOVE,command=add,height=2,width=24,font=("Gill Sans",12,""),disabledforeground="#212121");self.add_btn.place(x=20,y=100)
        self.add_win.bind(sequence="<Return>",func=add)
        self.add_win.mainloop()
    def func_show_goods(self):
        self.show_win = Tk()
        self.show_win.title("The Goods IDs Page-1")
        self.show_win.geometry("400x360")
        self.show_win.resizable(False,False)
        self.show_win.config(bg=calculator.WINDOW_BG)
        self.show_win.lift()
        self.page_counter = 0
        self.page_counter_title = 1
        self.re_fill()
        try:self.add_win.destroy()
        except:pass

        def func_right(event):
            self.re_fill()
            self.page_counter += 10
            if self.page_counter <= len(self.goods):
                self.page_counter_title += 1
                if self.page_counter+0 < len(self.goods):self.label_code_0.config(text=self.codes_list[0+self.page_counter])
                else:self.label_code_0.config(text="")
                if self.page_counter+1 < len(self.goods):self.label_code_1.config(text=self.codes_list[1+self.page_counter])
                else:self.label_code_1.config(text="")
                if self.page_counter+2 < len(self.goods):self.label_code_2.config(text=self.codes_list[2+self.page_counter])
                else:self.label_code_2.config(text="")
                if self.page_counter+3 < len(self.goods):self.label_code_3.config(text=self.codes_list[3+self.page_counter])
                else:self.label_code_3.config(text="")
                if self.page_counter+4 < len(self.goods):self.label_code_4.config(text=self.codes_list[4+self.page_counter])
                else:self.label_code_4.config(text="")
                if self.page_counter+5 < len(self.goods):self.label_code_5.config(text=self.codes_list[5+self.page_counter])
                else:self.label_code_5.config(text="")
                if self.page_counter+6 < len(self.goods):self.label_code_6.config(text=self.codes_list[6+self.page_counter])
                else:self.label_code_6.config(text="")
                if self.page_counter+7 < len(self.goods):self.label_code_7.config(text=self.codes_list[7+self.page_counter])
                else:self.label_code_7.config(text="")
                if self.page_counter+8 < len(self.goods):self.label_code_8.config(text=self.codes_list[8+self.page_counter])
                else:self.label_code_8.config(text="")
                if self.page_counter+9 < len(self.goods):self.label_code_9.config(text=self.codes_list[9+self.page_counter])
                else:self.label_code_9.config(text="")
                """======================================================================================================"""
                if self.page_counter+0 < len(self.goods):self.label_name_0.config(text=self.names_list[0+self.page_counter])
                else:self.label_name_0.config(text="")
                if self.page_counter+1 < len(self.goods):self.label_name_1.config(text=self.names_list[1+self.page_counter])
                else:self.label_name_1.config(text="")
                if self.page_counter+2 < len(self.goods):self.label_name_2.config(text=self.names_list[2+self.page_counter])
                else:self.label_name_2.config(text="")
                if self.page_counter+3 < len(self.goods):self.label_name_3.config(text=self.names_list[3+self.page_counter])
                else:self.label_name_3.config(text="")
                if self.page_counter+4 < len(self.goods):self.label_name_4.config(text=self.names_list[4+self.page_counter])
                else:self.label_name_4.config(text="")
                if self.page_counter+5 < len(self.goods):self.label_name_5.config(text=self.names_list[5+self.page_counter])
                else:self.label_name_5.config(text="")
                if self.page_counter+6 < len(self.goods):self.label_name_6.config(text=self.names_list[6+self.page_counter])
                else:self.label_name_6.config(text="")
                if self.page_counter+7 < len(self.goods):self.label_name_7.config(text=self.names_list[7+self.page_counter])
                else:self.label_name_7.config(text="")
                if self.page_counter+8 < len(self.goods):self.label_name_8.config(text=self.names_list[8+self.page_counter])
                else:self.label_name_8.config(text="")
                if self.page_counter+9 < len(self.goods):self.label_name_9.config(text=self.names_list[9+self.page_counter])
                else:self.label_name_9.config(text="")
                self.show_win.title("The Goods ID's Page-{}".format(str(self.page_counter_title)))
            else:self.page_counter -= 10
        def func_left(event):
            self.re_fill()
            if self.page_counter != 0:
                self.page_counter -= 10
                self.page_counter_title -= 1
                i = 0
                for label in codes_labels_list:
                    label.config(text=self.codes_list[i+self.page_counter])
                    i += 1
                i = 0
                for label in names_labels_list:
                    label.config(text=self.names_list[i+self.page_counter])
                    i += 1
                self.show_win.title("The Goods ID's Page-{}".format(str(self.page_counter_title)))

        self.label_code = Label(self.show_win,text="ID's",width=15,height=1,justify=CENTER,relief=GROOVE,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_code.place(x=5,y=0)
        self.label_name = Label(self.show_win,text="Name's",width=25,height=1,justify=CENTER,relief=GROOVE,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_name.place(x=160,y=0)

        self.label_code_0 = Label(self.show_win,text=self.codes_list[0+self.page_counter],width=15,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_code_0.place(x=5,y=30)
        self.label_code_1 = Label(self.show_win,text=self.codes_list[1+self.page_counter],width=15,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_code_1.place(x=5,y=60)
        self.label_code_2 = Label(self.show_win,text=self.codes_list[2+self.page_counter],width=15,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_code_2.place(x=5,y=90)
        self.label_code_3 = Label(self.show_win,text=self.codes_list[3+self.page_counter],width=15,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_code_3.place(x=5,y=120)
        self.label_code_4 = Label(self.show_win,text=self.codes_list[4+self.page_counter],width=15,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_code_4.place(x=5,y=150)
        self.label_code_5 = Label(self.show_win,text=self.codes_list[5+self.page_counter],width=15,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_code_5.place(x=5,y=180)
        self.label_code_6 = Label(self.show_win,text=self.codes_list[6+self.page_counter],width=15,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_code_6.place(x=5,y=210)
        self.label_code_7 = Label(self.show_win,text=self.codes_list[7+self.page_counter],width=15,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_code_7.place(x=5,y=240)
        self.label_code_8 = Label(self.show_win,text=self.codes_list[8+self.page_counter],width=15,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_code_8.place(x=5,y=270)
        self.label_code_9 = Label(self.show_win,text=self.codes_list[9+self.page_counter],width=15,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_code_9.place(x=5,y=300)

        self.label_name_0 = Label(self.show_win,text=self.names_list[0+self.page_counter],width=25,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_name_0.place(x=160,y=30)
        self.label_name_1 = Label(self.show_win,text=self.names_list[1+self.page_counter],width=25,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_name_1.place(x=160,y=60)
        self.label_name_2 = Label(self.show_win,text=self.names_list[2+self.page_counter],width=25,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_name_2.place(x=160,y=90)
        self.label_name_3 = Label(self.show_win,text=self.names_list[3+self.page_counter],width=25,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_name_3.place(x=160,y=120)
        self.label_name_4 = Label(self.show_win,text=self.names_list[4+self.page_counter],width=25,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_name_4.place(x=160,y=150)
        self.label_name_5 = Label(self.show_win,text=self.names_list[5+self.page_counter],width=25,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_name_5.place(x=160,y=180)
        self.label_name_6 = Label(self.show_win,text=self.names_list[6+self.page_counter],width=25,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_name_6.place(x=160,y=210)
        self.label_name_7 = Label(self.show_win,text=self.names_list[7+self.page_counter],width=25,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_name_7.place(x=160,y=240)
        self.label_name_8 = Label(self.show_win,text=self.names_list[8+self.page_counter],width=25,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_name_8.place(x=160,y=270)
        self.label_name_9 = Label(self.show_win,text=self.names_list[9+self.page_counter],width=25,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));self.label_name_9.place(x=160,y=300)

        codes_labels_list = [self.label_code_0,self.label_code_1,self.label_code_2,self.label_code_3,self.label_code_4,self.label_code_5,self.label_code_6,self.label_code_7,self.label_code_8,self.label_code_9,]
        names_labels_list = [self.label_name_0,self.label_name_1,self.label_name_2,self.label_name_3,self.label_name_4,self.label_name_5,self.label_name_6,self.label_name_7,self.label_name_8,self.label_name_9,]

        right_btn = Button(self.show_win,text="",width=7,height=1,justify=CENTER,relief=GROOVE,bd=2,bg=calculator.GRAY_BTNS_BG,fg=calculator.GRAY_BTNS_FG,activeforeground=calculator.GRAY_BTNS_FG,activebackground=calculator.GRAY_BTNS_BG_ACTV,command=lambda :func_right(event=""),font=("Gill Sans",10,""));right_btn.place(x=319,y=330)
        left_btn = Button(self.show_win,text="",width=7,height=1,justify=CENTER,relief=GROOVE,bd=2,bg=calculator.GRAY_BTNS_BG,fg=calculator.GRAY_BTNS_FG,activeforeground=calculator.GRAY_BTNS_FG,activebackground=calculator.GRAY_BTNS_BG_ACTV,command=lambda :func_left(event=""),font=("Gill Sans",10,""));left_btn.place(x=5,y=330)

        self.show_win.bind("<Left>",func_left)
        self.show_win.bind("<Right>",func_right)
        self.show_win.mainloop()
    def func_show_hide(self,event):
        if self.hidden == True:
            app.geometry("1010x540")
            self.hide_show_btn.config(text="")
            self.hidden = False
        elif self.hidden == False:
            app.geometry("710x540")
            self.hide_show_btn.config(text="")
            self.hidden = True
    def re_fill(self):
        self.codes_list = []
        self.price_list = []
        self.names_list = []
        for i in range(len(casher.goods.items())):
            self.codes_list.append(list(casher.goods.keys())[i])
            self.price_list.append(list(casher.goods.values())[i][0])
            self.names_list.append(list(casher.goods.values())[i][1])
calculator = CasherSystem.Calculator()
casher = CasherSystem(__version__="2.4.1",__data__="2023/1/14")
class Settings():
        def color_theme_func(theme):
            def configs():
                try:
                    app.config(bg=calculator.WINDOW_BG)
                    calculator.calculator_frame.config(bg = calculator.WINDOW_BG);
                    casher.invoice.config(bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG)
                    calculator.H3.config(bg=calculator.WINDOW_BG);
                    calculator.show.config(bg=calculator.WINDOW_BG,fg=calculator.GRAY_BTNS_FG)
                    calculator.show_s.config(bg=calculator.WINDOW_BG,fg=calculator.GRAY_BTNS_FG)
                    casher.hide_show_btn.config(bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG,activebackground=calculator.WHITE_BTNS_BG_ACTV,activeforeground=calculator.WHITE_BTNS_FG)
                    try:
                        casher.code_entry.config(bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG)
                        casher.code_entry_info.config(bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG)
                    except:pass
                    casher.bar_frame.config(bg=calculator.WHITE_BTNS_BG)
                    casher.enter_code_with_id.config(bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_BG_ACTV,activebackground=calculator.WHITE_BTNS_BG,activeforeground=calculator.WHITE_BTNS_FG)
                    casher.change_color.config(bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_BG_ACTV,activebackground=calculator.WHITE_BTNS_BG,activeforeground=calculator.WHITE_BTNS_FG)
                    casher.add_goods_btn.config(bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_BG_ACTV,activebackground=calculator.WHITE_BTNS_BG,activeforeground=calculator.WHITE_BTNS_FG)
                    casher.show_goods_btn.config(bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_BG_ACTV,activebackground=calculator.WHITE_BTNS_BG,activeforeground=calculator.WHITE_BTNS_FG)
                    casher.invoice_label.config(bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG)
                    casher.show_goods_quantity.config(bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG)
                    casher.show_goods_price.config(bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG)
                    casher.paid_up.config(bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG)
                    casher.paid_up_label.config(bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG)
                    try:
                        casher.add_win.config(bg=calculator.WINDOW_BG,)
                        casher.add_btn.config(bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG)
                        casher.goods_name_label.config(bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG)
                        casher.goods_price_label.config(bg=calculator.WINDOW_BG,fg=calculator.WHITE_BTNS_FG)
                        casher.goods_name.config(bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG)
                        casher.goods_price.config(bg=calculator.WHITE_BTNS_BG,fg=calculator.WHITE_BTNS_FG)
                    except:pass
                    try:
                        casher.show_win.destroy()
                        casher.add_win.destroy()
                    except:pass
                    for the_btn1 in calculator.white_btns_list:the_btn1.config(bg = calculator.WHITE_BTNS_BG,fg = calculator.WHITE_BTNS_FG,activebackground=calculator.WHITE_BTNS_BG_ACTV);
                    for the_btn2 in calculator.gray_btns_list:the_btn2.config(fg = calculator.GRAY_BTNS_FG,bg = calculator.GRAY_BTNS_BG,activebackground=calculator.GRAY_BTNS_BG_ACTV);
                except:
                    if   casher.color_theme_var == "<d>":calculator.WINDOW_BG        = "#121212";calculator.WHITE_BTNS_BG = "#3B3B3B";calculator.WHITE_BTNS_FG = "#F0F0F0";calculator.WHITE_BTNS_BG_ACTV = "#202020";calculator.WHITE_BTNS_BG_HOVER = "#151515";calculator.GRAY_BTNS_BG  = "#222222";calculator.GRAY_BTNS_FG  = "#F0F0F0";calculator.GRAY_BTNS_BG_ACTV  = "#101010";calculator.GRAY_BTNS_BG_HOVER  = "#333333";calculator.calculator_frame.config(bd=2);casher.color_theme_var = "<d>"
                    elif casher.color_theme_var == "<ad>":calculator.WINDOW_BG       = "#000C18";calculator.WHITE_BTNS_BG = "#051336";calculator.WHITE_BTNS_FG = "#6688C1";calculator.WHITE_BTNS_BG_ACTV = "#071B4C";calculator.WHITE_BTNS_BG_HOVER = "#0B2975";calculator.GRAY_BTNS_BG  = "#060621";calculator.GRAY_BTNS_FG  = "#6688C1";calculator.GRAY_BTNS_BG_ACTV  = "#0A0A36";calculator.GRAY_BTNS_BG_HOVER  = "#161673";calculator.calculator_frame.config(bd=2);casher.color_theme_var = "<ad>"
                    elif casher.color_theme_var == "<kd>":calculator.WINDOW_BG       = "#221A0F";calculator.WHITE_BTNS_BG = "#68563F";calculator.WHITE_BTNS_FG = "#DC3958";calculator.WHITE_BTNS_BG_ACTV = "#826C4F";calculator.WHITE_BTNS_BG_HOVER = "#756148";calculator.GRAY_BTNS_BG  = "#362712";calculator.GRAY_BTNS_FG  = "#DC3958";calculator.GRAY_BTNS_BG_ACTV  = "#4F391A";calculator.GRAY_BTNS_BG_HOVER  = "#423016";calculator.calculator_frame.config(bd=2);casher.color_theme_var = "<kd>"
                    elif casher.color_theme_var == "<mdd>":calculator.WINDOW_BG      = "#1E1F1C";calculator.WHITE_BTNS_BG = "#4C4C49";calculator.WHITE_BTNS_FG = "#6289B4";calculator.WHITE_BTNS_BG_ACTV = "#656661";calculator.WHITE_BTNS_BG_HOVER = "#6F706B";calculator.GRAY_BTNS_BG  = "#272822";calculator.GRAY_BTNS_FG  = "#6289B4";calculator.GRAY_BTNS_BG_ACTV  = "#414238";calculator.GRAY_BTNS_BG_HOVER  = "#34362E";calculator.calculator_frame.config(bd=2);casher.color_theme_var = "<mdd>"
                    elif casher.color_theme_var == "<l>":calculator.WINDOW_BG       = "#F0F0F0";calculator.WHITE_BTNS_BG = "#FFFFFF";calculator.WHITE_BTNS_FG = "#000000";calculator.WHITE_BTNS_BG_ACTV = "#D0D0D0";calculator.WHITE_BTNS_BG_HOVER = "#F0F0F0";calculator.GRAY_BTNS_BG  = "#E0E0E0";calculator.GRAY_BTNS_FG  = "#000000";calculator.GRAY_BTNS_BG_ACTV  = "#B0B0B0";calculator.GRAY_BTNS_BG_HOVER  = "#D0D0D0";calculator.calculator_frame.config(bd=4);casher.color_theme_var = "<l>"
                    elif casher.color_theme_var == "<qul>":calculator.WINDOW_BG     = "#DADAD9";calculator.WHITE_BTNS_BG = "#F8F8F2";calculator.WHITE_BTNS_FG = "#1E0F26";calculator.WHITE_BTNS_BG_ACTV = "#D3DBCD";calculator.WHITE_BTNS_BG_HOVER = "#D9D9D9";calculator.GRAY_BTNS_BG  = "#CFCFCC";calculator.GRAY_BTNS_FG  = "#1E0F26";calculator.GRAY_BTNS_BG_ACTV  = "#BBC2B6";calculator.GRAY_BTNS_BG_HOVER  = "#BFBFBF";calculator.calculator_frame.config(bd=4);casher.color_theme_var = "<qul>"
                    elif casher.color_theme_var == "<sal>":calculator.WINDOW_BG     = "#F2E8BF";calculator.WHITE_BTNS_BG = "#FFF2BD";calculator.WHITE_BTNS_FG = "#1E0F26";calculator.WHITE_BTNS_BG_ACTV = "#EBDBB2";calculator.WHITE_BTNS_BG_HOVER = "#EAEDBB";calculator.GRAY_BTNS_BG  = "#D9CDA0";calculator.GRAY_BTNS_FG  = "#1E0F26";calculator.GRAY_BTNS_BG_ACTV  = "#D1C39F";calculator.GRAY_BTNS_BG_HOVER  = "#D1D4A7";calculator.calculator_frame.config(bd=4);casher.color_theme_var = "<sal>"
                    elif casher.color_theme_var == "<sol>":calculator.WINDOW_BG     = "#E6DFCF";calculator.WHITE_BTNS_BG = "#EEE8D5";calculator.WHITE_BTNS_FG = "#534A30";calculator.WHITE_BTNS_BG_ACTV = "#EBDBB2";calculator.WHITE_BTNS_BG_HOVER = "#FFF4D9";calculator.GRAY_BTNS_BG  = "#D9D2C2";calculator.GRAY_BTNS_FG  = "#534A30";calculator.GRAY_BTNS_BG_ACTV  = "#D1C39F";calculator.GRAY_BTNS_BG_HOVER  = "#E6DCC3";calculator.calculator_frame.config(bd=4);casher.color_theme_var = "<sol>"
                    configs()
                    messagebox.showerror("Error","there was an error in color input\nso we reset the color theme ( ;")
            def apply_func(option):
                if   option == "W|C"      :calculator.WINDOW_BG           = window_color.get();window_color_win.destroy()
                
                elif option == "B|B|C"    :calculator.GRAY_BTNS_BG        = btn_bg_color.get();btn_bg_color_win.destroy()
                elif option == "B|B|C|L"  :calculator.WHITE_BTNS_BG       = btn_bg_color_light.get();btn_bg_color_light_win.destroy()
                
                elif option == "B|H|B|C"  :calculator.GRAY_BTNS_BG_HOVER  = btn_hover_bg_color.get();btn_hover_bg_color_win.destroy()
                elif option == "B|H|B|C|L":calculator.WHITE_BTNS_BG_HOVER = btn_hover_bg_color_light.get();btn_hover_bg_color_light_win.destroy()
                
                elif option == "B|A|B|C"  :calculator.GRAY_BTNS_BG_ACTV   = btn_actv_bg_color.get();btn_actv_bg_color_win.destroy()
                elif option == "B|A|B|C|L":calculator.WHITE_BTNS_BG_ACTV  = btn_actv_bg_color_light.get();btn_actv_bg_color_light_win.destroy()
                
                elif option == "B|F|C"    :calculator.WHITE_BTNS_FG       = btn_fg_color.get();calculator.GRAY_BTNS_FG = btn_fg_color.get();btn_fg_color_win.destroy()
                configs()
            if   theme == "Dark":calculator.WINDOW_BG        = "#121212";calculator.WHITE_BTNS_BG = "#3B3B3B";calculator.WHITE_BTNS_FG = "#F0F0F0";calculator.WHITE_BTNS_BG_ACTV = "#202020";calculator.WHITE_BTNS_BG_HOVER = "#151515";calculator.GRAY_BTNS_BG  = "#222222";calculator.GRAY_BTNS_FG  = "#F0F0F0";calculator.GRAY_BTNS_BG_ACTV  = "#101010";calculator.GRAY_BTNS_BG_HOVER  = "#333333";calculator.calculator_frame.config(bd=2);casher.color_theme_var = "<d>"
            elif theme == "ADark":calculator.WINDOW_BG       = "#000C18";calculator.WHITE_BTNS_BG = "#051336";calculator.WHITE_BTNS_FG = "#6688C1";calculator.WHITE_BTNS_BG_ACTV = "#071B4C";calculator.WHITE_BTNS_BG_HOVER = "#0B2975";calculator.GRAY_BTNS_BG  = "#060621";calculator.GRAY_BTNS_FG  = "#6688C1";calculator.GRAY_BTNS_BG_ACTV  = "#0A0A36";calculator.GRAY_BTNS_BG_HOVER  = "#161673";calculator.calculator_frame.config(bd=2);casher.color_theme_var = "<ad>"
            elif theme == "KDark":calculator.WINDOW_BG       = "#221A0F";calculator.WHITE_BTNS_BG = "#68563F";calculator.WHITE_BTNS_FG = "#DC3958";calculator.WHITE_BTNS_BG_ACTV = "#826C4F";calculator.WHITE_BTNS_BG_HOVER = "#756148";calculator.GRAY_BTNS_BG  = "#362712";calculator.GRAY_BTNS_FG  = "#DC3958";calculator.GRAY_BTNS_BG_ACTV  = "#4F391A";calculator.GRAY_BTNS_BG_HOVER  = "#423016";calculator.calculator_frame.config(bd=2);casher.color_theme_var = "<kd>"
            elif theme == "MDDark":calculator.WINDOW_BG      = "#1E1F1C";calculator.WHITE_BTNS_BG = "#4C4C49";calculator.WHITE_BTNS_FG = "#6289B4";calculator.WHITE_BTNS_BG_ACTV = "#656661";calculator.WHITE_BTNS_BG_HOVER = "#6F706B";calculator.GRAY_BTNS_BG  = "#272822";calculator.GRAY_BTNS_FG  = "#6289B4";calculator.GRAY_BTNS_BG_ACTV  = "#414238";calculator.GRAY_BTNS_BG_HOVER  = "#34362E";calculator.calculator_frame.config(bd=2);casher.color_theme_var = "<mdd>"
            
            elif theme == "Light":calculator.WINDOW_BG       = "#F0F0F0";calculator.WHITE_BTNS_BG = "#FFFFFF";calculator.WHITE_BTNS_FG = "#000000";calculator.WHITE_BTNS_BG_ACTV = "#D0D0D0";calculator.WHITE_BTNS_BG_HOVER = "#F0F0F0";calculator.GRAY_BTNS_BG  = "#E0E0E0";calculator.GRAY_BTNS_FG  = "#000000";calculator.GRAY_BTNS_BG_ACTV  = "#B0B0B0";calculator.GRAY_BTNS_BG_HOVER  = "#D0D0D0";calculator.calculator_frame.config(bd=4);casher.color_theme_var = "<l>"
            elif theme == "QULight":calculator.WINDOW_BG     = "#DADAD9";calculator.WHITE_BTNS_BG = "#F8F8F2";calculator.WHITE_BTNS_FG = "#1E0F26";calculator.WHITE_BTNS_BG_ACTV = "#D3DBCD";calculator.WHITE_BTNS_BG_HOVER = "#D9D9D9";calculator.GRAY_BTNS_BG  = "#CFCFCC";calculator.GRAY_BTNS_FG  = "#1E0F26";calculator.GRAY_BTNS_BG_ACTV  = "#BBC2B6";calculator.GRAY_BTNS_BG_HOVER  = "#BFBFBF";calculator.calculator_frame.config(bd=4);casher.color_theme_var = "<qul>"
            elif theme == "SALight":calculator.WINDOW_BG     = "#F2E8BF";calculator.WHITE_BTNS_BG = "#FFF2BD";calculator.WHITE_BTNS_FG = "#1E0F26";calculator.WHITE_BTNS_BG_ACTV = "#EBDBB2";calculator.WHITE_BTNS_BG_HOVER = "#EAEDBB";calculator.GRAY_BTNS_BG  = "#D9CDA0";calculator.GRAY_BTNS_FG  = "#1E0F26";calculator.GRAY_BTNS_BG_ACTV  = "#D1C39F";calculator.GRAY_BTNS_BG_HOVER  = "#D1D4A7";calculator.calculator_frame.config(bd=4);casher.color_theme_var = "<sal>"
            elif theme == "SOLight":calculator.WINDOW_BG     = "#E6DFCF";calculator.WHITE_BTNS_BG = "#EEE8D5";calculator.WHITE_BTNS_FG = "#534A30";calculator.WHITE_BTNS_BG_ACTV = "#EBDBB2";calculator.WHITE_BTNS_BG_HOVER = "#FFF4D9";calculator.GRAY_BTNS_BG  = "#D9D2C2";calculator.GRAY_BTNS_FG  = "#534A30";calculator.GRAY_BTNS_BG_ACTV  = "#D1C39F";calculator.GRAY_BTNS_BG_HOVER  = "#E6DCC3";calculator.calculator_frame.config(bd=4);casher.color_theme_var = "<sol>"
            
            elif theme == "W|C":
                window_color_win = Tk();window_color_win.geometry("500x75");window_color_win.title("Enter window color");window_color_win.config(bg=calculator.WINDOW_BG)
                    
                label = Label(window_color_win,text="Enter colors in HEX format like: (#F0F0F0) or (white)",bg=calculator.WINDOW_BG,fg=calculator.GRAY_BTNS_FG);label.pack()
                window_color = Entry(window_color_win,justify=LEFT,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,font=("Gill Sans",12,""));window_color.pack()
                apply_btn = Button(window_color_win,text="Apply",bg=calculator.WHITE_BTNS_BG,command=lambda:apply_func("W|C"),fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",12,""));apply_btn.pack()
                window_color_win.mainloop()
            elif theme == "B|B|C":
                btn_bg_color_win = Tk();btn_bg_color_win.geometry("500x75");btn_bg_color_win.title("Enter button background color");btn_bg_color_win.config(bg=calculator.WINDOW_BG)
                
                label = Label(btn_bg_color_win,text="Enter color in HEX format like: (#FFFFFF) or (white)",bg=calculator.WINDOW_BG,fg=calculator.GRAY_BTNS_FG,);label.pack()
                btn_bg_color = Entry(btn_bg_color_win,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,justify=LEFT,font=("Gill Sans",12,""));btn_bg_color.pack()
                apply_btn = Button(btn_bg_color_win,text="Apply",bg=calculator.WHITE_BTNS_BG,command=lambda:apply_func("B|B|C"),fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",12,""));apply_btn.pack()
                btn_bg_color_win.mainloop()
            elif theme == "B|B|C|L":
                btn_bg_color_light_win = Tk();btn_bg_color_light_win.geometry("500x75");btn_bg_color_light_win.title("Enter button background color light");btn_bg_color_light_win.config(bg=calculator.WINDOW_BG)
                
                label = Label(btn_bg_color_light_win,text="Enter color in HEX format like: (#FFFFFF) or (white)",bg=calculator.WINDOW_BG,fg=calculator.GRAY_BTNS_FG);label.pack()
                btn_bg_color_light = Entry(btn_bg_color_light_win,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,justify=LEFT,font=("Gill Sans",12,""));btn_bg_color_light.pack()
                apply_btn = Button(btn_bg_color_light_win,text="Apply",bg=calculator.WHITE_BTNS_BG,command=lambda:apply_func("B|B|C|L"),fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",12,""));apply_btn.pack()
                btn_bg_color_light_win.mainloop()
            elif theme == "B|H|B|C":
                btn_hover_bg_color_win = Tk();btn_hover_bg_color_win.geometry("500x75");btn_hover_bg_color_win.title("Enter button hover background color");btn_hover_bg_color_win.config(bg=calculator.WINDOW_BG)
                    
                label = Label(btn_hover_bg_color_win,text="Enter color in HEX format like: (#FFFFFF) or (white)",bg=calculator.WINDOW_BG,fg=calculator.GRAY_BTNS_FG);label.pack()
                btn_hover_bg_color = Entry(btn_hover_bg_color_win,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,justify=LEFT,font=("Gill Sans",12,""));btn_hover_bg_color.pack()
                apply_btn = Button(btn_hover_bg_color_win,text="Apply",bg=calculator.WHITE_BTNS_BG,command=lambda:apply_func("B|H|B|C"),fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",12,""));apply_btn.pack()
                btn_hover_bg_color_win.mainloop()
            elif theme == "B|H|B|C|L":
                btn_hover_bg_color_light_win = Tk();btn_hover_bg_color_light_win.geometry("500x75");btn_hover_bg_color_light_win.title("Enter button hover background color light");btn_hover_bg_color_light_win.config(bg=calculator.WINDOW_BG)
                
                label = Label(btn_hover_bg_color_light_win,text="Enter color in HEX format like: (#FFFFFF) or (white)",bg=calculator.WINDOW_BG,fg=calculator.GRAY_BTNS_FG);label.pack()
                btn_hover_bg_color_light = Entry(btn_hover_bg_color_light_win,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,justify=LEFT,font=("Gill Sans",12,""));btn_hover_bg_color_light.pack()
                apply_btn = Button(btn_hover_bg_color_light_win,text="Apply",bg=calculator.WHITE_BTNS_BG,command=lambda:apply_func("B|H|B|C|L"),fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",12,""));apply_btn.pack()
                btn_hover_bg_color_light_win.mainloop()
            elif theme == "B|A|B|C":
                btn_actv_bg_color_win = Tk();btn_actv_bg_color_win.geometry("500x75");btn_actv_bg_color_win.title("Enter button active background color");btn_actv_bg_color_win.config(bg=calculator.WINDOW_BG)
                
                label = Label(btn_actv_bg_color_win,text="Enter color in HEX format like: (#FFFFFF) or (white)",bg=calculator.WINDOW_BG,fg=calculator.GRAY_BTNS_FG);label.pack()
                btn_actv_bg_color = Entry(btn_actv_bg_color_win,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,justify=LEFT,font=("Gill Sans",12,""));btn_actv_bg_color.pack()
                apply_btn = Button(btn_actv_bg_color_win,text="Apply",bg=calculator.WHITE_BTNS_BG,command=lambda:apply_func("B|A|B|C"),fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",12,""));apply_btn.pack()
                btn_actv_bg_color_win.mainloop()
            elif theme == "B|A|B|C|L":
                btn_actv_bg_color_light_win = Tk();btn_actv_bg_color_light_win.geometry("500x75");btn_actv_bg_color_light_win.title("Enter button active background color light");btn_actv_bg_color_light_win.config(bg=calculator.WINDOW_BG)
                    
                label = Label(btn_actv_bg_color_light_win,text="Enter color in HEX format like: (#FFFFFF) or (white)",bg=calculator.WINDOW_BG,fg=calculator.GRAY_BTNS_FG);label.pack()
                btn_actv_bg_color_light = Entry(btn_actv_bg_color_light_win,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,justify=LEFT,font=("Gill Sans",12,""));btn_actv_bg_color_light.pack()
                apply_btn = Button(btn_actv_bg_color_light_win,text="Apply",bg=calculator.WHITE_BTNS_BG,command=lambda:apply_func("B|A|B|C|L"),fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",12,""));apply_btn.pack()
                btn_actv_bg_color_light_win.mainloop()
            elif theme == "B|F|C":
                btn_fg_color_win = Tk();btn_fg_color_win.geometry("500x75");btn_fg_color_win.title("Enter button foreground color");btn_fg_color_win.config(bg=calculator.WINDOW_BG)
                
                label = Label(btn_fg_color_win,text="Enter color in HEX format like: (#FFFFFF) or (white)",bg=calculator.WINDOW_BG,fg=calculator.GRAY_BTNS_FG);label.pack()
                btn_fg_color = Entry(btn_fg_color_win,bg=calculator.WHITE_BTNS_BG,fg=calculator.GRAY_BTNS_FG,justify=LEFT,font=("Gill Sans",12,""));btn_fg_color.pack()
                apply_btn = Button(btn_fg_color_win,text="Apply",bg=calculator.WHITE_BTNS_BG,command=lambda:apply_func("B|F|C"),fg=calculator.WHITE_BTNS_FG,font=("Gill Sans",12,""));apply_btn.pack()
                btn_fg_color_win.mainloop()
            configs()
if __name__ == "__main__":
    app.mainloop()