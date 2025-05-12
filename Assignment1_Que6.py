def fun(Value):
    if (Value>0):
        print("Positive Number:",Value)
    elif (Value<0):
        print("Negative Number:",Value)
    else:
        print("Zero:",Value)
print("Enter Number")
no=int(input())
fun(no)