#Mad with abodi2098
#-----------------------|

print("The math is[+ - * /]")

def the_start():

    start = input("")
    print("=" + str(eval(start)))
    want()


def want():
    agien = input("do you want to calculate another number (yes|no)")
    if agien.lower() == "yes":
        the_start()
    elif agien.lower() == "no":
        print("OK, See you soon")

the_start()