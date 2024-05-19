def main():
    file = input("File name: ")
    extension_check(file)

def extension_check(f):
    f = f.strip().lower()
    extension = f[f.rfind(".")+1:len(f)]
    match extension:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")
        

main()

