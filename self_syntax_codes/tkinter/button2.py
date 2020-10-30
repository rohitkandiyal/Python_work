import Tkinter as tk
import remotelogin as rlogin
import time
import cffi
from subprocess import Popen
import os


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
	
	sftp.put("C:\\SITA\\DB\\scripts\\sample_db_install.rsp","/tmp/sample_db_install.rsp",confirm=True)
	sftp.put("C:\\SITA\\DB\\scripts\\softwarelocations.txt","/tmp/softwarelocations.txt",confirm=True)
	sftp.put("C:\\SITA\\DB\\scripts\\db_installation.sh","/tmp/db_installation.sh",confirm=True)
	sftp.put("C:\\SITA\\DB\\scripts\\silent_install.sh","/tmp/silent_install.sh",confirm=True)
	sftp.put("C:\\SITA\\DB\\scripts\\db_install.rsp","/tmp/db_install.rsp",confirm=True)
	sftp.put("C:\\SITA\\DB\\scripts\\menuselect.sh","/tmp/menuselect.sh",confirm=True)
	sftp.put("C:\\SITA\\DB\\scripts\\cr_std_dir.sh","/tmp/cr_std_dir.sh",confirm=True)
	
	sftp.put("C:\\SITA\\DB\\config\\DataProvisingTemplates_V2.1.csv","/tmp/DataProvisingTemplates_V2.1.csv",confirm=True)
	sftp.put("C:\\SITA\\DB\\config\\Installation.csv","/tmp/Installation.csv",confirm=True)
	
	tk.Label(window2,text="Required packages copied to remote server").grid()
	
	sftp.close()
	cmd1="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/sample_db_install.rsp > /scripts/25102017/sample_db_install.rsp"
	cmd2="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/softwarelocations.txt > /scripts/25102017/softwarelocations.txt"
	cmd3="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/db_installation.sh > /scripts/25102017/db_installation.sh"
	cmd4="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/silent_install.sh > /scripts/25102017/silent_install.sh"
	cmd5="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/db_install.rsp > /scripts/25102017/db_install.rsp"
	cmd6="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/menuselect.sh > /scripts/25102017/menuselect.sh"
	cmd7="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/cr_std_dir.sh > /scripts/25102017/cr_std_dir.sh"
	
	cmd8="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/DataProvisingTemplates_V2.1.csv > /scripts/templates/DataProvisingTemplates_V2.1.csv"
	cmd9="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/Installation.csv > /scripts/templates/Installation.csv"
	
	stdin, stdout, stderr = a.exec_command(cmd1)
	stdin, stdout, stderr = a.exec_command(cmd2)
	stdin, stdout, stderr = a.exec_command(cmd3)
	stdin, stdout, stderr = a.exec_command(cmd4)
	stdin, stdout, stderr = a.exec_command(cmd5)
	stdin, stdout, stderr = a.exec_command(cmd6)
	stdin, stdout, stderr = a.exec_command(cmd7)
	stdin, stdout, stderr = a.exec_command(cmd8)
	stdin, stdout, stderr = a.exec_command(cmd9)
	
	time.sleep(5)
	
	stdin, stdout, stderr = a.exec_command("cd /scripts/25102017;source ./menuselect.sh", get_pty=True)
	
	exit_status = stdout.channel.recv_exit_status()
	if exit_status == 0:
		tk.Label(window2,text="Oracle DB has been successfully installed").grid()
	else:
		tk.Label(window2,text="DB install unsuccessful").grid()
		print stderr.readlines()
		print stdout.readlines()
	#stdin, stdout, stderr = a.exec_command("cat /tmp/output.txt")
	#for line in stdout.readlines():
	#	tk.Label(window2,text=line).grid()
	
	a.close()
	
