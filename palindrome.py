num = int(input("enter a num: "))
str = input("enter a word: ")

test = num
rev = 0

while num > 0:
    rem = num % 10  # this takes remainder, 121%10= 1 is rem and 12 is quotient
    rev = rev * 10 + rem  # this creates reverse num
    num = num // 10  # this saves quotient, 121%10= 1 is rem and 12 is quotient hence last digit is removed

if rev == test:
    print("yes int")
else:
    print("no int")

str_rev = str[::-1]
if str == str_rev:
    print("yes str")
else:
    print("no str")
