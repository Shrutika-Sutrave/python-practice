user = int(input("enter a number :"))
user_bool = bool(int(input("enter order asc(1) or desc(0) :")))

if user_bool == True:
    for i in range(1, user+1): #i=1
        for j in range(1, i+1): #i=1 j=1 end=2
            print('*',end='')
        print('')

if user_bool == False:
    for i in range(user,0,-1): #i=1
        for j in range(1, i+1): #i=1 j=1 end=2
            print('*',end='')
        print('')
