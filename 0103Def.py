def main():
    hello()
    name = input("What's your name? ")
    hello(name)

def hello(to="World"):
    print("Hello", to)

main()

#using return
def main02():
    x = int(input("What's x? "))
    print("01.x squared is", square01(x))
    print("02.x squared is", square02(x))
    print("03.x squared is", square03(x))

#return 
def square01(n):
    return n * n 
def square02(n):
    return n ** 2 
def square03(n):
    return pow(n, 2)

main02()