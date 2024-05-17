#while loop uses boolean expression
i = 0
while i < 3:
    print("Meow")
    i = i + 1
print("\n")
#for loop uses range or lists
#list
for i in [0,1,2]:
    print("Meow")
print("\n")

#range --> range 3 means there are three places available to offer, starting from 0 up to 2.
#in here, i is a variable who don't need, so, in a pythonic way, we can put underscore there
for _ in range(3):
    print("Meow")
print("\n")

#just using pythonic way
print("Meow\n" * 3 , end="")
print("\n")

#using while True loop for limit or conditions you want to put over user input or something
def main():
    number = get_num()
    meow(number)

def get_num():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()