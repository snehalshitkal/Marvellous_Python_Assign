#   Write a recursive function to calculate sum of digit
#   sumofdigit(1+2+3+4)   =  10

sum = 0
def SumDigit(No):
    global sum
    if(No >= 1):
        sum = sum + No
        No = No - 1
        SumDigit(No)
    return sum

def main():
    ret = SumDigit(4)
    print("Sum of Digit:",ret)

if __name__=="__main__":
    main()