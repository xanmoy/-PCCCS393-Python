a=int(input('Enter first number - '))
b=int(input('Enter second number - '))
c=int(input('Enter third number - '))
if a!=b!=c:
    if a>b and b>c:
        print('A is the greatest amongst them ')
    elif b>a and b>c:
        print('B is the greatest amongst them ')
    else:
        print('C is the greatest amongst them ')
else:
    print('All inputed elements should be distinct')