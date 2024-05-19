def main():
    speech = input("")
    playback(speech)

def playback(i):
    i = i.strip().replace(" ", "...")
    print(i)

main()