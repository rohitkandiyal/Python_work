import Tkinter as tk

class Todo(tk.Tk,object):

	def __init__(self, tasks=None):
 		super(Todo, self).__init__()
		
		if not tasks:
			self.tasks = []
		else:
			self.tasks = tasks
		
		self.title("To-Do App v1")
		self.geometry("300x400")

		todo1 = tk.Label(self, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)

		self.tasks.append(todo1)

		for task in self.tasks:
			task.pack(side=tk.TOP, fill=tk.X)		#The widgets are packed to the TOP of the window, and are set to fill in the X direction, i.e. horizontally

		self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

	def add_task(self, task_n):
		if len(task_n) > 0:	
			new_task = tk.Label(self, text=task_n, bg="lightgrey", fg="black", pady=10)
			new_task.pack(side=tk.TOP, fill=tk.X)
			self.tasks.append(new_task)
				

if __name__ == "__main__":
	root = Todo()
	root.add_task("Unix")
	root.mainloop()
	
try:
		a=login1.getconnect()
		tk.Label(window2,text="Connection successful to remote server").pack()
	except Exception, e:
		tk.Label(window2,text="Connection failed to remote server").pack()
		return
	t_start="Installation started at {0}".format(time.asctime(time.localtime()))
	tk.Label(window2,text=t_start).pack()
	sftp = a.open_sftp()
	
	sftp.put(or_home+"scripts\\sample_db_install.rsp","/tmp/sample_db_install.rsp",confirm=True)
	sftp.put(or_home+"scripts\\softwarelocations.txt","/tmp/softwarelocations.txt",confirm=True)
	sftp.put(or_home+"scripts\\db_installation.sh","/tmp/db_installation.sh",confirm=True)
	sftp.put(or_home+"scripts\\silent_install.sh","/tmp/silent_install.sh",confirm=True)
	sftp.put(or_home+"scripts\\db_install.rsp","/tmp/db_install.rsp",confirm=True)
	sftp.put(or_home+"scripts\\menuselect.sh","/tmp/menuselect.sh",confirm=True)
	sftp.put(or_home+"scripts\\cr_std_dir.sh","/tmp/cr_std_dir.sh",confirm=True)
	
	
framec=tk.Frame(window)
framec.pack(fill="both")
ttk.Label(framec,text="").pack()
tk.Label(framec,text="MdbBot - DB Management Console",padx=10,pady=10,font=('Times', '12', 'bold')).pack()
ttk.Label(framec,text="").pack()

nb1=ttk.Notebook(framec,padding=10)
framea=ttk.Frame(nb1)
#frameb=ttk.Frame(nb1)
nb1.add(framea,text="ORACLE")
#nb1.add(frameb,text="SQL")
nb1.pack(expand=1, fill="both")

ttk.Label(framea,text="").pack()
ttk.Label(framea,text="").pack()
frame1=tk.LabelFrame(framea,cursor="top_left_corner",text="Choose an option",padx=20,pady=20,bd=5)
frame1.pack(fill="y")
ttk.Label(framea,text="").pack()
ttk.Label(framea,text="").pack()