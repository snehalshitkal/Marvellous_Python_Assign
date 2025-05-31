'''
    Program contain filter(),map(),reduce() in it.
    List contain number accept from user
    flter should number greater than or equal to 70 and less than or equal to 90
    Map increase each number by 10
    reduce will return product of all that number
'''
from functools import reduce

def checkNumber(no):
    return ((no>=70)&(no<=90))

def Increase(no):
    return (no + 10)

def Product(A,B):
    return (A * B)

Data = [4,34,36,76,68,24,89,23,86,90,45,70]
print("Input Data:",Data)

fData = list(filter(checkNumber,Data))
print("Filter Data:",fData)

mData = list(map(Increase,fData))
print("Increase by 10:",mData)

rData = reduce(Product,mData)
print("product of all :",rData)

