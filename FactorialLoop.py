'''
Accept a number and print its factorial using for loop
enter number  5
output        120
'''
def Factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
        i = i + 1
    return fact

def main():
    print("Enter number:")
    no = int(input())
    ret = Factorial(no)
    print("Factorial number:",ret)
if __name__ =="__main__":
    main()