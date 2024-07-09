#6b. Write a python program to simulate saving account processing in a bank using constructors. Create Deposit and Withdraw with other member function and Check for Validation while withdrawing the
#amount. Raise the appropriate exceptions when depositing and withdrawing an incorrect amount. Display appropriate messages.

class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class SavingsAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self.balance += amount
        print("Deposited:", amount, ". New balance:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for the withdrawal.")
        self.balance -= amount
        print("Withdrawn:", amount, ". New balance:", self.balance)

    def display_balance(self):
        print("Current balance:", self.balance)

def main():
    account = SavingsAccount("John Doe", 1000.0)
    print("Account created for", account.account_holder, "with initial balance", account.balance)
    
    while True:
        choice = input("\n1. Deposit\n2. Withdraw\n3. Display Balance\n4. Exit\nEnter your choice: ")
        try:
            if choice == '1':
                account.deposit(float(input("Enter amount to deposit: ")))
            elif choice == '2':
                account.withdraw(float(input("Enter amount to withdraw: ")))
            elif choice == '3':
                account.display_balance()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
        except (InvalidAmountError, InsufficientFundsError) as e:
            print(e)

if __name__ == "__main__":
    main()
