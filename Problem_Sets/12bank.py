def main():
    greeting = input("Greeting: ")
    greeting_rule(greeting)

def greeting_rule(greet):
    greet = greet.strip().lower()
    if greet[0] == "h":
        if greet[0:5] == "hello":
            print("$0")
        else:
            print("$20")
    else:
        print("$100")

main()