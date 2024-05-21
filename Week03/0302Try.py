#for version 1 to 5,
def main_extra():
    x = get_int()
    print(f"x is {x}")

#for final version
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


#v01 you can use else and break
def get_int_01():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer.")
        else:
            break
    return x
 
#v02: you can omit else and break
def get_int_02():
    while True:
        try:
            x = int(input("What's x? "))
            break
        except ValueError:
            print("x is not an integer.")
    return x

#v03: return is a little stronger than break
def get_int_03():
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            print("x is not an integer.")

#v04: you can return int input without assigning to x
def get_int_04():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer.")

#v05: pass can be used if you face the exception but you want to ignore and prompt again
def get_int_05():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

#v06: you want to use your defined function in any code you want to write in future, so we must make our def function more dynamic
def get_int_06(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


#vFinal: all above examples are right, you just have to justify youself for the right approach
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
