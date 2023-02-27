
import random


while 8 == 8 :
        
    t = int(input("Your turn, enter 1 to play: "))

    if t == 1:
        dice_num = random.randint(1,6)
        print("Dice number is: ",dice_num)

        if dice_num == 6:
            print("Congratulation 🤑 👏 🔥, you can play again")
            p = random.randint(1,6)
            print("Your prize dice: ", p)
        else:
            print("your turn is over")

    else:
        print("please enter 1 to play")
