"""
    Sum of first N Natural Number
    write a recursive fun to calculate sum from 1 to n
    Sum_n(5)  15
"""
sum = 0
i = 0
def sumNatural(iNo):
    global sum
    global i
    if(iNo>=i):
        sum = sum + i
        i = i + 1
        sumNatural(iNo)
    return sum

def main():
    print("Enter Number:")
    no = int(input())
    ret = sumNatural(no)
    print("Sum of Natural Number:",ret)
if __name__ == "__main__":
    main()