def create_oracle(s_name,u_name,passwd):
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
	stdin, stdout, stderr = a.exec_command("mkdir /scripts/templates/Ver_12.1.0.2")
	
	
	sftp = a.open_sftp()
	sftp.put("C:\\SITA\\DB\\scripts\\sample_catalog.sql","/tmp/sample_catalog.sql",confirm=True)
	sftp.put("C:\\SITA\\DB\\scripts\\softwarelocations.txt","/tmp/softwarelocations.txt",confirm=True)
	sftp.put("C:\\SITA\\DB\\scripts\\sample_mydb.sql","/tmp/sample_mydb.sql",confirm=True)
	sftp.put("C:\\SITA\\DB\\scripts\\sample_init.ora","/tmp/sample_init.ora",confirm=True)
	sftp.put("C:\\SITA\\DB\\scripts\\db_creation_inp.sh","/tmp/db_creation_inp.sh",confirm=True)
	sftp.put("C:\\SITA\\DB\\scripts\\menuselect.sh","/tmp/menuselect.sh",confirm=True)
	sftp.put("C:\\SITA\\DB\\scripts\\cr_std_dir.sh","/tmp/cr_std_dir.sh",confirm=True)
	
	sftp.put("C:\\SITA\\DB\\config\\create\\DataProvisingTemplates_V2.1.csv","/tmp/DataProvisingTemplates_V2.1.csv",confirm=True)
	sftp.put("C:\\SITA\\DB\\config\\Installation.csv","/tmp/Installation.csv",confirm=True)
	sftp.put("C:\\SITA\\DB\\config\\Database_V2.1.csv","/tmp/Database_V2.1.csv",confirm=True)
	
	tk.Label(window2,text="Required packages copied to remote server").grid()
	
	sftp.close()
	cmd1="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/sample_catalog.sql > /scripts/25102017/sample_catalog.sql"
	cmd2="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/softwarelocations.txt > /scripts/25102017/softwarelocations.txt"
	cmd3="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/sample_mydb.sql > /scripts/25102017/sample_mydb.sql"
	cmd4="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/sample_init.ora > /scripts/25102017/sample_init.ora"
	cmd5="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/db_creation_inp.sh > /scripts/25102017/db_creation_inp.sh"
	cmd6="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/menuselect.sh > /scripts/25102017/menuselect.sh"
	cmd7="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/cr_std_dir.sh > /scripts/25102017/cr_std_dir.sh"
	
	cmd8="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/DataProvisingTemplates_V2.1.csv > /scripts/templates/DataProvisingTemplates_V2.1.csv"
	cmd9="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/Installation.csv > /scripts/templates/Ver_12.1.0.2/Installation.csv"
	cmd10="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/Database_V2.1.csv > /scripts/templates/Database_V2.1.csv"
	
	stdin, stdout, stderr = a.exec_command(cmd1)
	stdin, stdout, stderr = a.exec_command(cmd2)
	stdin, stdout, stderr = a.exec_command(cmd3)
	stdin, stdout, stderr = a.exec_command(cmd4)
	stdin, stdout, stderr = a.exec_command(cmd5)
	stdin, stdout, stderr = a.exec_command(cmd6)
	stdin, stdout, stderr = a.exec_command(cmd7)
	stdin, stdout, stderr = a.exec_command(cmd8)
	stdin, stdout, stderr = a.exec_command(cmd9)
	stdin, stdout, stderr = a.exec_command(cmd10)
	
	time.sleep(5)
	
	stdin, stdout, stderr = a.exec_command("cd /scripts/25102017;source ./menuselect.sh", get_pty=True)
	
	exit_status = stdout.channel.recv_exit_status()
	if exit_status == 0:
		tk.Label(window2,text="Oracle DB has been successfully created").grid()
	else:
		tk.Label(window2,text="DB Creation unsuccessful").grid()
		print stderr.readlines()
		print stdout.readlines()
	
	a.close()

def install_sql(s_name,u_name):
	window2=tk.Tk()
	window2.title("Mphasis Automation App")
	window2.geometry("300x400")
	a=r"C:\Users\kandiyal\Desktop\for work\python\self_syntax_codes\OS commands\a.PS1"
	cmd='powershell.exe -noexit -file "{0}" "{1}" "{2}"'.format(a,s_name,u_name)
	print cmd
	
	p = Popen(cmd, shell=True)
	stdout, stderr = p.communicate()
	print stdout.readlines()
	print stderr.readlines()
	
def hello_world():
	def install_form():
		'''window1.grid_forget()
		window2=tk.Tk()
		window2.title("Mphasis Automation App")
		window2.grid()
		window2.geometry("400x400")'''
		tk.Label(window1,text="\n\nPlease enter the remote server details\n").grid()
		tk.Label(window1,text="Server:").grid(sticky="W")
		tk.Label(window1,text="Username:").grid(sticky="W")
		tk.Label(window1,text="Password:").grid(sticky="W")
		e1=tk.Entry(window1)
		e1.grid(row=3,column=1,sticky="W")
		e2=tk.Entry(window1)
		e2.grid(row=4,column=1,sticky="W")
		e3=tk.Entry(window1,show="*")
		e3.grid(row=5,column=1,sticky="W")
		tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Next", padx=10, pady=3, command= lambda: install_oracle(e1.get(),e2.get(),e3.get())).grid()
	window1=tk.Tk()
	window1.title("Mphasis Automation App")
	window1.grid()
	window1.geometry("600x400")
	#frame3=tk.Frame(window1,bd=5)
	label=tk.Label(window1,text='Please upload the property/config/ini file in "C:\\SITA\\DB\\config folder"\n\n And click on Proceed to continue\n\n')
	label.grid(sticky="W")
	tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Proceed", padx=10, pady=3, command= install_form).grid()
	
	
	'''tk.Label(window1,text="Server:").grid(sticky="W")
	tk.Label(window1,text="Username:").grid(sticky="W")
	tk.Label(window1,text="Password:").grid(sticky="W")
	e1=tk.Entry(window1)
	e1.grid(row=1,column=1,sticky="W")
	e2=tk.Entry(window1)
	e2.grid(row=2,column=1,sticky="W")
	e3=tk.Entry(window1,show="*")
	e3.grid(row=3,column=1,sticky="W")
	tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Next", padx=10, pady=3, command= lambda: install_oracle(e1.get(),e2.get(),e3.get())).grid()
	'''

	
