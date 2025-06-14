class BankAccount:
    ROI=10.5
    def __init__(self):
       self.name=input("enter name ")
       self.amount=float(input("enter amount value"))

    def Display(self):
        print("account holder name",self.name)
        print("cURRENT BALANACE",self.amount)


    def deposit(self):
        print("enter deposit amount:")
        amt=float(input())
        self.amount=self.amount+amt
        print("new balance",self.amount)


    def withdraw(self):
        print("enter amount to withdraw")
        withdraw_amt =float(input())
        if withdraw_amt > self.amount:
            print("insuficient balance withdrawl failed")
        else:
           
           self.amount=self.amount-withdraw_amt

    def calculateIntrest(self):
        interest=(self.amount*BankAccount.ROI)/100
        print("interest=",interest)

        return interest
def main():
    acc1=BankAccount()
    acc1.Display()
    acc1.deposit()
    acc1.withdraw()
    acc1.calculateIntrest()
    acc1.Display()
       

    acc2=BankAccount()
    acc2.deposit()
    acc2.Display()
    acc2.deposit()
    acc2.withdraw()
    acc2.calculateIntrest()
    acc1.Display()
    
if __name__=="__main__":
    main()
