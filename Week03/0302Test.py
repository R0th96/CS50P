#How to use try function to handle exception? 
try:
    x = int(input("What's x? "))
except ValueError:
    print("Input should be digit")
else:
    print(x)
    

#How to create a program that request user to rate about your service? 
#User should be able to leave a message about your service. 
#The code should be used in another program which require rating system with different prompts. 


def main():
    x = rating("Please rate our service: ")
    y = feedback("Is there anything we can improve next time? ")
    print(f"Thanks for giving us rating {x}")
    print(y)

def rating(value):
    while True:
        try:
            return int(input(value))
        except ValueError:
            pass

def feedback(prompt):
    y = input(prompt).strip().lower().capitalize()
    if y.isalnum():
        return "Thanks for your feedback. \nHave a nice day"
    else:
        return "Glad to know that you satisfy with our service. \nHave a nice day"

main()