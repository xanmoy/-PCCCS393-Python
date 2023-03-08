import math
print('For Circle :')
r=int(input('Enter the radius of the circle - '))
ac= math.pi *(r*r)
print('Area of the given circle is - ',ac)
pc=2*math.pi*r
print('Perimeter of the given circle is - ',pc)
print('For Triangle : ')
s1=int(input('Ener first side - '))
s2=int(input('Ener second side - '))
s3=int(input('Ener third side - '))
pt=s1+s2+s3
print('Perimeter of the given triangle is - ',pt)
if s1!=s2!=s3:
    s=pt/2
    at=math.sqrt(s*((s-s1)*(s-s2)*(s-s3)))
    print('Area of the given triangle is - ',at)
else:
    print('Try with sides having distinct lengths')

    
    