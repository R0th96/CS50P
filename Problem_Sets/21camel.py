def main():
    camelCase = input("camelCase: ")
    print("snake_case:", snake_case(camelCase))

def snake_case(case):
    l = ""
    for i in range(len(case)):
        if case[i].isupper():
            l = l + "_" + case[i].lower()
        else:
            l += case[i]
    return l
main()