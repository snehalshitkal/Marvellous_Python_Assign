'''
Create two thread Evenlist oddlist.both thread accept list of integer parameter.
Even thread add all even element from input list and display the addition.
Oddlist thread add all element from input list & display addition.
'''
import threading
def Even(ListNum):
    sum = 0
    for i in ListNum:
        if (i%2==0):
            sum = sum +i
    print("Addition:",sum)        


def Odd(ListNum):
    sum = 0
    for i in ListNum:
        if (i%2!=0):
            sum = sum +i
    print("Addition:",sum)        


def main():
    print("Inside main thread")
    print("Enter no of element in list:")
    num = int(input())
    List = []

    for i in range(num+1):
        print("Enter elements:")
        element=int(input())

        List.append(element)
        print("List of elements:",List)

    EvenThread = threading.Thread(target = Even,args=(List,))
    OddThread = threading.Thread(target = Odd,args=(List,))

    EvenThread.start()
    OddThread.start()
    EvenThread.join()
    OddThread.join()

    print("Exit main thread:")
if __name__ == "__main__":
    main()