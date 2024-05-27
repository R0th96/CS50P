#How to create own modules? 
def main():
    hello("htet")
    goodbye("htet")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

if __name__ == "__main__":
    main()

