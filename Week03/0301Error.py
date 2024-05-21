#SyntaxError       --> when you don't write the complete syntax in the code
print("Hello World") 
#if you forgot to add one or two " in that code, you will get syntax error.
#if there is SyntaxError, it is entirely up to you to solve it. 

#ValueError        --> when the function can't get the expected type of data                   
#NameError         --> when the variable is not defined or assigned but used in some of the code. 

x = int(input("What's x? "))
print(f"x is {x}")

#you request a user to give some input. 
#According to the code, the int function will convert the incoming str into int. 
#But if the user enter an input which is not digit str but alpha str, that int function won't be able to convert that value into int.
#Then, you will get the valueError

#if you didn't define x but used it in print function, variable name error will occur. 
#if the int can't get the required data to pass down to the left side x, that x become a variable without value so the name x is useless and name error will occur.

