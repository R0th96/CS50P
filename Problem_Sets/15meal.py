def main():
    current_time = input("What time is it? ")
    time = convert(current_time)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")

def convert(time):
    if time.endswith(("a.m.", "p.m.")):
        hour, minute = time.split(":")
        minute, dn = minute.split(" ")
        current = float(hour) + float(minute)/60
        if dn == "a.m." and hour != "12" or dn == "p.m." and hour == "12":
            return current
        if dn == "p.m." and hour != 12 or dn == "a.m." and hour == "12":
            current += 12.00
            return current
    else:
        hour, minute = time.split(":")
        current = float(hour) + float(minute)/60
        return current

main()