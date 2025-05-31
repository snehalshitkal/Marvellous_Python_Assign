'''
Two thread named as Thread1 and Threa2.
Thread1 display 1 to 50 on screen.
Thread2 display 50 to 1 in reverse order on screen.
After execution of thread1 gets completed then schedule thread2.

'''
import threading
def NumDisplay(num):
    for i in range(1,num+1):
        print(i)

def RevNumDisplay(num):
    for i in range(num,0,-1):
        print(i)

def main():
    print("Inside main:")
    Thread1 = threading.Thread(target = NumDisplay,args=(50,))
    Thread2 = threading.Thread(target = RevNumDisplay,args=(50,))
    Thread1.start()
    Thread1.join()
    print("Second Thread:")
    Thread2.start()
    Thread2.join()
    print("Exit main thread:")

if __name__ =="__main__":
    main()