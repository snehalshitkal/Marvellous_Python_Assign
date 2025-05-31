'''
Accept list of integer from user and use map()
to double each value
enter list  1   2   3   4   5
double list 2   4   6   8   10
'''
no = 1
def doubleValue(no):
   return no * 2

def main():
    List = []
    print("Enter number of element in list")
    no = int(input())
    for i in range(no):
        print("Enter element")
        ele = int(input())
        List.append(ele)
    print(List)

    mData = list(map(doubleValue,List))
    print("doble list value",mData)

if __name__ =="__main__":
    main()