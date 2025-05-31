'''
Write a python program using Multiprocessing.
Process to square a list of Number using Multiple process.
'''

import multiprocessing


def square(n):
    return n*n

def main():
    number = [1,2,3,4,5]
    with multiprocessing.Pool() as pool:
        result = pool.map(square,number)
        print("Orignal Number:",number)
        print("Square number:",result)


if __name__ == "__main__":
    main()


