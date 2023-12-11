import time
tm = time.localtime()
hr = tm.tm_hour
hr = int(time.strftime("%H"))
print(hr)

if(hr < 12):
    print("Good Morning!")
elif(hr >= 12 and hr < 16):
    print("Good afternoon!")
elif(hr >= 16 and hr < 20):
    print("Good evening!")
else:
    print("Good night!")