def main():
    print("Enter Number:")
    no=int(input())

    for i in range(no):
        for j in range(no):
            print("*",end=" ")
        print()

if __name__=="__main__":
    main()