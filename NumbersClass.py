class Numbers:
    def __init__(self):
        print("Enter Number:")
        no = int(input())
        self.Value = no

    def ChkPrime(self):
        if self.Value<0:
            return False
        for i in range(2,int(self.Value**0.5)+1):
            if (self.Value % i == 0):
                return False
        return True


    def ChkPerfect(self):
        sum = 0
        for i in range(1,self.Value+1):
            if (self.Value%i==0):
                sum = sum + i
                return True
            else:
                return False
        if (sum==Value):
            return True


        return self.SumFactor()==self.Value


    def SumFactor(self):
        total = 0
        for i in range(1,self.Value):
            if (self.Value % i==0):
                total= total + i
        return total

    def Factor(self):
        for i in range (1,self.Value+1):
            if self.Value % i ==0:
                print(i)
        print()


def main():
    obj1=Numbers()   
    ret = obj1.ChkPrime()
    if (ret == True):
        print("Prime no",ret) 
    else:
         print("Not Prime no")

    ret = obj1.ChkPerfect()
    if (ret == True):
        print("PerfectNo",ret) 
    else:
         print("Not Perfect")

    ret = obj1.SumFactor()
    print("Sum of Factor:",ret)

    ret = obj1.Factor()
    print("Factors:",ret)
 
if __name__ =="__main__":
    main()