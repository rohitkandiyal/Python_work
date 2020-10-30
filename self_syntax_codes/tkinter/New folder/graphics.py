import Tkinter as tk

class application(tk.Tk,object):

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
				
