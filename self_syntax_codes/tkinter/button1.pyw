import Tkinter as tk
import ttk
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

def patch_oracle(s_name,u_name,passwd,o_home,m_num,p_num,j_num):
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
	sftp = a.open_sftp()
	sftp.put("C:\\SITA\\DB\\scripts\\menuselect.sh","/tmp/menuselect.sh",confirm=True)
	sftp.put("C:\\SITA\\DB\\scripts\\opatch_apply.sh","/tmp/opatch_apply.sh",confirm=True)
	
	sftp.put("C:\\SITA\\DB\\config\\patch\\DataProvisingTemplates_V2.1.csv","/tmp/DataProvisingTemplates_V2.1.csv",confirm=True)
	
	tk.Label(window2,text="Required packages copied to remote server").grid()
	
	sftp.close()
	cmd1="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/menuselect.sh > /scripts/25102017/menuselect.sh"
	cmd2="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/opatch_apply.sh > /scripts/25102017/opatch_apply.sh"
	cmd3="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/DataProvisingTemplates_V2.1.csv > /scripts/templates/DataProvisingTemplates_V2.1.csv"
	
	stdin, stdout, stderr = a.exec_command(cmd1)
	stdin, stdout, stderr = a.exec_command(cmd2)
	stdin, stdout, stderr = a.exec_command(cmd3)
	time.sleep(5)
	print o_home,m_num,p_num,j_num
	
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
	
	stdin, stdout, stderr = a.exec_command(cmd, get_pty=True)
	
	exit_status = stdout.channel.recv_exit_status()
	if exit_status == 0:
		tk.Label(window2,text="Oracle DB has been successfully patched").grid()
	else:
		tk.Label(window2,text="DB Patching unsuccessful").grid()
		print stderr.readlines()
		print stdout.readlines()
	
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

def install_sql(s_name,u_name,passwd):
	window2=tk.Tk()
	window2.title("Mphasis Automation App")
	window2.geometry("300x400")
	a=r"C:\SITA\DB\SQL\scripts\a.PS1"
	cmd='powershell.exe -noexit -file "{0}" "{1}" "{2}" "{3}"'.format(a,s_name,u_name,passwd)
	print cmd
	
	p = Popen(cmd, shell=True)
	stdout, stderr = p.communicate()
	print stdout.readlines()
	print stderr.readlines()

def patch_sql(s_name,u_name,passwd):
	window2=tk.Tk()
	window2.title("Mphasis Automation App")
	window2.geometry("300x400")
	a=r"C:\SITA\DB\SQL\scripts\b.PS1"
	cmd='powershell.exe -noexit -file "{0}" "{1}" "{2}" "{3}"'.format(a,s_name,u_name,passwd)
	print cmd
	p = Popen(cmd, shell=True)
	stdout, stderr = p.communicate()
	print stdout.readlines()
	print stderr.readlines()

