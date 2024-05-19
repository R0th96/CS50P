def main():
    text = input("Input: ")
    omit_vowels(text)

def omit_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    text = text.strip()
    omitted = ""
    for i in text:
        if i in vowels:
            omitted += ""
        else:
            omitted += i
    print(omitted)

main()