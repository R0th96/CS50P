userID = input("Create user name: ").lower().strip()
password = input("Create a password: ").lower().strip()

while True:
    request01 = input("What's your username: ").lower().strip()
    request02 = input("What's your password: ").lower().strip()
    if request01 == userID and request02 == password :
        print("Success, you are in!")
        break