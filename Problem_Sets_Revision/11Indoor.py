def main():
    voice = input("")
    print(all_cap(voice))

def all_cap(text):
    text = text.strip().upper()
    return text
    
if __name__ == "__main__" :
    main()