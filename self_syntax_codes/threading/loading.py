import itertools
import threading
import time
import sys
import os

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rThe job has been done successfully!!!     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(10)
cmd1='mkdir abc'
os.popen(cmd1)
done = True