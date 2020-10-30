import remotelogin as rlogin

login1=rlogin.login('192.168.56.26','root','Symantec@123')
a=login1.getconnect()

stdin, stdout, stderr = a.exec_command("touch /tmp/abcd3.txt")
