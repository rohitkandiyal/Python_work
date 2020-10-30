import Tkinter as tk
import ttk
import remotelogin as rlogin
import time
import cffi
from subprocess import Popen
import os

or_home=r"C:\MdbBOT\Oracle"+"\\"
sr_home=r"C:\MdbBOT\SQL"+"\\"

def install_oracle(s_name,u_name,passwd):
	window2=tk.Tk()
	window2.title("Mphasis Automation App")
	window2.geometry("440x410")
	login1=rlogin.login(s_name,u_name,passwd)
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
	
	sftp.put(or_home+"config\\install\\DataProvisingTemplates_V2.1.csv","/tmp/DataProvisingTemplates_V2.1.csv",confirm=True)
	sftp.put(or_home+"config\\install\\Installation.csv","/tmp/Installation.csv",confirm=True)
	
	tk.Label(window2,text="Required packages copied to remote server").pack()
	
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
		tk.Label(window2,text="Oracle DB has been successfully installed").pack()
	else:
		tk.Label(window2,text="DB install unsuccessful").pack()
		print stderr.readlines()
		print stdout.readlines()
	#stdin, stdout, stderr = a.exec_command("cat /tmp/output.txt")
	#for line in stdout.readlines():
	#	tk.Label(window2,text=line).grid()
	time.sleep(5)
	stdin, stdout, stderr = a.exec_command("c=`ls -ltr /logs/|tail -n 1|awk '{print $9}'` && cp /logs/$c /tmp/install_log.txt")
	time.sleep(5)
	dest="/tmp/install_log.txt"
	t=time.asctime(time.localtime())
	t=t[4:10]+t[19:]
	src=or_home+"logs"+"\\"+"install_log.txt"+t
	#dest=dest.replace("\n","")
	#src=src.replace("\n","")
	sftp.get(dest,src)
	tk.Label(window2,text="Please refer the logs in C:\\MdbBOT\\Oracle\\logs").pack()
	t_stop="Installation finished at {0}".format(time.asctime(time.localtime()))
	tk.Label(window2,text=t_stop).pack()
	sftp.close()
	a.close()

