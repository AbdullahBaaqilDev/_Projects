#Mad with abodi2098
#-----------------------|
from tkinter import *




the_nums = []
the_place = 20
the_math = ""
#DELETE FUNCTION----
def yf():
    global the_place
    if the_place < 20 :
        zf()
    the_place -= 20
    if len(the_nums) > 0:
        del(the_nums[-1])

    show_num = Label(app,text="  ",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
#Clear FUNCTION
def zf():
    global the_place
    for y in range(len(the_nums)):
        del(the_nums[-1])
        the_place -= 20
    the_place = 20
    white_color()


#-----------------
#numder 1 FUNCTION
def af():
    the_nums.append("1")
    global the_place
    

    show_num = Label(app,text="1",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
#numder 2 FUNCTION
def bf():
    (the_nums.append("2"))
    global the_place


    show_num = Label(app,text="2",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
#numder 3 FUNCTION
def cf():
    (the_nums.append("3"))
    global the_place


    show_num = Label(app,text="3",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
#numder 4 FUNCTION
def df():
    (the_nums.append("4"))
    global the_place


    show_num = Label(app,text="4",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
#numder 5 FUNCTION
def ef():
    (the_nums.append("5"))
    global the_place


    show_num = Label(app,text="5",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
#numder 6 FUNCTION
def ff():
    (the_nums.append("6"))
    global the_place


    show_num = Label(app,text="6",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
#numder 7 FUNCTION
def gf():
    (the_nums.append("7"))
    global the_place


    show_num = Label(app,text="7",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
#numder 8 FUNCTION
def hf():
    (the_nums.append("8"))
    global the_place


    show_num = Label(app,text="8",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
#numder 9 FUNCTION
def ih():
    (the_nums.append("9"))
    global the_place


    show_num = Label(app,text="9",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
#numder 0 FUNCTION
def jf():
    (the_nums.append("0"))
    global the_place


    show_num = Label(app,text="0",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
# (.) FUNCTION
def dot():
    global the_place
    (the_nums.append("."))


    show_num = Label(app,text=".",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 10
# (Equal) FUNCTION
def kf():

    global the_place
    global the_math
    global the_nums


    for m in the_nums:
        the_math += m
    the_equal = eval(the_math)
    zf()
    show_e = Label(app,text=str(the_equal),bg="white",font=("",20,""))
    show_e.place(x=20,y=70)
    the_nums = [str(eval(the_math))]
    the_math = ""
    the_place = len(the_nums[0]) * 20
# (+) FUNCTION
def mf():
    (the_nums.append("+"))
    global the_place


    show_num = Label(app,text="+",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
# (-) FUNCTION
def nf():
    (the_nums.append("-"))
    global the_place


    show_num = Label(app,text="-",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
# (x) FUNCTION
def of():
    (the_nums.append("*"))
    global the_place


    show_num = Label(app,text="x",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
# (÷) FUNCTION
def pf():
    (the_nums.append("/"))
    global the_place


    show_num = Label(app,text="÷",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 20
# (%) FUNCTION
def qf():
    (the_nums.append("%"))
    global the_place


    show_num = Label(app,text="%",bg="white",font=("",20,""))
    show_num.place(x=the_place,y=70)
    the_place += 27
#( FUNCTION
def rf():
    global the_place
    if the_nums[-1] != "*" or "%" or "/" or "+" or "-":
        (the_nums.append("*"))
        (the_nums.append("("))

        show_num = Label(app,text="(",bg="white",font=("",20,""))
        show_num.place(x=the_place,y=70)
        the_place += 20
    else:
        (the_nums.append("("))

        show_num = Label(app,text="(",bg="white",font=("",20,""))
        show_num.place(x=the_place,y=70)
        the_place += 20
#) FUNCTION
def wf():
    global the_place
    if the_nums[-1] != "*" or "%" or "/" or "+" or "-":
        (the_nums.append(")"))
        (the_nums.append("*"))

        show_num = Label(app,text=")",bg="white",font=("",20,""))
        show_num.place(x=the_place,y=70)
        the_place += 20
        show_num = Label(app,text="×",bg="white",font=("",20,""))
        show_num.place(x=the_place,y=70)
        the_place += 20
    else:
        (the_nums.append(")"))

        show_num = Label(app,text=")",bg="white",font=("",20,""))
        show_num.place(x=the_place,y=70)
        the_place += 20

app = Tk()
app.geometry("400x480")
app.title("Calculater Mad with abodi2098")
app.resizable(False,False)

whited = Label(app,text="\n \n",)
whited.pack(fill = "x")
def white_color():



    whitei = Label(app,text="                                                                                                                                                                                                                        \n                                                                                                                                             \n                                                                                                                                             \n                                                                                                                                             \n",bg="white")
    whitei.place(x=1,y=50)
white_color()

#11111111111111111111111
btn1 = Button(app,
text=" 1 ",
font=("tajawal",
25,
""),
bg="gray",
command = af)
btn1.place(x=80,y=340)
#222222222222222222222222222
btn2 = Button(app,
text=" 2 ",
font=("tajawal",
25,
""),
bg="gray",
command = bf)
btn2.place(x=145,y=340)
#33333333333333333333333
btn3 = Button(app,
text=" 3 ",
font=("tajawal",
25,
""),
bg="gray",
command = cf)
btn3.place(x=210,y=340)
#44444444444444444444
btn4 = Button(app,
text=" 4 ",
font=("tajawal",
25,
""),
bg="gray",
command = df)
btn4.place(x=80,y=273)
#5555555555555555555555555
btn5 = Button(app,
text=" 5 ",
font=("tajawal",
25,
""),
bg="gray",
command = ef)
btn5.place(x=145,y=273)
#66666666666666666666
btn6 = Button(app,
text=" 6 ",
font=("tajawal",
25,
""),
bg="gray",
command = ff)
btn6.place(x=210,y=273)
#77777777777777777
btn7 = Button(app,
text=" 7 ",
font=("tajawal",
25,
""),
bg="gray",
command = gf)
btn7.place(x=80,y=206)
#88888888888888
btn8 = Button(app,
text=" 8 ",
font=("tajawal",
25,
""),
bg="gray",
command = hf)
btn8.place(x=145,y=206)
#9999999999999
btn9 = Button(app,
text=" 9 ",
font=("tajawal",
25,
""),
bg="gray",
command = ih)
btn9.place(x=210,y=206)
#00000000000000
btn0 = Button(app,
text=" 0 ",
font=("tajawal",
25,
""),
bg="gray",
command = jf)
btn0.place(x=145,y=407)
#.....................
btnb = Button(app,
text=" .  ",
font=("tajawal",
25,
""),
bg="gray",
command = dot)
btnb.place(x=210,y=407)
#==============
btne = Button(app,
text=" = ",
font=("tajawal",
25,
""),
bg="gray",
command = kf)
btne.place(x=275,y=407)
#++++++++++++++++++
btnp = Button(app,
text=" + ",
font=("tajawal",
25,
""),
bg="gray",
command = mf)
btnp.place(x=275,y=340)
#---------------
btnn = Button(app,
text=" - ",
font=("tajawal",
25,
""),
bg="gray",
command = nf,
width=3)
btnn.place(x=275,y=273)
#xxxxxxxxxxxxxxxxxxxxxxxxx
btnx = Button(app,
text=" × ",
font=("tajawal",
25,
""),
bg="gray",
command = of)
btnx.place(x=275,y=206)
#"%%%%%%%%%%%%%%%%%%%"
btnh = Button(app,
text=" % ",
font=("tajawal",
25,
""),
bg="gray",
command = qf)
btnh.place(x=210,y=139)
#÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷
btnd = Button(app,
text=" ÷ ",
font=("tajawal",
25,
""),
bg="gray",
command = pf)
btnd.place(x=276,y=139)
#Clear
btnc = Button(app,
text=" c ",
font=("tajawal",25,""),
bg="gray",
command = zf)
btnc.place(x=80,y=139)
#Back Space
btndl = Button(app,
text=" <=",
font=("tajawal",
25,
""),
bg="gray",
command = yf)
btndl.place(x=144,y=139)
#(((((((((((((((((
btnq1 = Button(app,
text="(",
font=("tajawal",
25,
""),
bg="gray",
command = rf)
btnq1.place(x=80,y=407)
#)))))))))))))))))
btnq2 = Button(app,
text=")",
font=("tajawal",
25,
""),
bg="gray",
command = wf)
btnq2.place(x=110,y=407)
app.mainloop()