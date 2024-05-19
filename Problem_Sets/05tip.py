def main():
    bill = bill_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = bill * percent
    print(f"Leave ${tip:.2f}")

def bill_to_float(n1):
    n1 = float(n1.replace("$", ""))
    return n1

def percent_to_float(n2):
    n2 = float(n2.replace("%", "")) / 100
    return n2

main()