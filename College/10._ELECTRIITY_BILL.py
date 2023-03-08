a=int(input('Enter unit calcuated - '))
if a<=100:
    s='No Charges Appilcable'
elif a>100 and a<=200:
    s=5*(a-100)
else:
    s=(5*100)+(10*(a-200))
print('Electricity Bill : ',s)