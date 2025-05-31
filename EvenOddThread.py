'''
create two thread named as even odd.
Even thread display first 10 even number.
Odd thread display first 10 odd number.
'''
import threading
def Even(no):
    for i in range(2,no+1,2):
        print(i)

def Odd(no):
    for i in range(1,no+1,2):
        print(i)


def main():
    print("Inside Main Thread:")
    T1 = threading.Thread(target = Even,args = (20,))
    T2 = threading.Thread(target = Odd,args = (20,))
    T1.start()
    T2.start()
    T1.join()
    T2.join()
    print("End of main Thread:")


if __name__ =="__main__":
    main()