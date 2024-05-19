def main():
    text = input("")
    convert(text)

def convert(i):
    i = i.strip().replace(":)", "🙂").replace(":(", "🙁")
    print(i)

main()