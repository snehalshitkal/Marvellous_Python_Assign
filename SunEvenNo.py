'''
print sum of even number between 1 to 100
'''

def main():
    num = 1
    sum = 0
    while num<=100:
        if(num%2==0):
            sum = sum + num
        num = num + 1
    print("Sum of Even Number:",sum)

if __name__ == "__main__":
    main()