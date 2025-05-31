'''
Accept three number from user and print the largest using nested if else statement
'''
def main():
    no1 = int(input("Enter First number:"))
    no2 = int(input("Enter Second number:"))
    no3 = int(input("Enter Third number:"))

    if(no1 > no2):
        if(no1>no3):
            print("First no Large",no1)
        else:
            print("Third no Large:",no3)
    else:
        if (no2 > no3):
            print("Second number Large:",no2)
        else:
            print("Third no Large:",no3)
    

if __name__ =="__main__":
    main()