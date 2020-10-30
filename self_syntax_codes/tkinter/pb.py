import Tkinter as tk
import ttk
import time

window=tk.Tk()
window.title("Mphasis Automation App")
window.geometry("300x400")

def create_user(u_name):
	frame2=tk.Frame(window)
	frame2.pack()
	pb=ttk.Progressbar(frame2,mode="indeterminate")
	pb.grid()
	pb.start()
	for _ in range(50):
		time.sleep(0.1)
		pb.step(10)
		pb.update_idletasks()
	pb.stop()


	
frame1=tk.LabelFrame(window,cursor="top_left_corner",text="Unix",padx=20,pady=20,bd=5)
frame1.pack()
tk.Label(frame1,text="User:").grid(sticky="W")
e1=tk.Entry(frame1)
e1.grid(row=0,column=1,sticky="W")
tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="Create User", padx=10, pady=3, command= lambda: create_user(e1.get())).grid()

window.mainloop()