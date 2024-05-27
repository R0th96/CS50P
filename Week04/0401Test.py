#How to use the module of other users in your python code 
import random
import statistics


#What are the three functions of random module and their usage? 
print("Let's roll a dice")
dice = random.randint(1, 6)
print(f"It is {dice} ")
print("\n")

print("Let's play some card game")
deck = [ "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King" ]
random.shuffle(deck)
for _ in deck:
    print(_)
print("\n")

print("Let's flip three coins")
for i in range(3):
    coin = random.choice(["Head", "Tail"])
    print(coin,"", end="")
print("\n")


#What are the one function of statistics module and their usage? 
print("Let's roll a dice three times and calculate the mean")
coin = []
for i in range(3):
    number = [random.randint(1,6)]
    coin += number

print(statistics.mean(coin))
print("\n")