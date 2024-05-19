students = ["Hermione", "Harry", "Ron"]

#1st way
print(students[0])
print("\n")

#2nd way
for student in students:
    print(student)
print("\n")

#3rd way
for i in range(len(students)):
    print(i + 1, students[i])
print("\n")

#dict way
students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}

for student in students:
    print(student, students[student], sep=" : ")
print("\n")

#dict way to another step
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" : ")