user = input("enter num: ")

lenn = len(user)
sum=0
# print(len)
for i in range(0,len(user)):
    # print(i,user[i])
    sum=int(user[i])**lenn+sum

print(sum)
if sum == int(user):
    print("it is armstrong num")
else:
    print("it is not")