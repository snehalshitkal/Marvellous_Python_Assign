class BankAccount:
    ROI = 10.5

    def __init__(self,nm,amt):
        self.Name = nm
        self.Amount = amt

    def Display(self):
        print("Inside Display method:")
        print("Name:"+self.Name)
        print("Amount:",self.Amount)

    def Deposit(self):
        print("Credit Amount are :")
        Amt = int(input())
        self.Amount = self.Amount + Amt
        print("Deposit sucessfully:",self.Amount)

    def Withdraw(self):
        print("Enter Amount of Withdraw")
        withdraw_amt = int(input())
        self.Amount=self.Amount - withdraw_amt
        print("Withdraw Successfully:",self.Amount)

    def CalculateIntrest(self):
        print("Rate of Interest:")
        Intrest = (self.Amount * BankAccount.ROI)/100
        print("ROI %",Intrest)

def main():
    obj1 = BankAccount("Bank of India",50000)
    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateIntrest()


if __name__=="__main__":
    main()