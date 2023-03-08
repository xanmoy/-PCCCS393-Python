# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
lst = [i for i in range(4)]
print([lst])
lst = [i*i for i in range(10) if i%2==0]
print([lst])