def create_sql(s_name,u_name,passwd,i_name,db_name):
	window2=tk.Tk()
	window2.title("Mphasis Automation App")
	window2.geometry("300x400")
	a=r"C:\SITA\DB\SQL\scripts\c.PS1"
	cmd='powershell.exe -noexit -file "{0}" "{1}" "{2}" "{3}" "{4}" "{5}"'.format(a,s_name,u_name,passwd,i_name,db_name)
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
		frame4=tk.Frame(window1)
		frame4.pack()
		tk.Label(frame4,text="\n\nPlease enter the remote server details\n").grid()
		tk.Label(frame4,text="Server:").grid(sticky="W")
		tk.Label(frame4,text="Username:").grid(sticky="W")
		tk.Label(frame4,text="Password:").grid(sticky="W")
		e1=tk.Entry(frame4)
		e1.grid(row=1,column=1,sticky="W")
		e2=tk.Entry(frame4)
		e2.grid(row=2,column=1,sticky="W")
		e3=tk.Entry(frame4,show="*")
		e3.grid(row=3,column=1,sticky="W")
		tk.Button(frame4, activeforeground="#000fff000", bg="lightgrey", text="Install", padx=10, pady=3, command= lambda: install_oracle(e1.get(),e2.get(),e3.get())).grid()
		
	window1=tk.Tk()
	window1.title("Mphasis Automation App")
	window1.grid()
	window1.geometry("380x375")
	label=tk.Label(window1,text='Please upload the property/config/ini file in "C:\\SITA\\DB\\config folder"\n\n And click on Proceed to continue\n\n')
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
		tk.Label(frame5,text="Oracle Home:").grid(sticky="W")
		tk.Label(frame5,text="Master Patch Number").grid(sticky="W")
		tk.Label(frame5,text="PSU Patch Number").grid(sticky="W")
		tk.Label(frame5,text="JVM Patch Number").grid(sticky="W")
		e1=tk.Entry(frame5)
		e1.grid(row=1,column=1,sticky="W")
		e2=tk.Entry(frame5)
		e2.grid(row=2,column=1,sticky="W")
		e3=tk.Entry(frame5,show="*")
		e3.grid(row=3,column=1,sticky="W")
		e4=tk.Entry(frame5)
		e4.grid(row=4,column=1,sticky="W")
		e5=tk.Entry(frame5)
		e5.grid(row=5,column=1,sticky="W")
		e6=tk.Entry(frame5)
		e6.grid(row=6,column=1,sticky="W")
		e7=tk.Entry(frame5)
		e7.grid(row=7,column=1,sticky="W")
		tk.Button(frame5, activeforeground="#000fff000", bg="lightgrey", text="Patch", padx=10, pady=3, command= lambda: patch_oracle(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get())).grid()
	window1=tk.Tk()
	window1.title("Mphasis Automation App")
	window1.grid()
	window1.geometry("380x375")
	#frame3=tk.Frame(window1,bd=5)
	label=tk.Label(window1,text='Please upload the property/config/ini file in "C:\\SITA\\DB\\config folder"\n\n And click on Proceed to continue\n\n')
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
		e1=tk.Entry(frame6)
		e1.grid(row=1,column=1,sticky="W")
		e2=tk.Entry(frame6)
		e2.grid(row=2,column=1,sticky="W")
		e3=tk.Entry(frame6,show="*")
		e3.grid(row=3,column=1,sticky="W")
		tk.Button(frame6, activeforeground="#000fff000", bg="lightgrey", text="Create", padx=10, pady=3, command= lambda: create_oracle(e1.get(),e2.get(),e3.get())).grid()
	window1=tk.Tk()
	window1.title("Mphasis Automation App")
	window1.grid()
	window1.geometry("380x375")
	#frame3=tk.Frame(window1,bd=5)
	label=tk.Label(window1,text='Please upload the property/config/ini file in "C:\\SITA\\DB\\config folder"\n\n And click on to continue\n\n')
	label.pack()
	tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Proceed", padx=10, pady=3, command= install_form2).pack()
	
def hello_world3():
	def install_form3():
		'''window1.grid_forget()
		window2=tk.Tk()
		window2.title("Mphasis Automation App")
		window2.grid()
		window2.geometry("400x400")'''
		frame7=tk.Frame(window1)
		frame7.pack()
		tk.Label(frame7,text="\n\nPlease enter the remote server details\n").grid()
		tk.Label(frame7,text="Server:").grid(sticky="W")
		tk.Label(frame7,text="Username:").grid(sticky="W")
		tk.Label(frame7,text="Password:").grid(sticky="W")
		e1=tk.Entry(frame7)
		e1.grid(row=1,column=1,sticky="W")
		e2=tk.Entry(frame7)
		e2.grid(row=2,column=1,sticky="W")
		e3=tk.Entry(frame7,show="*")
		e3.grid(row=3,column=1,sticky="W")
		tk.Button(frame7, activeforeground="#000fff000", bg="lightgrey", text="Install SQL", padx=10, pady=3, command= lambda: install_sql(e1.get(),e2.get(),e3.get())).grid()
	window1=tk.Tk()
	window1.title("Mphasis Automation App")
	window1.grid()
	window1.geometry("380x375")
	#frame3=tk.Frame(window1,bd=5)
	label=tk.Label(window1,text='Please upload the property/config/ini file in "C:\\SITA\\DB\\config folder"\n\n And click on Proceed to continue\n\n')
	label.pack()
	tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Proceed", padx=10, pady=3, command= install_form3).pack()
	
def hello_world4():
	def install_form4():
		'''window1.grid_forget()
		window2=tk.Tk()
		window2.title("Mphasis Automation App")
		window2.grid()
		window2.geometry("400x400")'''
		frame8=tk.Frame(window1)
		frame8.pack()
		tk.Label(frame8,text="\n\nPlease enter the remote server details\n").grid()
		tk.Label(frame8,text="Server:").grid(sticky="W")
		tk.Label(frame8,text="Username:").grid(sticky="W")
		tk.Label(frame8,text="Password:").grid(sticky="W")
		e1=tk.Entry(frame8)
		e1.grid(row=1,column=1,sticky="W")
		e2=tk.Entry(frame8)
		e2.grid(row=2,column=1,sticky="W")
		e3=tk.Entry(frame8,show="*")
		e3.grid(row=3,column=1,sticky="W")
		tk.Button(frame8, activeforeground="#000fff000", bg="lightgrey", text="Patch SQL", padx=10, pady=3, command= lambda: patch_sql(e1.get(),e2.get(),e3.get())).grid()
	window1=tk.Tk()
	window1.title("Mphasis Automation App")
	window1.grid()
	window1.geometry("380x375")
	#frame3=tk.Frame(window1,bd=5)
	label=tk.Label(window1,text='Please upload the property/config/ini file in "C:\\SITA\\DB\\config folder"\n\n And click on Proceed to continue\n\n')
	label.pack()
	tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Proceed", padx=10, pady=3, command= install_form4).pack()

