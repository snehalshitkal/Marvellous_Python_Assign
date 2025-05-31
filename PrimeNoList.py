'''
 Accept N number from user and store it List.
 return addition of all prime number from that list.
 Main python file accept  N number from user pass each no to checkprime()
 userdefined module MavellousNum.
 Name of the function from main python file should be ListPrime()
 Input : 13      5      45      7       4       56      10   34    2   5   8
 output :54(13+5+7+2+5)   

'''
from MarvellousNum import CheckPrime
def ListPrime():
    print("Enter how many element in our List:")
    no = int(input())
    List = []
    for i in range(n):
        print("Enter Element:")
        num = int(input())
        List.append(num)

    prime_sum = 0
    for num in List:
        if CheckPrime(num):
            prime_sum = prime_sum + num
    print("Sum of All Prime number:",prime_sum)
