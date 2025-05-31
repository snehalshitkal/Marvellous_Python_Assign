'''
write a function that accept a list of integer and return a list of prime number
using filter function
enter list : 10,11,12,13,14,15,16,17
output  :    11,13,17
'''
from functools import reduce

def Prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def main():
    List = []
    print("Enter how many number of element of list")
    element = int(input())
    for i in range(element):
        print("Enter element:")
        num = int(input())
        List.append(num)

    print("List:",List)

    fData = list(filter (Prime,List))
    print("Filter Data :",fData)

if __name__ =="__main__":
    main()
