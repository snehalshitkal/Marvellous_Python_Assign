'''
Program contain filter(),map(),reduce() in it.
list of number accepted from user.
filter should number which are even.
map fun will calculate it square.
reduce will return addition of all number.
'''
from functools import reduce

def checkEven(No):
    return (No % 2 ==0)

def Square(No):
    return No * No

def Addition(No1,No2):
    return (No1+No2)

Data = [5,2,3,4,3,4,1,2,8,10]
print("List of Number:",Data)

fData = list(filter(checkEven,Data))
print("Filter output:",fData)

mData = list(map(Square,fData))
print("Reduce data:",mData)

rData =reduce(Addition,mData) 
print("Addition :",rData)