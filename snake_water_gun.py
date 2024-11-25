import random

user_num = int(input("how many times you want to play?: "))
comp = 0
you = 0
i = 1
while i <= user_num:
    user = input("enter from S/W/G: ").upper()
    R = random.choice(['S', 'W', 'G'])
    print(f'computer chose {R}')

    if (R == 'S' and user == 'W') or (R == 'W' and user == 'G') or (R == 'G' and user == 'S'):
        print('computer wins')
        comp += 1

    elif (R == 'G' and user == 'W') or (R == 'S' and user == 'G') or (R == 'W' and user == 'S'):
        print('You won')
        you += 1

    else:
        print("It is a draw")

    if i < user_num:
        print(f"you won {you} times as of now")
        print(f"computer won {comp} times as of now")
        print(f'you have {user_num - i} chances left out of {user_num}')

    i += 1

print("Game over")

if comp > you:
    print("The winner is computer")
elif you > comp:
    print("The winner is you")
else:
    print("It is a draw")

print(f"you won {you} times")
print(f"computer won {comp} times")
