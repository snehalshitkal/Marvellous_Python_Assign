'''
Compare Execution time  of summing number from 1 to 10 million
using normal function thread and multiprocessing
'''
import multiprocessing
import os
import time
def SumEven(no):
    sum = 0
    for i in range(2,no+1,2):
        sum = sum + i
    print(sum)

def SumOdd(no):
    sum = 0
    for i in range (1,no+1,2):
        sum = sum +i
    print(sum)
    

def main():
    print("Execution time:")
    start_time = time.time()
    T1= multiprocessing.Process(target = SumEven,args = (100000000),)
    T2 = multiprocessing.Process(target = SumOdd,args = (100000000),)
    T1 . start()
    T2.start()
    T1.join()
    T2.join()
    end_time = time.time()
    print("Time of Execution:",end_time - start_time)

if __name__ =="__main__":
    main()