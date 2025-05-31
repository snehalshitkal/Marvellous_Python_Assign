#   Count how many zero are in given number
#   count_zeros(1020300)    - 4
count = 0
Digit = 0
def Count_Zero(No):
    global count
    global Digit
    while (No != 0):
        Digit = No%10
        if(Digit == 0):
            count = count + 1
        No = No / 10
        Count_Zero(No)
    return count
        
def main():
    print("Enter Number:")
    no = int(input())
    ret = Count_Zero(no)
    print("Number of Zeros are:",ret)

if __name__ =="__main__":
    main()