sum=0
while(True):
    user = input("Enter num or q to quite: \n")
    if user != 'q':
        sum = sum + int(user)
        print(f"your total so far is: {sum}")
    else:
        print(f"your total is: {sum}")
        break
