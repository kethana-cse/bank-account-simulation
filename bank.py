#bank class
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
#method for deposite the amount
def deposit(self, amount):
    if amount > 0:
        self.balance += amount
        print("Amount Deposited Successfully!")
    else:
            print("Invalid Amount!")
#method for withdraw the money
def withdraw(self, amount):
    if amount > self.balance:
        print("Insufficient Balance!")
    elif amount <= 0:
        print("Invalid Amount!")
    else:
         self.balance -= amount
         print("Amount Withdrawn Successfully!")
#method foe balance checking
def check_balance(self):
    print("Current Balance:", self.balance)
#menu_driven program
name = input("Enter Account Holder Name: ")
account = BankAccount(name)
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    #to handle the exception
    try:
    choice = int(input("Enter your choice: "))
    except ValueError:
    print("Please enter a valid number!")
    continue

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        print("Thank you for banking!")
        break

    else:
        print("Invalid Choice!")
