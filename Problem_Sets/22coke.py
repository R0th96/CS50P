def main():
    payment()

def payment():
    accepted_coin = (5,10,25)
    cost = 50
    current_paid = 0
    print("Amount Due:", cost)
    while True:
        paid = int(input("Insert Coin: "))
        if paid in accepted_coin:
            cost = cost - paid
            current_paid += paid
            if current_paid < 50:
                print("Amount Due:", cost)
            else:
                change = current_paid - 50
                print("Change Owed:", change)
                break
        else:
            print("Amount Due: ", cost)

main()