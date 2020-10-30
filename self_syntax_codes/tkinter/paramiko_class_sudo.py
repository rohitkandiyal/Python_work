'''import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

class login():
        def __init__(self,sname,uname,spasswd):
                self.sname=sname
                self.uname=uname
                self.spasswd=spasswd

        def getconnect(self):
                ssh.connect(self.sname, username=self.uname, password=self.spasswd)
                return ssh
				
'''

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('139.73.76.201', username='oracle', password='oracle')

stdin, stdout, stderr = ssh.exec_command("sudo id>/tmp/output123.txt", get_pty=True)
#stdin, stdout, stderr = ssh.exec_command("id>output123.txt")
				
