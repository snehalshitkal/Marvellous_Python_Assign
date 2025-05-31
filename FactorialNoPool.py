'''
    Create Python Program using Multiprocessing.Pool
    to compare factorial number in a list
'''

import multiprocessing

def Factorial(No):
    for i  in range(1,n+1):
        fact = fact * no
    return fact

def main():
    number = [3,4,5,6,7]
    
    with multiprocessing.Pool() as pool:
        factNo = pool.map(Factorial,number)
        for num,f in zip(number,factNo):
            print("Factorial Number:",factNo)

if __name__ == "__main__":
    main()