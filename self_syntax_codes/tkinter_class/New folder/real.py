import gui
import Tkinter as tk

b_args = { 'activeforeground' : '#000fff000', 'bg' : 'lightgrey'}
w1=tk.Tk()
f1=gui.page(w1)
f1.pack()

def print_name():
	f1.f_clear()
	f2=gui.page(w1)
	f2.pack()
	f2.lb_create("The button has been clicked..").pack()
	
	
f1.b_create("Proceed",print_name,**b_args).pack()


w1.mainloop()