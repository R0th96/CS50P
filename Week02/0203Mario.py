def main():
    print_row(3)
    print("\n")
    print_column(4)
    print("\n")
    print_square(3)
    print("\n")

#using for loops
def print_row(width):
    for _ in range(width):
        print("# ", end="")
    
def print_column(height):
    #1st way
    for _ in range(height):
        print("#")

def print_square(size):
    #1st way
    for i in range(size):
        for j in range(size):
            print("# ", end = "")
        print()
    
    print("\n")
    #2nd way
    for _ in range(size):
        print_row(size)
        print()
main()