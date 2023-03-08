num = input("Enter a Number: ")

if (int(num) < 0):
    print("Number is negative.")
elif (int(num) > 0):
    if (int(num) <= 10):
        print("Number is between 1-10")
    elif (int(num) > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")


    