def hello_world5():
	def install_form5():
		'''window1.grid_forget()
		window2=tk.Tk()
		window2.title("Mphasis Automation App")
		window2.grid()
		window2.geometry("400x400")'''
		frame9=tk.Frame(window1)
		frame9.pack()
		tk.Label(frame9,text="\n\nPlease enter the remote server details\n").grid()
		tk.Label(frame9,text="Server:").grid(sticky="W")
		tk.Label(frame9,text="Username:").grid(sticky="W")
		tk.Label(frame9,text="Password:").grid(sticky="W")
		tk.Label(frame9,text="Instance Name:").grid(sticky="W")
		tk.Label(frame9,text="DB Name:").grid(sticky="W")
		e1=tk.Entry(frame9)
		e1.grid(row=1,column=1,sticky="W")
		e2=tk.Entry(frame9)
		e2.grid(row=2,column=1,sticky="W")
		e3=tk.Entry(frame9,show="*")
		e3.grid(row=3,column=1,sticky="W")
		e4=tk.Entry(frame9)
		e4.grid(row=4,column=1,sticky="W")
		e5=tk.Entry(frame9)
		e5.grid(row=5,column=1,sticky="W")
		tk.Button(frame9, activeforeground="#000fff000", bg="lightgrey", text="Create DB", padx=10, pady=3, command= lambda: create_sql(e1.get(),e2.get(),e3.get(),e4.get(),e5.get())).grid()
	window1=tk.Tk()
	window1.title("Mphasis Automation App")
	window1.grid()
	window1.geometry("380x375")
	#frame3=tk.Frame(window1,bd=5)
	label=tk.Label(window1,text='Click on Proceed to continue with DB Creation Process\n\n')
	label.pack()
	tk.Button(window1, activeforeground="#000fff000", bg="lightgrey", text="Proceed", padx=10, pady=3, command= install_form5).pack()
	
	
window=tk.Tk()
window.title("Mdb-BOT")
window.geometry("375x375")

nb1=ttk.Notebook(window)
framea=ttk.Frame(nb1)
frameb=ttk.Frame(nb1)
nb1.add(framea,text="ORACLE")
nb1.add(frameb,text="SQL")
nb1.pack(expand=1, fill="both")

framec=tk.Frame(framea)
framec.pack()
ttk.Label(framec,text="").pack()
tk.Label(framec,text="MdbBot - DB Management Console",bg="lightblue",fg="blue",padx=10,pady=10,font=('Times', '12', 'bold')).pack()
ttk.Label(framec,text="").pack()
ttk.Label(framec,text="").pack()

framed=tk.Frame(frameb)
framed.pack()
ttk.Label(framed,text="").pack()
tk.Label(framed,text="MdbBot - DB Management Console",bg="lightblue",fg="blue",padx=10,pady=10,font=('Times', '12', 'bold')).pack()
ttk.Label(framed,text="").pack()
ttk.Label(framed,text="").pack()


frame1=tk.LabelFrame(framea,cursor="top_left_corner",text="Oracle Tasks",padx=20,pady=20,bd=5)
frame1.pack(fill="y")

frame2=tk.LabelFrame(frameb,cursor="top_left_corner",text="SQL Tasks",padx=20,pady=20,bd=5)
frame2.pack(fill="y")


b = tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="DB Installation", padx=40, pady=5, command=hello_world)
b.pack(fill="both")
b1 = tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="DB Patching", padx=40, pady=5, command=hello_world1)
b1.pack(fill="both")
tk.Button(frame1, activeforeground="#000fff000", bg="lightgrey", text="DB Creation", padx=40, pady=5, command=hello_world2).pack(fill="both")


b2 = tk.Button(frame2, activeforeground="#000fff000", bg="lightgrey", text="DB Installation", padx=40, pady=5, command=hello_world3)
b2.pack(fill="both")
tk.Button(frame2, activeforeground="#000fff000", bg="lightgrey", text="DB Patching", padx=40, pady=5, command=hello_world4).pack(fill="both")
tk.Button(frame2, activeforeground="#000fff000", bg="lightgrey", text="DB Creation", padx=40, pady=5, command=hello_world5).pack(fill="both")
window.mainloop()