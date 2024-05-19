#What are the different types of boolean mathematical expressions in python? 
"""
 < --> less than
<= --> less than or equal
 > --> greater than
>= --> greater than or equal
== --> equal to
!= --> not equal to
"""

#How to use them for conditional coding? 
name = input("What's your name? ")
score = int(input("Score: "))
if score > 60:
    print("You passed, congratulations")
elif score < 60:
    print("You failed, try next time")
else:
    print("You pass but be careful next time")
print("\n")

#How to define a range to compare with the user input? 
#1st way
print("First way")
if score >= 90 and score < 100:
    print("Score: A")
elif score >= 80 and score < 90:
    print("Score: B")
elif score >= 70 and score < 80:
    print("Score: C")
elif score >= 60 and score < 70:
    print("Score: D")
else:
    print("Score: F")
print("\n")

print("Second Way")
if 90 <= score < 100:
    print("Score: A")
elif 80 <= score < 90:
    print("Score: B")
elif 70 <= score < 80:
    print("Score: C")
elif 60 <= score < 70:
    print("Score: D")
else:
    print("Score: F")
print("\n")

#How to use new function match to use for cases which are too much for if elif else conditional function? 
match name:
    case "Harry" | "Hermione" | "Ron":
        print(f"{name}, You are from Gryffindor!")
    case "Draco":
        print(f"{name}, You are from Slytherin!")
    case _:
        print(f"{name}, Who are you? Are you even from Hogwart?")

