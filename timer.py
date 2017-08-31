import time 
import msvcrt

print("Enter y to start timer")
dec = input()
if dec == 'y':
    timeLoop = True
    
sec = 0
min = 0
hr = 0
timeLoop = dec
print('Enter Ctlr+c to stop timer')
try:
    while timeLoop:
        sec = sec+1
        time.sleep(1)
        if sec == 60:
            min = min+1
            sec = 0
        if min == 60:
            hr = hr+1
            min = 0
except KeyboardInterrupt:
    pass
print("Hours:"+str(hr))
print("Minutes:"+str(min))
print("Seconds:"+str(sec))
