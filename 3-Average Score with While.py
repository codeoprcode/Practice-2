b = 0
itr = 0

while 1 == 1 :
        
    score = float(input("score: "))
    ending = input("If you finish, write exit: ")
    b = b + score
    itr = itr + 1

    if ending == "exit":
        break
    else:
        avr = b / itr


print(avr)