def patch_oracle(s_name,u_name,passwd):

	window2=tk.Tk()
	window2.title("Mphasis Automation App")
	window2.geometry("300x400")
	login1=rlogin.login(s_name,u_name,passwd)
	try:
		a=login1.getconnect()
		tk.Label(window2,text="Connection successful to remote server").pack()
	except Exception, e:
		tk.Label(window2,text="Connection failed to remote server").pack()
		return
	t_start="DB Patching started at {0}".format(time.asctime(time.localtime()))
	tk.Label(window2,text=t_start).pack()
	sftp = a.open_sftp()
	
	sftp.put(or_home+"scripts\\menuselect.sh","/tmp/menuselect.sh",confirm=True)
	sftp.put(or_home+"scripts\\opatch_apply.sh","/tmp/opatch_apply.sh",confirm=True)
	
	sftp.put(or_home+"config\\patch\\DataProvisingTemplates_V2.1.csv","/tmp/DataProvisingTemplates_V2.1.csv",confirm=True)
	
	tk.Label(window2,text="Required packages copied to remote server").pack()
	
	cmd1="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/menuselect.sh > /scripts/25102017/menuselect.sh"
	cmd2="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/opatch_apply.sh > /scripts/25102017/opatch_apply.sh"
	cmd3="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/DataProvisingTemplates_V2.1.csv > /scripts/templates/DataProvisingTemplates_V2.1.csv"
	
	stdin, stdout, stderr = a.exec_command(cmd1)
	stdin, stdout, stderr = a.exec_command(cmd2)
	stdin, stdout, stderr = a.exec_command(cmd3)
	time.sleep(5)
	
	file=or_home+"config\\patch\\Patching.txt"
	txt = open(file)
	args=[]
	for line in txt.readlines():
		args.append(line.split(",")[1])
	arg=[]
	for val in args:
		val=val.replace("\n","")
		arg.append(val)
	
	o_home=arg[0]
	m_num=arg[1]
	p_num=arg[2]
	j_num=arg[3]
	
	
	stdin, stdout, stderr = a.exec_command("mv /u01/app/oracle/product/12.1.0.2/db_1/OPatch /u01/app/oracle/product/12.1.0.2/db_1/OPatch_old", get_pty=True)
	print stderr.readlines()
	print stdout.readlines()
	stdin, stdout, stderr = a.exec_command("cd /u01/app/oracle/product/12.1.0.2/db_1 && unzip /u01/PATCH/p6880880_122010_Linux-x86-64.zip", get_pty=True)
	print stderr.readlines()
	print stdout.readlines()
	stdin, stdout, stderr = a.exec_command("cd /u01/app/oracle/product/12.1.0.2/db_1/OPatch && unzip /u01/PATCH/p26550023_121020_Linux-x86-64.zip", get_pty=True)
	print stderr.readlines()
	print stdout.readlines()
	
	cmd="cd /scripts/25102017;source ./menuselect.sh {0} {1} {2} {3}".format(o_home,m_num,p_num,j_num)
	#print cmd
	#print type(cmd)
	stdin, stdout, stderr = a.exec_command(cmd, get_pty=True)
	
	exit_status = stdout.channel.recv_exit_status()
	if exit_status == 0:
		tk.Label(window2,text="Oracle DB has been successfully patched").pack()
	else:
		tk.Label(window2,text="DB Patching unsuccessful").pack()
		print stderr.readlines()
		print stdout.readlines()
	time.sleep(5)	
	stdin, stdout, stderr = a.exec_command("c=`ls -ltr /logs/|tail -n 1|awk '{print $9}'` && cp /logs/$c /tmp/patch_log.txt")
	time.sleep(5)
	dest="/tmp/patch_log.txt"
	t=time.asctime(time.localtime())
	t=t[4:10]+t[19:]
	src=or_home+"logs"+"\\"+"patch_log.txt"+t
	#dest=dest.replace("\n","")
	#src=src.replace("\n","")
	sftp.get(dest,src)
	tk.Label(window2,text="Please refer the logs in C:\\MdbBOT\\Oracle\\logs").pack()
	t_stop="DB Patching finished at {0}".format(time.asctime(time.localtime()))
	tk.Label(window2,text=t_stop).pack()
	sftp.close()
	a.close()
	
