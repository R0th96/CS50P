#Accepting integers
x = int(input("What's int01? "))
y = int(input("What's int02? "))

#Accepting floating points
a = float(input("What's float01? "))
b = float(input("What's float02? "))

z = x + y
c = a + b


#Normat Print function
print("Default value for operatioin \'int\' is", z)
print("Default value for operatioin \'float\' is", c)

#If you wanna add comma in your value for readabiltiy
print(f"With comma for int: {z:,}")
print(f"With comma for float: {c:,}")

#Two way to round

print("With f string")
print(f"Rounded for int: {z:.3f}")
print(f"Rounded for float: {c:.3f}")

z = round(z,2)
c = round (c,2)
print("With round function")
print("Rounded for int:", z)
print("Rounded for float:", c)

#Round function does not mess with the integer
#F string messes with the integer and add decimal points