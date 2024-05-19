def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    check(answer)

def check(ans):
    right_answer = ("42", "forty-two", "forty two")
    if ans.strip().lower() in right_answer:
        print("Yes")
    else:
        print("No")

main()