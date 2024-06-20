def main():
    total_type = []
    total_cost = []
    while True:
        try:
            type, cost = usage()
            total_type += [type]
            total_cost += [cost]
        except EOFError:
            print()
            for i in range(len(total_type)):
                print(total_type[i], total_cost[i])
            print("Total is", sum(total_cost), "Baht")
            break
def usage():
    try:
        type = input("Where did you spend? ")
        cost = float(input("How much? "))
        return type, cost
    except ValueError:
        pass

main()
print("I Love Akari"*3)


"""
git --version
git config --global user.name NAME
git config --global user.email MAIL
git clone
git add file
git commit
git push
git remote set-url origin git@github.com:<Username>/<Project>.git


"""
