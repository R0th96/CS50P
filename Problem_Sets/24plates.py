def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(code):
    code = code.strip().lower()
    if 2 <= len(code) <= 6:
        if code.isalpha():
            return True
        elif code.isalnum() and code[0:2].isalpha():
            for c in code:
                if c.isdigit():
                    index = code.index(c)
                    if int(c) != 0 and code[index:len(code)].isdigit():
                        return True
                    else:
                        return False



main()


#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”