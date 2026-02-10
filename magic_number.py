import random

ran_num = random.randint(1, 9)

answer = 0
while answer != ran_num:
    answer = int(input("Guess a number between 1 and 9: "))
    if answer != ran_num:
        print("wrong guess")

print(f"{answer} is the correct guess")