import remotelogin as rlogin
import time

login1=rlogin.login('192.168.56.26','rohit','Symantec@123')
a=login1.getconnect()
stdin, stdout, stderr = a.exec_command("sudo su -;id>/tmp/id1.txt", get_pty=True)
print stdout.readlines()
#stdin, stdout, stderr = a.exec_command("id>/tmp/id1.txt", get_pty=True)
stdin, stdout, stderr = a.exec_command("mkdir /tmp/database123", get_pty=True)
#stdin, stdout, stderr = a.exec_command("id>/tmp/id1.txt", get_pty=True)

'''sftp = a.open_sftp()
sftp.put("C:\\repo\\useradd.sh","/tmp/database4488/useradd.sh",confirm=True)
sftp.close()
cmd="awk '{ sub(\"\\r$\", \"\"); print }' /tmp/database4488/useradd.sh > /tmp/database4488/useradd_ch.sh"
stdin, stdout, stderr = a.exec_command(cmd)
time.sleep(5)
#stdin, stdout, stderr = a.exec_command("sh /tmp/database4488/useradd_ch.sh")
stdin, stdout, stderr = a.exec_command("sh /tmp/database4488/useradd_ch.sh", get_pty=True)
#stdin, stdout, stderr = a.exec_command("id>/tmp/output123.txt")

exit_status = stdout.channel.recv_exit_status()
if exit_status == 0:
    print ("Done")
else:
    print("Error", exit_status,stderr.readlines())
'''


a.close