'''
    Program contain filter(),map(),reduce() in it.
    List contain number accept from user
    flter should out all prime number
    Map will multiply by each no 2
    reduce will return maximum number from that number
'''
from functools import reduce
def PrimeNo(No):
        for i in range(2,int(No**0.5)+1):
            if(No % i ==0):
                return false    
        return true

def Multiply(No):
    return (No * 2)

def Maxno(A,B):
    return (A>B)

Data = [2,70,11,10,17,23,31,77]
print("Input:",Data)

fData = list(filter(PrimeNo,Data))
print("Prime Number",fData)

mData = list(map(Multiply,fData))
print("multiply Each Number by 2:",mData)

rData = reduce(Maxno,mData)
print("Maximum number:",rData)