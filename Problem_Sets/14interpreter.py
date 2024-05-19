def main():
    expression = input("Expression: ")
    print(calculate(expression))

def calculate(exp):
    x,y,z = exp.split(" ")
    x, z =(float(x), float(z))
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z
main()