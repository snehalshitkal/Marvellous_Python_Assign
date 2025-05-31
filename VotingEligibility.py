'''
Accept age from user check whwther the person is eligible to vote
age should be 18 or above
'''
def main():
    print("Enter Age:")
    age = int(input())
    if(age>=18):
        print("Elibile to Vote:")
    else:
        print("Not Eligible to vote:")

if __name__ =="__main__":
    main()