def main():
    print("Enter Number:")
    no = int(input())
    for i in range(2,no+1):
        if (((no % i)==0)&(i==no)):
           print("prime number")
        else:
            print("not prime number")
    

if __name__ == "__main__":
    main()