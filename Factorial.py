def main():
    print("Enter number:")
    no= int(input())
    Fact = 1
    for i in range(1,no+1):
        Fact = Fact * i
    print(Fact)

if __name__ =="__main__":
    main()