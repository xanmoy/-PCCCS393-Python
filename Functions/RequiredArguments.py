#In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.
def average(a, b, c=1):
    print("The average is ",(a+b+c)/2)


average(5, 6)