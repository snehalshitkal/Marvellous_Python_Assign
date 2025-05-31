'''
Area and Perimeter of Rectangle
'''

def RectangleArea(l ,w):
    area = 0
    area = l * w
    return area

def Perimeter(l , w):
    perimeter = 0
    perimeter = 2*(l + w)
    return perimeter

def main():
    print("Enter Length:")
    Length = int(input())
    print("Enter Width:")
    width = int(input())

    ret = RectangleArea(Length,width)
    print("Area of Rectangle:",ret)

    ret = Perimeter(Length,width)
    print("Perimeter of Rectangle:",ret)

if __name__ =="__main__":
    main()