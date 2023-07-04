import tkinter as tk
import random as ran

window = tk.Tk()
window.title("Luck Wheel")
window.geometry("350x300+10+10")
# window.resizable(False,False)


class Chooser():
    def __init__(self):
        self.thing_index = 0
        self.step_label = tk.Label(window,text = "Set things number");self.step_label.pack()
        self.things_entry = tk.Entry(window,);self.things_entry.pack()
        self.choosed_label = tk.Label(window,text = "");self.choosed_label.pack()
        self.things_list = []
        window.bind("<Return>",lambda var:self.set_things_number())
    
    def set_things_number(self):
        self.things_number = int(self.things_entry.get())
        self.things_entry.delete(0,tk.END)
        self.step_label.config(text = "enter thing number {}".format(self.thing_index+1))
        window.unbind("<Return>")
        window.bind("<Return>",lambda var:self.add_thing(self.things_entry.get()))
        

    def add_thing(self,thing):
        if self.things_number > 0:
            self.things_entry.delete(0,tk.END)
            self.things_list.append(thing)
            self.thing_index += 1
            self.things_number -= 1
            self.step_label.config(text = "enter thing number {}".format(self.thing_index+1))
        if self.things_number <= 0:
            self.things_entry.delete(0,tk.END)
            self.things_entry.destroy()
            window.unbind("<Return>")
            self.step_label.config(text = "press enter to choose".format(self.things_number))
            window.bind("<Return>",lambda var:self.show_choosed())

    def show_choosed(self):
        print(self.things_list)
        choosed = ran.choice(self.things_list)
        self.choosed_label.config(text = choosed)

app = Chooser()
window.mainloop()