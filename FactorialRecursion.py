# Factorial using Recurssion
#Calculate number using Recurssion function
# input 5 
# output 120

fact= 1
def Factorial(iNo):
    global fact
    if (iNo > 1):
        fact = fact * iNo
        iNo = iNo - 1
        Factorial(iNo)
    return fact
def main():
    print("Enter Number")
    No = int(input())
    ret = Factorial(No)
    print("Factorial :",ret)

if __name__=="__main__":
    main()