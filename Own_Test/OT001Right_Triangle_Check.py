def main():
    a = int(input("Side 1 length: "))
    b = int(input("Side 2 length: "))
    c = int(input("Longest Side length: "))
    calculation(a,b,c)

def calculation(x, y, z):
    left = x**2 + y**2
    right = z**2
    if left == right:
        print("It is a right triangle")
    else:
        print("It is not a right triangle") 

main()