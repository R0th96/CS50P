#How to make a set using list? 
previous_work = ["TinaMoeHtwe", "ACH", "Frontiir", "CHID"]

#How to make a set using dict? 
work_duration = {
    "TinaMoeHtwe" : "4 months", 
    "ACH" : "8 months", 
    "Frontiir" : "7 months", 
    "CHID" : "4.5 months"
}

#How to make a set using list and dict? 
exact_details = [
    {"Work" : "TinaMoeHtwe" , "Position" : "Translator" , "Start" : "From Sep 2020" , "End" : "To Dec 2020"},
    {"Work" : "ACH" , "Position" : "Trainee" , "Start" : "From Jun 2022" , "End" : "To Jan 2023"},
    {"Work" : "Frontiir" , "Position" : "Network Engineer" , "Start" : "From May 2023" , "End" : "To Nov 2023"},
    {"Work" : "CHID" , "Position" : "NOC Engineer" , "Start" : "From Nov 2023" , "End" : "To Mar 2024"}
]

def main():
    job_check()
    duration_check()
    details_check()

#How to print a specific index from a list? 
def job_check():
    while True:    
        jobs = int(input("I have done four professional jobs. \nFrom job 1 to 4, what would you like to know? (5 for all) "))
        if 0 < jobs < 5:
            print(jobs, previous_work[jobs-1], sep=". ")
            print("\n")
            break
        elif jobs == 5:
            for i in range(len(previous_work)):
                print(i + 1, previous_work[i])
            print("\n")
            break
        else:
            print("Choose between 1 to 5")

#How to print a details using key from a dict? 
def duration_check():
    while True:
        duration = int(input("Which job you wanna know about job duaration? (5 for all) "))
        if 0 < duration < 5:
            print(duration, previous_work[duration - 1], work_duration[previous_work[duration - 1]], sep=": ")
            print("\n")
            break
        elif duration == 5:
            for i in range(len(previous_work)):
                print(i + 1, previous_work[i], work_duration[previous_work[i]], sep = ": ")
            print("\n")
            break
        else:
            print("Choose between 1 to 5")

#How to print a details of a key from a nested list and dict? 
def details_check():
    while True:
        details = int(input("Wanna know more about details? (5 for all) "))
        if 0 < details < 5:
            index = exact_details[details-1]
            print(details , index["Work"] , index["Position"] , index["Start"] , index["End"], sep=": ")
            break
        elif details == 5:
            _ = 1
            for i in exact_details:
                print(_, i["Work"] , i["Position"] , i["Start"] , i["End"], sep=": ")
                _ += 1
            break            
        else:
            print("Choose between 1 to 5")
main()