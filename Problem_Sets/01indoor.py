def main():
    greet = input("")
    greeting(greet)

def greeting(n):
    n = n.strip().lower()
    print(n)

main()