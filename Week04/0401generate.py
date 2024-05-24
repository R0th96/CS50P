#to import whole module
import random

#to import just one function into your workplace
#from random import choice

#choosing between items
coin = random.choice(["head", "tail"])
print(coin)
print("\n")

#picking up one number from 1 to 10
number = random.randint(1, 10)
print(number)
print("\n")

#shuffle the list provided to the function
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for _ in  cards:
    print(_)
print("\n")
