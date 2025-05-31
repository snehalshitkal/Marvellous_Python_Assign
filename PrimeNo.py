'''
Accept number from user and check whether it is prime or no
'''
def PrimeNo(value):
    if value<0:
        value = -value

    for i in range(2, value+1):
        if(value%i==0):
            return False
        return True

def main():
    print("Enter Number:")
    no = int(input())
    
    ret = PrimeNo(no)
    if(ret == True):
        print("Prime number:")
    else:
        print("Not Prime number:")

if __name__ =="__main__":
    main()