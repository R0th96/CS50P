#How to print 15 stars in a row? 
def print_row():
    row_c = input("What character do you want to print out? ").strip()
    row_n = int(input("How many block do you want as a row? "))
    for _ in range(row_n):
        print(f"{row_c} ", end="")
    print("\n")

#How to print 3 hash in a column? 
def print_column():
    column_c = input("What character do you want to print out? ").strip()
    column_n = int(input("How many block do you want as a column? "))
    for _ in range(column_n):
        print(f"{column_c}") 
    print("\n")

#How to print block of * square of size 10? 
def print_square():
    square_c = input("What character do you want to print out? ").strip()
    square_n = int(input("What size do you want? "))
    for i in range(square_n):
        for j in range(square_n):
            print(f"{square_c} ", end = "")
        print()
    print("\n")

def main():
    print_row()
    print_column()
    print_square()

main()