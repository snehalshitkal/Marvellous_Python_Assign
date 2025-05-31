'''
Program which Accept N number from user and store it into List.
return addition of all that element from that list
Input:   6
         13    5     45      7       4       56
output:  130    
'''
def SumElement():

    print("enter how many number in list:")
    No = int(input())
    List = []

    for i in range(No):
        Num=int(input("Enter number:"))
        List.append(Num)
    total = sum(List)
    return total

result = SumElement()
print("Addition:",result)
