def main():
    x = int(input("What's x? "))
    print("1st way")
    if is_even_01(x):
        print("Even")
    else:
        print("Odd")
        
    print("\n")
    print("2nd way")
    if is_even_02(x):
        print("Even")
    else:
        print("Odd")
                
    print("\n")
    print("3rd way")
    if is_even_03(x):
        print("Even")
    else:
        print("Odd")
        
def is_even_01(n):
    if n % 2 == 0:
       return True
    else:
        return False

def is_even_02(n):
    return n % 2 == 0 or False

def is_even_03(n):
    return True if n % 2 == 0 else False

main()