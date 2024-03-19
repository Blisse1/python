# floor division, round it down
operation = 24 // 5
print(operation)

# round
operationRounded = round(24 / 5)
print(operationRounded)

# to the power of
exampleNumber = 2 ** 5

meaning = 42
meaning += 1
print(meaning)

# comparison, only two equals
# 42 == 21 false
# 42 == 42 true
# 43 != 42 true

x = False
y = True
z = False

print(not x)
print(not y)
print(x and z)
print(y or z)

if meaning < 10:
    print("right on!")
else:
    print("not today")

# ternary operator
# what I want to be the output first if the statement is true

print("It's working") if meaning > 10 else print("Maybe other day")
