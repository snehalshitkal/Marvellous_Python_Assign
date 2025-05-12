def ChkNum(Value):
    if(int(Value%2)==0):
        print("Even Number:",Value)
    else:
        print("Odd Number:",Value)


print("Enter Number")
no =int(input())
ChkNum(no)
