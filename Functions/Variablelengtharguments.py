def average(*numbers): #takes as touple
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is: ", sum/ len(numbers))
    return sum / len(numbers)

c = average(5, 6, 7, 1)
print(c)
def name(**name): #takes as dict
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")
