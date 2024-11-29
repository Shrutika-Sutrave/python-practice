level = [100000, 500000, 1000000]
QA = [["q1", 'opA', 'opB', 2], ["q2", 'op 1', 'op 2', 2], ["q3", 'op 1', 'op 2', 1]]

for i in range(0,len(QA)):
    print(f"You are playing for {level[i]}")
    print(f"{QA[i][i]} ")
    print("Options are:")
    print(f"1.{QA[i][1]}    2.{QA[i][2]}")
    user=int(input("Enter option 1 or 2: "))
    if user== QA[i][3]:
        print("you won")
    else:
        print("you lost")
        break
