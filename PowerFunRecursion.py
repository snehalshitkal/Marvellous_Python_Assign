# Write recursion function to calculate x^n
#power(2,3) - 8

def Power(no,p):

    if p == 0:
        return 1

    return (no*Power(no,p-1))


def main():
    print("enter number:")
    n=int(input())
    print("Enter power:")
    pow=int(input())
    ret = Power(n,pow)
    print("No of Power:",ret)

if __name__ =="__main__":
    main()