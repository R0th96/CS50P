#Purpose of comments
#Pseudocode or outlines for your program

#Ways to use comments
#Here is the comments
"""
Here is the comments
"""

#Say hello to user
print("Hello Dear User.")

#Asking for name
#input function will convert the word you type into string
name = input("What is your name, Sir? ")
print("Then, Hello Dear ", name)

#Say thanks you
#three ways to use print multiple arguments
print("Thanks for using our service, " + name)
print("Thanks for using our service,", name)
print(f"Thanks for using our service, {name}")

#the first one is using + operator which tells print function to just concatenate multiple arguments
#the second one is using multiple arguments in a different slots for arguments prepared by print function
#the third one is using FORMAT method for the following argument by telling to be carefull of varable inside the curly bracket

#there are two kinds of parameter as far as I've learned
#Positional parameter or Argument
#Named parameter or optional options

#Positional parameter in print function
print("Argument 01", "Argument 02")

#Named Parameters in print function
print("Argument 01", end="")
print("Argument 02")

print("Argument 01", "Argument 02", sep="")

#the default value of end parameter is "\n"
#the default value of sep parameter is " "

#backslash is actually an escape character
print("Argument01, \"Argument02\"")

#A method is something you can do to the previous function
#You can do many things with user's input string
#You can read documentations at docs.python.org/3/library/stdtypes.html#string-methods

name = input("What's your name? ")

#if the user added unwanted white spaces in left and right side and used all lowercase letters
#you can strip off white spaces and change it to capitalize everyletter
#there are two ways for capitalizing; 
#CAPITALIZE which will capitalize only the first letter 
#TITLE which will capitalize every first letter in the sentence

Cname = name.strip().capitalize()
Tname = name.strip().title()

print(f"This is original, {name}")
print(f"This is capitalized, {Cname}")
print(f"This is titled, {Tname}")

