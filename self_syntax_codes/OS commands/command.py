'''import os

cmd1='test.bat'
#print os.popen(cmd).read()
#print os.popen(cmd1).read()

os.popen(cmd1)

The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This module intends to replace several older modules and functions:

os.system
os.spawn*
os.popen*
popen2.*
commands.*

'''
from subprocess import Popen
p = Popen("test.bat", cwd=r"C:\Users\kandiyal\Desktop\for work\python\self_syntax_codes\OS commands")
stdout, stderr = p.communicate()

rc=p.returncode

print rc
