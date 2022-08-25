import subprocess
import io

# read Date
sp = subprocess.Popen(['date'], stdout=subprocess.PIPE, shell=True)
print(sp)

# read the result
out = io.TextIOWrapper(sp.stdout, encoding="cp866")  # cyrilic
s = ' ';
while s:
    s = out.readline()
    print(s)


# this commands reads the directories
sp = subprocess.Popen(['dir'], stdout=subprocess.PIPE, shell=True)
print(sp)

# read the result
out = io.TextIOWrapper(sp.stdout, encoding="cp866")  # cyrilic
s = ' ';
while s:
    s = out.readline()
    print(s)
