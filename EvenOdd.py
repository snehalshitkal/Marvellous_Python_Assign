'''
Write a program to check wheter the entered number is even or odd
'''
def main():
    no = int(input("Enter number:"))
    if(no%2==0):
        print("Even Number",no)
    else:
        print("Odd Number:",no)
if __name__ =="__main__":
    main()