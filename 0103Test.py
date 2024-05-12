#How to position your code if you have own functions def part? 
#Following format
def main():
    hello()
    name = input("What's your name? ")
    x = int(input("Pick a number? "))
    hello(name)
    print("Square of your picked number is:",square(x)) 

#How to use def to create own functions? 
#How to add parameter to the created functions? 
def hello(to="World"):
    print("Hello,",to)

#How to return value for other functions? 
def square(n):
    return n * n 


main()