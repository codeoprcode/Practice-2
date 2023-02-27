import random
cpu_s = 0
user_s = 0

while cpu_s < 4 or user_s < 4 :
    
    a = random.randint (1 , 3)
    if a == 1 :
        cpu_ch = "stone"

    elif a == 2 :
        cpu_ch = "paper"

    elif a == 3 :
        cpu_ch = "scissors"

    user_ch = input("Please write one between stone paper scissors: ")

    print("💻 :", cpu_ch ,"and 👤 :", user_ch)

    if cpu_ch == "stone" and user_ch == "paper":
            user_s = user_s + 1 

    elif cpu_ch == "stone" and user_ch == "scissors":
            cpu_s = cpu_s + 1

    elif cpu_ch == "paper" and user_ch == "stone":
            cpu_s = cpu_s + 1

    elif cpu_ch == "paper" and user_ch == "scissors":
            user_s = user_s + 1 

    elif cpu_ch == "scissors" and user_ch == "stone":
            user_s = user_s + 1 

    elif cpu_ch == "scissors" and user_ch == "paper":
            cpu_s = cpu_s + 1

    print("💻 :", cpu_s, "vs 👤 :", user_s)
    




