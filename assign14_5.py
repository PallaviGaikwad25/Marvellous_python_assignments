class BankAccount:
    def __init__(self,acc_number,balance,Name):
        self.acc_number=acc_number
        self.balance=balance
        self.Name=Name


    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f"Amount added sucessfully{self.balance}")
        else:
            print("invalid deposit amount")

    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance=self.balance-amount
            print(f"{amount}amount withdraw sucessfully")

        else:
            print("insuffieient balance")


    def display_bal(self):
        print("Name",self.Name)
        print("balance=",self.balance)
        print ("account number",self.acc_number)

def main():
    print("Enter account details:")
    acc_number = input("Account Number: ")
    acc_name = input("Account Holder Name: ")
    balance = float(input("Initial Balance: "))

    # Create a BankAccount object
    obj1 = BankAccount(acc_number,balance,acc_name)

    print("\n--- Deposit ---")
    amount = float(input("Enter amount to deposit: "))
    obj1.deposit(amount)

    print("\n--- Withdraw ---")
    amount = float(input("Enter amount to withdraw: "))
    obj1.withdraw(amount)

    obj1.display_bal()


if __name__ == "__main__":
    main()