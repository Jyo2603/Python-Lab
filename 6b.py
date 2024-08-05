#6b. Write a python program to simulate saving account processing in a bank using constructors. Create Deposit and Withdraw with other member function and Check for Validation while withdrawing the
#amount. Raise the appropriate exceptions when depositing and withdrawing an incorrect amount. Display appropriate messages.

class InsufficientFundsError(Exception): pass
class InvalidAmountError(Exception): pass

class SavingsAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive.")
        self.balance += amount
        print(f"Deposited: {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrawn: {amount}. Balance: {self.balance}")

    def display_balance(self):
        print(f"Balance: {self.balance}")

def main():
    account = SavingsAccount("John Doe", 1000)
    while True:
        choice = input("\n1. Deposit\n2. Withdraw\n3. Display Balance\n4. Exit\nEnter choice: ")
        try:
            if choice == '1':
                account.deposit(float(input("Amount to deposit: ")))
            elif choice == '2':
                account.withdraw(float(input("Amount to withdraw: ")))
            elif choice == '3':
                account.display_balance()
            elif choice == '4':
                break
            else:
                print("Invalid choice")
        except (InvalidAmountError, InsufficientFundsError, ValueError) as e:
            print(e)

if __name__ == "__main__":
    main()
