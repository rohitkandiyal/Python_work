import Tkinter as tk
window1=tk.Tk()
window1.title("Mphasis Automation App")
window1.grid()
window1.geometry("600x400")

def create_file(a,b,c):
	filename=r"C:\content.txt"
	print filename
	txtw = open(filename,'w')
	out="{0};{1};{2}".format(a,b,c)
	print out
	txtw.write(out)
	
	
	
	
tk.Label(window1,text="Server:").grid(sticky="W")
tk.Label(window1,text="Username:").grid(sticky="W")
tk.Label(window1,text="Password:").grid(sticky="W")
e1=tk.Entry(window1)
e1.grid(row=0,column=1,sticky="W")
e2=tk.Entry(window1)
e2.grid(row=1,column=1,sticky="W")
e3=tk.Entry(window1,show="*")
e3.grid(row=2,column=1,sticky="W")
tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Next", padx=10, pady=3, command= lambda: create_file(e1.get(),e2.get(),e3.get())).grid()


window1.mainloop()