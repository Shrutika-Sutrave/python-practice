n=50
i=0
while i<9:
    u= int(input("Guess the number: "))

    if n==u:
        print("you won!")
        print("you took these many guesses to finish:", i+1)
        break

    elif n!=u and u<25:
        i=i+1
        print("Your guess is too low, remaining guesses: ", 9-i)

    elif n!=u and u>50:
        i=i+1
        print("Your guess is too high, remaining guesses: ", 9-i)

    elif n!=u and u>=25 and u<50:
        i=i+1
        print("Your guess is close, remaining guesses: ", 9-i)


