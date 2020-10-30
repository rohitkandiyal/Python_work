import Tkinter as tk

class page(tk.Frame,object):

	def __init__(self,parent):
 		super(page, self).__init__() 
		self.parent=parent
		self.parent.title("Mphasis Application")
		self.parent.geometry("300x400")
	
	def b_create(self,b_text,funcn,**b_opt):
		return tk.Button(self,activeforeground=b_opt["activeforeground"],bg=b_opt["bg"],text=b_text,command=funcn)
		
	def lb_create(self,lb_text):
		return tk.Label(self,text=lb_text,font=('Times', '12', 'bold'))
	def f_clear(self):
		self.pack_forget()
