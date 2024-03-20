# Convention for writing name files with underscore and all lowercased

# String data type

# Literal assignment
first = "Bliss"
last = "asd"

# print(type(last))
# print(isinstance(first, str))

# Constructor function
# pizza = str("pepperoni")
# print(type(pizza))
# print(isinstance(pizza, str))

# Concatenation

fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?                                     

I was just checking in.   

                All good?
'''
print(multiline)

# Escaping special characters

sentence = 'I\'m back at work!\tHey!\nOn another line\nisn\'t it? \\'
print(sentence)

# String Methods

print(first)
print(first.lower())  # it doesnt modify the original value
print(first.upper())
print(first)

print(multiline.title())  # capitalizing the first letter
print(multiline.replace("good", "ok"))  # doesnt modify the original value
print(multiline)
print(len(multiline))
multiline += "                                            "
multiline = "                             " + multiline
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$3".rjust(4))
print("Cheesecake".ljust(16, ".") + "$2".rjust(4))

# string index values

print(first[0])
print(first[-1])
print(first[0:])

# some methods return boolean data
print(first.startswith("B"))
print(first.endswith("x"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# Complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))
