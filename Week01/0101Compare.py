#There are mathematical expressions or boolean that can be used in python conditionals
"""
< --> less than
<=  --> less than or equal
> --> greater than
>=  --> greater than or equal
==  -->  equal to
!= --> not equal to 
"""

x = int(input("What's x? "))
y = int(input("What's y? "))

#Way to compare two numbers
print("Comparing two numbers")
if x == y:
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
else:
    print("x is less than y")

#way to know whether two numbers are equal or not
print("Checking whether they are equal or not")
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
