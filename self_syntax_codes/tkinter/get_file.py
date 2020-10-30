import remotelogin as rlogin

login1=rlogin.login('192.168.56.26','root','Symantec@123')
a=login1.getconnect()
stdin, stdout, stderr = a.exec_command("ls -ltr /tmp/|tail -n 1|awk '{print $9}'")
b=stdout.readlines()
b[0]=str(b[0])
dest="/tmp/"+b[0]
src=r"C:\repo"+"\\"+b[0]
dest=dest.replace("\n","")
src=src.replace("\n","")


sftp = a.open_sftp()
sftp.get(dest,src)
sftp.close()


a.close()