def hello_world2():
	def install_form1():
		'''window1.grid_forget()
		window2=tk.Tk()
		window2.title("Mphasis Automation App")
		window2.grid()
		window2.geometry("400x400")'''
		tk.Label(window1,text="\n\nPlease enter the remote server details\n").grid()
		tk.Label(window1,text="Server:").grid(sticky="W")
		tk.Label(window1,text="Username:").grid(sticky="W")
		tk.Label(window1,text="Password:").grid(sticky="W")
		e1=tk.Entry(window1)
		e1.grid(row=3,column=1,sticky="W")
		e2=tk.Entry(window1)
		e2.grid(row=4,column=1,sticky="W")
		e3=tk.Entry(window1,show="*")
		e3.grid(row=5,column=1,sticky="W")
		tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Create", padx=10, pady=3, command= lambda: create_oracle(e1.get(),e2.get(),e3.get())).grid()
	window1=tk.Tk()
	window1.title("Mphasis Automation App")
	window1.grid()
	window1.geometry("600x400")
	#frame3=tk.Frame(window1,bd=5)
	label=tk.Label(window1,text='Please upload the property/config/ini file in "C:\\SITA\\DB\\config folder"\n\n And click on to continue\n\n')
	label.grid(sticky="W")
	tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Proceed", padx=10, pady=3, command= install_form1).grid()
	
def hello_world3():
	def install_form2():
		'''window1.grid_forget()
		window2=tk.Tk()
		window2.title("Mphasis Automation App")
		window2.grid()
		window2.geometry("400x400")'''
		tk.Label(window1,text="\n\nPlease enter the remote server details\n").grid()
		tk.Label(window1,text="Server:").grid(sticky="W")
		tk.Label(window1,text="Username:").grid(sticky="W")
		#tk.Label(window1,text="Password:").grid(sticky="W")
		e1=tk.Entry(window1)
		e1.grid(row=3,column=1,sticky="W")
		e2=tk.Entry(window1)
		e2.grid(row=4,column=1,sticky="W")
		#e3=tk.Entry(window1,show="*")
		#e3.grid(row=5,column=1,sticky="W")
		tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Create", padx=10, pady=3, command= lambda: install_sql(e1.get(),e2.get())).grid()
	window1=tk.Tk()
	window1.title("Mphasis Automation App")
	window1.grid()
	window1.geometry("600x400")
	#frame3=tk.Frame(window1,bd=5)
	label=tk.Label(window1,text='Please upload the property/config/ini file in "C:\\SITA\\DB\\config folder"\n\n And click on Proceed to continue\n\n')
	label.grid(sticky="W")
	tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Proceed", padx=10, pady=3, command= install_form2).grid()
	
	
window=tk.Tk()
window.title("Mphasis Automation App")
window.geometry("200x330")

frame1=tk.LabelFrame(window,cursor="top_left_corner",text="Oracle",padx=20,pady=20,bd=5)
frame1.grid(sticky=tk.S)

frame2=tk.LabelFrame(window,cursor="top_left_corner",text="SQL",padx=20,pady=20,bd=5)
frame2.grid()


b = tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="Installation  ", padx=40, pady=5, command=hello_world)
b.grid(columnspan=5,rowspan=5,sticky="W")
b1 = tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="DB Patching", padx=40, pady=5)
b1.grid(columnspan=10,rowspan=10,sticky="W")
tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="DB Creation", padx=40, pady=5, command=hello_world2).grid(sticky="W")

b2 = tk.Button(frame2, activeforeground="#000fff000", bg="lightgrey", text="Installation", padx=40, pady=5, command=hello_world3)
b2.grid(sticky="W")
tk.Button(frame2, activeforeground="#000fff000", bg="lightgrey", text="DB Patching", padx=40, pady=5).grid(sticky="W")
tk.Button(frame2, activeforeground="#000fff000", bg="lightgrey", text="DB Creation", padx=40, pady=5).grid(sticky="W")
window.mainloop()