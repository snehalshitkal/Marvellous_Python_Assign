'''
Accept a list of number and use reduce() from functools .
find product of all number
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

    rData =reduce (lambda A,B:A*B,List)
    print("Reduce Data :",rData)

if __name__ =="__main__":
    main()