p=int(input('Enter Principle Amount - '))
t=int(input('Ener Time in Years - '))
r=int(input('Enter Rate Applied - '))
si= (p*t*r)/100
print('Simle Interest Calculated is - ',si)
p1=p
for c in range(t):
    i=(p*r)/100
    p=p+i
print('Compound Interest Calculated is - ',p-p1)
    