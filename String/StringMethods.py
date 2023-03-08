# Strings are immutable
a = "!!!Anthony!! !!!!!! Anthony"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Anthony", "Stark"))
print(a.split(" "))
print(a.count("Anthony"))

blogHeading = "introduction tO js"
print(blogHeading.capitalize())

str1 = "Welcome to Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(str1)
print(str1.center(50))
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.find("ishh"))
print(str1.index("is"))
# print(str1.index("ishh"))

str1 = "WelcomeT@oTheConsole"
print(str1.isalnum()) #if (a-z or A-Z or 0 to 9) == true else flase

str1 = "Welcome"
print(str1.isalpha()) # if (a-z or A-Z) == true else flase

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1)
print(str1.isprintable())

str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())
str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1)
print(str1.swapcase())

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())