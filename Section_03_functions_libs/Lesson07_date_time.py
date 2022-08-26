from datetime import *
from time import *

# start 01.01.1970 0.0.0

start = time()

print(date.today())
print(datetime.today())

# create date
d = date(2017, 4, 21)
print(d)

# create datetime
dt = datetime(2017, 4, 21, 13, 50, 31)
print(dt)
print(dt.year)
print(dt.month)

# formating
print("----------------------")
print(dt.strftime("%Y %m %d %H:%M"))  # 2017 04 21 13:50

# time
print("----------------------")
print(time())  #1661545130.3184645
dt = datetime.fromtimestamp(1661545130.3184645)
print(dt.strftime("%Y %m %d %H:%M"))  # 2017 04 21 13:50
dt = datetime.fromtimestamp(1555545130)
print(dt.strftime("%Y %m %d %H:%M"))  # 2017 04 21 13:50

# timestamp from dt
print(dt.timestamp())

# just to add a delay
i = 0
while i < 10000:
    i += 1

print("Time ellapsed : ", time() - start)



