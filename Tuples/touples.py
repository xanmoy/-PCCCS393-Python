tuple = (1, 5, 76, 342, 32, "green", True)
print(type(tuple), tuple)
tup = (1,)
print(type(tup), tup)
tup = (1)
print(type(tup), tup)
# tuple[0] = 90 
print(type(tuple), tuple)
print(len(tuple))
print(tuple[0])
print(tuple[-1])
print(tuple[2])
# print(tuple[34])
if 3421 in tuple:
    print("3421 is present")
tuple2 = tuple[1:4]
print(tuple2)