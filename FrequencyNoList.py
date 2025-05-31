'''
    Accept N number from user and store it List.
    Accept one another no from user.
    return frequency of that number
    Input   6
            1   4    5    4    1    4
    output  3
'''

def frequency():
    print("Enter how many Element you want to input:")
    n = int(input())
    List = []

    for i in range(n):
        print("Enter number:")
        num = int(input())
        List.append(num)

    print("Enter search Element:")
    search_num = int(input())

    freq = List.count(search_num)
    return freq
def main():
    ret = frequency()
    print("Frequency of number:",ret)
if __name__ =="__main__":
    main()


