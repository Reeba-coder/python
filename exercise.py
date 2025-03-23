import time
t=str(input("Enter your message:"))
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
print(t)
hour=int(time.strftime('%H'))
print(hour)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)
if(hour>0 and hour<12):
    print("Good Morning Sir!")
elif(hour>12 and hour<17):
    print("Good Afternoon Sir!")
if(hour>17 and hour<0):
    print("Good Evening Sir!")
else:
    print("Thank You Sir!")
 