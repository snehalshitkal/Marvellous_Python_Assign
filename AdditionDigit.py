def main():
    print("Enter Number:")
    no = int(input())
    iDigit = 0
    iSum = 0
    while ( no != 0):
        iDigit = iDigit % 10
        iSum = iSum + iDigit
        no = no /10
    print("Addition of Digit:",iSum)

if __name__ =="__main__":
    main()