import ArithmaticModule

def main():
    print("Enter First Number:")
    no1 = int(input())
    print("Enter Second Number:")
    no2 = int(input())

    ans = ArithmaticModule.Addition(no1,no2)
    print("Addition:",ans)

    ans = ArithmaticModule.Substraction(no1,no2)
    print("Substraction:",ans)

    ans = ArithmaticModule.multiplication(no1,no2)
    print("Multiplication:",ans)

    ans = ArithmaticModule.Division(no1,no2)
    print("Division:",ans)

if __name__=="__main__":
    main()