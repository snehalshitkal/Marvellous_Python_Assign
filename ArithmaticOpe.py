'''
Arithmatic operation of two number
sum,difference,product,division
'''
def Sum (value1 , value2):
    Ans = 0
    Ans = value1 + value2
    return Ans

def Difference (value1 , value2):
    Ans = 0
    Ans = value1 - value2
    return Ans

def Product (value1 , value2):
    Ans = 0
    Ans = value1 * value2
    return Ans

def Division (value1 , value2):
    Ans = 0
    Ans = value1 / value2
    return Ans

def main():
    print("Enter First Number:")
    no1 = int(input())
    print("Enter Second number:")
    no2 = int(input())

    ret = Sum(no1,no2)
    print("Sum",ret)
    ret = Difference(no1,no2)
    print("Difference",ret)
    ret = Product(no1,no2)
    print("Product",ret)
    ret = Division(no1,no2)
    print("Division",ret)

if __name__ =="__main__":
    main()