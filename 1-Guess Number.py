print("Welcome to Guess Number game")
print("Hey, Smart")
print("Guss number between 10 to 60")

import random

rnd_num = random.randint (10 , 60)
itr = 0

while 8 == 8:
    gus = int(input("Pleas enter your guess: "))
    
    if gus == rnd_num:
        print("Riiiiiight 👌👏 ✔")
        itr = itr + 1
        break

    elif gus > rnd_num:
        print("Go down")
        itr = itr + 1

    elif gus < rnd_num:
        print("Go up")
        itr = itr + 1

print("You won with", itr, "times try")