def create_oracle(s_name,u_name,passwd):
	window2=tk.Tk()
	window2.title("Mphasis Automation App")
	window2.geometry("440x410")
	login1=rlogin.login(s_name,u_name,passwd)
	try:
		a=login1.getconnect()
		tk.Label(window2,text="Connection successful to remote server").pack()
	except Exception, e:
		tk.Label(window2,text="Connection failed to remote server").pack()
		return
	t_start="DB Creation started at {0}".format(time.asctime(time.localtime()))
	tk.Label(window2,text=t_start).pack()

	stdin, stdout, stderr = a.exec_command("mkdir /scripts/templates/Ver_12.1.0.2")
	
	
	sftp = a.open_sftp()
	sftp.put(or_home+"scripts\\sample_catalog.sql","/tmp/sample_catalog.sql",confirm=True)
	sftp.put(or_home+"scripts\\softwarelocations.txt","/tmp/softwarelocations.txt",confirm=True)
	sftp.put(or_home+"scripts\\sample_mydb.sql","/tmp/sample_mydb.sql",confirm=True)
	sftp.put(or_home+"scripts\\sample_init.ora","/tmp/sample_init.ora",confirm=True)
	sftp.put(or_home+"scripts\\db_creation_inp.sh","/tmp/db_creation_inp.sh",confirm=True)
	sftp.put(or_home+"scripts\\menuselect.sh","/tmp/menuselect.sh",confirm=True)
	sftp.put(or_home+"scripts\\cr_std_dir.sh","/tmp/cr_std_dir.sh",confirm=True)
	
	sftp.put(or_home+"config\\db_create\\DataProvisingTemplates_V2.1.csv","/tmp/DataProvisingTemplates_V2.1.csv",confirm=True)
	sftp.put(or_home+"config\\db_create\\Installation.csv","/tmp/Installation.csv",confirm=True)
	sftp.put(or_home+"config\\db_create\\Database_V2.1.csv","/tmp/Database_V2.1.csv",confirm=True)
	
	tk.Label(window2,text="Required packages copied to remote server").pack()
	
	
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
		tk.Label(window2,text="Oracle DB has been successfully created").pack()
		print stderr.readlines()
		print stdout.readlines()
	else:
		tk.Label(window2,text="DB Creation unsuccessful").pack()
		print stderr.readlines()
		print stdout.readlines()
	time.sleep(5)
	stdin, stdout, stderr = a.exec_command("c=`ls -ltr /logs/|tail -n 1|awk '{print $9}'` && cp /logs/$c /tmp/createDB_log.txt")
	time.sleep(5)
	dest="/tmp/createDB_log.txt"
	t=time.asctime(time.localtime())
	t=t[4:10]+t[19:]
	src=or_home+"logs"+"\\"+"createDB_log.txt"+t
	#dest=dest.replace("\n","")
	#src=src.replace("\n","")
	sftp.get(dest,src)
	tk.Label(window2,text="Please refer the logs in C:\\MdbBOT\\Oracle\\logs").pack()
	t_stop="DB Creation finished at {0}".format(time.asctime(time.localtime()))
	tk.Label(window2,text=t_stop).pack()
	sftp.close()
	a.close()

def hello_world():
	def install_form():
		'''window1.grid_forget()
		window2=tk.Tk()
		window2.title("Mphasis Automation App")
		window2.grid()
		window2.geometry("400x400")'''
		frame4=tk.Frame(window1)
		frame4.pack()
		tk.Label(frame4,text="\n\nPlease enter the remote server details\n").grid()
		tk.Label(frame4,text="Server:").grid(sticky="W")
		tk.Label(frame4,text="Username:").grid(sticky="W")
		tk.Label(frame4,text="Password:").grid(sticky="W")
		tk.Label(frame4,text="").grid(sticky="W")
		e1=tk.Entry(frame4)
		e1.grid(row=1,column=1,sticky="W")
		e2=tk.Entry(frame4)
		e2.grid(row=2,column=1,sticky="W")
		e3=tk.Entry(frame4,show="*")
		e3.grid(row=3,column=1,sticky="W")
		framep=tk.Frame(window1)
		framep.pack()
		tk.Button(framep, activeforeground="#000fff000", bg="lightgrey", text="Install", padx=10, pady=3, command= lambda: install_oracle(e1.get(),e2.get(),e3.get())).grid()
		
	window1=tk.Tk()
	window1.title("Mphasis Automation App")
	window1.grid()
	window1.geometry("440x410")
	label=tk.Label(window1,text='Please upload the request form(csv) file in C:\\MdbBOT\\Oracle\\config\\install folder\n\n And click on Proceed to continue\n\n')
	label.pack()
	tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Proceed", padx=10, pady=3, command= install_form).pack()
	
	
	'''
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
	'''

