#This program generates a Home Automation System(HAS) panel.
#It will manually report the current occupancy state of the room.
#And it will provide an option to user to set the required temperature.
#The recordings will go to the file output.txt
#
#Written on 04/26/2018
#


import Tkinter as tk
import ttk
import time



def hello_world():
	with open("output.txt",'a+') as txta:
		txta.write(time.asctime(time.localtime())+" : The occupancy state is : 1\n")
	window1=tk.Tk()
	window1.title("HOME AUTOMATION SYSTEM")
	window1.grid()
	window1.geometry("620x100")
	tk.Label(window1,text='').pack()
	
	label=tk.Label(window1,text='The occupancy state has been changed to "occupied" successfully.')
	label.pack()

def hello_world1():
	with open("output.txt",'a+') as txta:
		txta.write(time.asctime(time.localtime())+" : The occupancy state is : 0\n")
	window1=tk.Tk()
	window1.title("HOME AUTOMATION SYSTEM")
	window1.grid()
	window1.geometry("620x100")
	tk.Label(window1,text='').pack()
	
	label=tk.Label(window1,text='The occupancy state has been changed to "unoccupied" successfully.')
	label.pack()
	
def set_temp(s_temp):
	with open("output.txt",'a+') as txta:
		txta.write(time.asctime(time.localtime())+" : The comfortable temperature is : "+s_temp)
	window1=tk.Tk()
	window1.title("HOME AUTOMATION SYSTEM")
	window1.grid()
	window1.geometry("620x100")
	tk.Label(window1,text='').pack()
	
	label=tk.Label(window1,text='The comfortable temperature has been changed successfully.')
	label.pack()
	
def hello_world2():
	window1=tk.Tk()
	window1.title("HOME AUTOMATION SYSTEM")
	window1.grid()
	window1.geometry("440x210")
	frame4=tk.Frame(window1)
	frame4.pack()
	tk.Label(frame4,text="\n\nPlease enter the required comfortable temperature:\n").grid()
	tk.Label(frame4,text="Temperature:").grid(sticky="W")
	e1=tk.Entry(frame4)
	e1.grid(row=1,column=1,sticky="W")
	tk.Label(frame4,text="").grid()
	framep=tk.Frame(window1)
	framep.pack()
	tk.Button(framep, activeforeground="#000fff000", bg="lightgrey", text="Set", padx=10, pady=3, command= lambda: set_temp(e1.get())).grid()
	
	
	
	
window=tk.Tk()
window.title("HOME AUTOMATION SYSTEM")
window.geometry("440x410")

framec=tk.Frame(window)
framec.pack(fill="both")
ttk.Label(framec,text="").pack()
tk.Label(framec,text="HOME AUTOMATION SYSTEM",padx=10,pady=10,font=('Times', '12', 'bold')).pack()
ttk.Label(framec,text="").pack()

nb1=ttk.Notebook(framec,padding=10)
framea=ttk.Frame(nb1)
nb1.add(framea,text="HEATER")
nb1.pack(expand=1, fill="both")
ttk.Label(framea,text="").pack()
ttk.Label(framea,text="").pack()

frame1=tk.LabelFrame(framea,cursor="top_left_corner",text="Choose an option",padx=20,pady=20,bd=5)
frame1.pack(fill="y")
ttk.Label(framea,text="").pack()
ttk.Label(framea,text="").pack()

b = tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="I am IN", padx=40, pady=5, command=hello_world)
b.pack(fill="both")
tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="I am OUT", padx=40, pady=5, command=hello_world1).pack(fill="both")
b1 = tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="Set Temperature", padx=40, pady=5, command=hello_world2)
b1.pack(fill="both")


window.mainloop()