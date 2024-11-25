from datetime import datetime

class Health:
    def __init__(self, operation, name, fittype):
        self.op = operation
        self.name = name
        self.what = fittype

    def perform_action(self):
        if self.op == 'V':  # View operation
            if self.what == 'W':
                try:
                    with open(rf"C:\Users\shrut\Documents\Python Coding\python-practice\{self.name}_client_G.txt", "r") as file:
                        print(file.read())
                except FileNotFoundError:
                    print(f"No workout log found for {self.name}.")
            elif self.what == 'D':
                try:
                    with open(rf"C:\Users\shrut\Documents\Python Coding\python-practice\{self.name}_client_D.txt", "r") as file:
                        print(f"This is the diet consumed by {self.name}:\n", file.read())
                except FileNotFoundError:
                    print(f"No diet log found for {self.name}.")
        elif self.op == 'E':  # Entry operation
            print("This is an entry operation")
            if self.what == 'W':
                with open(rf"C:\Users\shrut\Documents\Python Coding\python-practice\{self.name}_client_G.txt", "a") as file:
                    entry = input("Enter exercise: ")
                    file.write(f"{datetime.now().date()} -> {entry}\n")
            elif self.what == 'D':
                with open(rf"C:\Users\shrut\Documents\Python Coding\python-practice\{self.name}_client_D.txt", "a") as file:
                    entry = input("Enter meal: ")
                    file.write(f"{datetime.now().date()} -> {entry}\n")
        else:
            print("Invalid operation. Please enter 'V' for view or 'E' for entry.")

# Interactive creation of user instances
num_users = int(input("How many users do you want to process? "))

for i in range(num_users):
    print(f"Processing user {i + 1}:")
    operation = input("Do you want to view(V) or entry(E)?: ").upper()
    name = input("Which client? Enter A for Alex, B for Brit: ").upper()
    fittype = input("Are you interested in workout(W) or diet(D)?: ").upper()
    user = Health(operation, name, fittype)
    user.perform_action()
