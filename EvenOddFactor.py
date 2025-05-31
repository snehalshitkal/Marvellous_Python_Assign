'''
Create two thread Evenfactor and oddfactor
Both thread accept one parameter as integer.
Evenfactor thread display addition of even factor of given number.
oddfactor thread display addition of odd factor of given number
'''

import threading

def EvenFactor(no):
    sum = 0
    for i in range(1,no+1):
        if((no%i==0)&(i%2==0)):
            sum = sum + i
    return sum

def OddFactor(no):
    sum = 0
    for i in range(1,no+1):
        if((no%i==0)&(i%2!=0)):
            sum = sum + i
    return sum

def main():
    print("Start main thread:")
    print("Enter Number:")
    number = int(input())
    EvenThread = threading.Thread(target = EvenFactor,args=(number,))
    OddThread = threading.Thread(target = OddFactor,args=(number,))
    EvenThread.start()
    OddThread.start()
    EvenThread.join()
    OddThread.join()

    print("Exit main Thread:")

if __name__ =="__main__":
    main()