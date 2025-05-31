'''
Program which contain one Lambda fun which accepts one parameter
and return power of two
input   4       output  16
input   6       output  64
'''

power = lambda no: no * no

print("enter Number")
ino = int(input())
ret = power(ino)
print("Power of No:",ret)