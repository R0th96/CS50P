#How to print something iteratively using while loop? 
i = 0
while i < 3:
    print("I love Coding")
    i = i + 1 
print()

#How to print something iteratively using for loop? 
for i in [0,1]:
    print("I have someone to protect")
print()

#What is a range function in pseudo code and how to use it in for loop? 
for i in range(3):
    print("I love you")
print()

#What is a "While True" loop and how to use it? 
def main():
    greeting_time()

def greeting_time():
    while True:
        userID = input("How should I greet you? ")
        time = int(input("How many time should I greet you? "))
        if time > 0:
            print(f"Hello {userID}\n" * time)
            break    
main()