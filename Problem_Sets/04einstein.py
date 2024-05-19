def main():
    mass = int(input("m: "))
    Energy(mass)

def Energy(m):
    c = 300000000
    E = m * (c**2)
    print(E)

main()

