'''
Write a program which Accept N number from user and store it into List.
return Maximum number from that list
Input:   6
         13    5     45      7       4       56
output:  56
'''
def MaximumNo():

    print("Enter the how many element in list:")
    no = int(input())
    List = []

    for i in range(no):
        print("Enter Element")
        num = int(input())
        List.append(num)

    result = max(List)
    return result
    
def main():
    ret = MaximumNo()
    print("Maximum No:",ret)

if __name__ =="__main__":
    main()