import Tkinter as tk
import remotelogin as rlogin
import cffi
import time

def install_oracle(s_name,u_name,passwd):
	window2=tk.Tk()
	window2.title("Mphasis Automation App")
	window2.geometry("300x400")
	login1=rlogin.login(s_name,u_name,passwd)
	try:
		a=login1.getconnect()
		tk.Label(window2,text="Connection successful to remote server").grid()
	except Exception, e:
		tk.Label(window2,text="Connection failed to remote server").grid()
		return
	stdin, stdout, stderr = a.exec_command("mkdir /tmp/database")
	sftp = a.open_sftp()
	sftp.put("C:\\repo\\useradd.sh","/tmp/database/useradd.sh",confirm=True)
	tk.Label(window2,text="Required packages copied to remote server").grid()
	sftp.close()
	cmd="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/database/useradd.sh > /tmp/database/useradd_ch.sh"
	stdin, stdout, stderr = a.exec_command(cmd)
	time.sleep(5)
	stdin, stdout, stderr = a.exec_command("sh /tmp/database/useradd_ch.sh")
	exit_status = stdout.channel.recv_exit_status()
	if exit_status == 0:
		tk.Label(window2,text="User has been successfully created").grid()
	else:
		tk.Label(window2,text="error").grid()
	stdin, stdout, stderr = a.exec_command("cat /tmp/output.txt")
	for line in stdout.readlines():
		tk.Label(window2,text=line).grid()
	
	a.close()
	

def hello_world():
	window1=tk.Tk()
	window1.title("Mphasis Automation App")
	window1.grid()
	window1.geometry("400x400")
	#frame3=tk.Frame(window1,bd=5)
	label=tk.Label(window1,text='Please keep the required files in "C:\\repo"\nGoing to install Oracle DB...\n\nPlease enter server details below\n\n')
	label.grid()
	tk.Label(window1,text="Server:").grid(sticky="W")
	tk.Label(window1,text="Username:").grid(sticky="W")
	tk.Label(window1,text="Password:").grid(sticky="W")
	e1=tk.Entry(window1)
	e1.grid(row=1,column=1,sticky="W")
	e2=tk.Entry(window1)
	e2.grid(row=2,column=1,sticky="W")
	e3=tk.Entry(window1,show="*")
	e3.grid(row=3,column=1,sticky="W")
	tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Next", padx=10, pady=3, command= lambda: install_oracle(e1.get(),e2.get(),e3.get())).grid()
	
	
	
	

window=tk.Tk()
window.title("Mphasis Automation App")
window.geometry("300x400")

frame1=tk.LabelFrame(window,cursor="top_left_corner",text="Oracle",padx=20,pady=20,bd=5)
frame1.grid()

frame2=tk.LabelFrame(window,cursor="top_left_corner",text="SQL",padx=20,pady=20,bd=5)
frame2.grid()


b = tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="Install", padx=40, pady=5, command=hello_world)
b.grid(columnspan=5,rowspan=5)
b1 = tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="Patching", padx=30, pady=5)
b1.grid(columnspan=10,rowspan=10)
b2 = tk.Button(frame2, activeforeground="#000fff000", bg="lightgrey", text="Install", padx=40, pady=5)
b2.grid()
tk.Button(frame2, activeforeground="#000fff000", bg="lightgrey", text="Patching", padx=30, pady=5).grid()

window.mainloop()