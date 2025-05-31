class Arithmatic:
    def __init__(self,no1,no2):
        self.Value1 = no1
        self.Value2 = no2
    
    #def Accept(self):
        
    def Addition(self):
        Result = 0
        Result = self.Value1 + self.Value2
        return Result

    def Substraction(self):
        Result = 0
        Result = self.Value1 - self.Value2
        return Result


    def Multiplication(self):
        Result = 0
        Result = self.Value1 * self.Value2
        return Result


    def Division(self):
        Result = 0
        Result = self.Value1 / self.Value2
        return Result

def main():
    print("Enter First Number:")
    Value1 = int (input())

    print("Enter Second Number:")
    Value2 = int (input())

    obj = Arithmatic(Value1,Value2)
    #obj.Accept()
    ret = obj.Addition()
    print("Addition:",ret)

    ret = obj.Substraction()
    print("Substrction:",ret)


    ret = obj.Multiplication()
    print("Multiplication:",ret)


    ret = obj.Division()
    print("Division:",ret)

if __name__ =="__main__":
    main()