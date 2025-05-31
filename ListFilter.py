'''
Accept list of number and use filter() to keep only even number
Enter list : 1  2   3   4   5   6
Even number: 2  4   6
'''
from functools import reduce
def main():
    List = []
    print("Enter how many number of element of list")
    element = int(input())
    for i in range(element):
        print("Enter element:")
        num = int(input())
        List.append(num)

    print("List:",List)

    fData = list(filter (lambda no:(no%2==0),List))
    print("Filter Data :",fData)

if __name__ =="__main__":
    main()