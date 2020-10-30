import Tkinter as tk

def show():
	frame2=tk.Frame(window)
	frame2.grid()
	tk.Label(frame2,text="My first name is {0} and last is {1}\n".format(e1.get(),e2.get())).grid()
	

window=tk.Tk()
window.geometry("300x400")
frame1=tk.Frame(window,bd=5)
frame1.grid(row=2,column=2)

tk.Label(frame1,text="First Name:").grid(row=1,sticky="W")
tk.Label(frame1,text="Second Name:").grid(row=2,sticky="W")

e1=tk.Entry(frame1)
e1.grid(row=1,column=2)
e2=tk.Entry(frame1)
e2.grid(row=2,column=2)

tk.Button(frame1,text="Show",command=show).grid()


window.mainloop()