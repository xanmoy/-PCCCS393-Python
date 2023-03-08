marks = [3, 5, 6, "Tanmoy", True, 6, 7 , 2, 32, 345, 23]
print(marks)
print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])
# print(marks[-3]) #negetive index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3])
# print(marks[2])
if "6" in marks:
    print("Yes")
else:
    print("No")

if "nmoy" in "Tanmoy":
    print("Yes")
else:
    print("No")

# print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])