def hello_world1():
	def install_form1():
		'''window1.grid_forget()
		window2=tk.Tk()
		window2.title("Mphasis Automation App")
		window2.grid()
		window2.geometry("400x400")'''
		frame5=tk.Frame(window1)
		frame5.pack()
		tk.Label(frame5,text="\n\nPlease enter the remote server details\n").grid()
		tk.Label(frame5,text="Server:").grid(sticky="W")
		tk.Label(frame5,text="Username:").grid(sticky="W")
		tk.Label(frame5,text="Password:").grid(sticky="W")
		#tk.Label(frame5,text="Oracle Home:").grid(sticky="W")
		#tk.Label(frame5,text="Master Patch Number").grid(sticky="W")
		#tk.Label(frame5,text="PSU Patch Number").grid(sticky="W")
		#tk.Label(frame5,text="JVM Patch Number").grid(sticky="W")
		tk.Label(frame5,text="").grid(sticky="W")
		e1=tk.Entry(frame5)
		e1.grid(row=1,column=1,sticky="W")
		e2=tk.Entry(frame5)
		e2.grid(row=2,column=1,sticky="W")
		e3=tk.Entry(frame5,show="*")
		e3.grid(row=3,column=1,sticky="W")
		'''e4=tk.Entry(frame5)
		e4.grid(row=4,column=1,sticky="W")
		e5=tk.Entry(frame5)
		e5.grid(row=5,column=1,sticky="W")
		e6=tk.Entry(frame5)
		e6.grid(row=6,column=1,sticky="W")
		e7=tk.Entry(frame5)
		e7.grid(row=7,column=1,sticky="W")
		'''
		framez=tk.Frame(window1)
		framez.pack()
		tk.Button(framez, activeforeground="#000fff000", bg="lightgrey", text="Patch", padx=10, pady=3, command= lambda: patch_oracle(e1.get(),e2.get(),e3.get())).pack()
	window1=tk.Tk()
	window1.title("Mphasis Automation App")
	window1.grid()
	window1.geometry("440x410")
	#frame3=tk.Frame(window1,bd=5)
	label=tk.Label(window1,text='Please upload the request form(csv) file in C:\\MdbBOT\\Oracle\\config\\patch folder\n\n And click on Proceed to continue\n\n')
	label.pack()
	tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Proceed", padx=10, pady=3, command= install_form1).pack()
	
def hello_world2():
	def install_form2():
		'''window1.grid_forget()
		window2=tk.Tk()
		window2.title("Mphasis Automation App")
		window2.grid()
		window2.geometry("400x400")'''
		frame6=tk.Frame(window1)
		frame6.pack()
		tk.Label(frame6,text="\n\nPlease enter the remote server details\n").grid()
		tk.Label(frame6,text="Server:").grid(sticky="W")
		tk.Label(frame6,text="Username:").grid(sticky="W")
		tk.Label(frame6,text="Password:").grid(sticky="W")
		tk.Label(frame6,text="").grid(sticky="W")
		e1=tk.Entry(frame6)
		e1.grid(row=1,column=1,sticky="W")
		e2=tk.Entry(frame6)
		e2.grid(row=2,column=1,sticky="W")
		e3=tk.Entry(frame6,show="*")
		e3.grid(row=3,column=1,sticky="W")
		frameq=tk.Frame(window1)
		frameq.pack()
		tk.Button(frameq, activeforeground="#000fff000", bg="lightgrey", text="Create DB", padx=10, pady=3, command= lambda: create_oracle(e1.get(),e2.get(),e3.get())).grid()
	window1=tk.Tk()
	window1.title("Mphasis Automation App")
	window1.grid()
	window1.geometry("457x410")
	#frame3=tk.Frame(window1,bd=5)
	label=tk.Label(window1,text='Please upload the request form(csv) file in C:\\MdbBOT\\Oracle\\config\\db_create folder\n\n And click on Proceed to continue\n\n')
	label.pack()
	tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Proceed", padx=10, pady=3, command= install_form2).pack()
	

window=tk.Tk()
window.title("Mdb-BOT")
window.geometry("440x410")

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


b = tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="DB Installation", padx=40, pady=5, command=hello_world)
b.pack(fill="both")
tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="DB Creation", padx=40, pady=5, command=hello_world2).pack(fill="both")
b1 = tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="DB Patching", padx=40, pady=5, command=hello_world1)
b1.pack(fill="both")

window.mainloop()