'''
Write a program which Accept N number from user and store it into List.
return Minimum number from that list
Input:   6
         13    5     45      7       4       56
output:  4
'''

def MinimumNo():
    print("Enter number of element:")
    No = int(input())
    List = []
    for i in range(No):
        print("Enter Elements:")
        ele = int(input())
        List.append(ele)
    result = min(List)
    return result

def main():
    ret = MinimumNo()
    print("Minimum Number:",ret)

if __name__ =="__main__":
    main()

