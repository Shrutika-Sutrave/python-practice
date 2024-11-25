from datetime import datetime

operation = input("Do you want to view(V) or entry(E)?: ").upper()
name = input("which client? Enter A for Alex, B for Brit: ").upper()
fittype = input("Are you interested in workout(W) or diet(D)?: ").upper()


class health():
    def __init__(self, operation, name, fittype):
        self.op = operation
        self.name = name
        self.what = fittype

        if operation == 'V':
            if fittype == 'W':
                with open(rf"C:\Users\shrut\Documents\Python Coding\python-practice\{name}_client_G.txt", "r") as file:
                    print(file.read())
            elif fittype == 'D':
                with open(rf"C:\Users\shrut\Documents\Python Coding\python-practice\{name}_client_D.txt", "r") as file:
                    print(f" This is the diet consumed by {name}: \n", file.read())

        elif operation == 'E':
            print(" this is an entry operation")
            if fittype == 'W':
                with open(rf"C:\Users\shrut\Documents\Python Coding\python-practice\{name}_client_G.txt", "a") as file:
                    entry = input("Enter exercise: ")
                    file.write(f"{datetime.now().date()} -> {entry}\n")
            elif fittype == 'D':
                with open(rf"C:\Users\shrut\Documents\Python Coding\python-practice\{name}_client_D.txt", "a") as file:
                    entry = input("Enter meal: ")
                    file.write(f"{datetime.now().date()} -> {entry}\n")
        else:
            print("Invalid input: try again and enter V for view or E for entry")


user = health(operation, name, fittype)
