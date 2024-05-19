#How to add comments? (Hints: Two ways) 
#COMMENTS
"""
COMMENTS
"""

#How to print hello world? 
print("Hello World")

#How to ask user for input. 
print("We would like to know about yours")
name = input("What's your name? ")
age = input("How old are you? ")
occupation = input("What kind of occupation do you have right now? ")
occupation = occupation.lower()

#How to add multiple arguments in print function? (Hints: Three ways) 
print("Hello,", name)
print("You are " + age + " ,right?")
print(f"Glad to know that you are a {occupation}")

#What are the two parameters for print function? 
print("I am glad to know you today. ", end="")
print("Would you like to know about \"our products\"?")
print("If there is something you need, tell me", name , sep=":" )

#How to strip off unwanted spaces and capitalize each first letter? 
print("Oh sorry to hear that you aren't interested in our products.")
fullname = input("Btw, can I know your full name? ")
full = fullname.strip().title()
print(f"Nice to meet you {full}")
print("Have", "a", "good", "day,", "sir.")
