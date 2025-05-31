# Print Number Using Recursion
# n = 5
#output 1   2   3   4   5
i =  0
def Num(No):
    global i
    if(No > i):  
        i = i + 1 
        print(i)
        Num(No)

def main():
    Num(5)

if __name__ =="__main__":
    main()