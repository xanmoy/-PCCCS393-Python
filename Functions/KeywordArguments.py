# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.
def average(a=9, b=1):
    print("The average is ",(a+b)/2)


average(b=9, a=21)