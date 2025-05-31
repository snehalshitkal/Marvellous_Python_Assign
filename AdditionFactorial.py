def main():
    print("Enter number:")
    no= int(input())
    sum = 0
    for i in range(1,no):
        if ((no % i)==0):
            sum = sum + i
    print(sum)

if __name__ =="__main__":
    main()