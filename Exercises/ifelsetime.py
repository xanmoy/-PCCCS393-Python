print("24 Hours Format")
time = int(input("Enter thr Time: "))
if(time<12 & time>5):
    print("Good Morning Sir!")
elif(time==12):
    print("Good Noon Sir!")
elif(time>12 & time<16):
    print("Good Afternoon Sir!")
elif(time>16 & time<19):
    print("Good Evening Sir!")
elif(time>19 & time<5):
    print("Good Night Sir!")
else:
    print("Please Enter the correct time")