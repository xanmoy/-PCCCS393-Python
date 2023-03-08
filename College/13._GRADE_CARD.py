a=int(input('Enter percentage scored - '))
if a<25:
    print('GRADE - D')
elif a>=25 and a<=45:
    print('GRADE - C')
elif a>45 and a<=50:
    print('GRADE - B')
elif a>50 and a<=60:
    print('GRADE - B+')
elif a>60 and a<=80:
    print('GRADE - A')
else:
    print('GRADE - A+')