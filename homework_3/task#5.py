import random
fortuna = random.randint(1, 10)
attempt = 0
while attempt < 3:
    attempt += 1
    number = int(input("Введи число від 1-10: "))
    if number != fortuna:
        print("You lose!")
        continue
    else:
        print("You win!")
        break
