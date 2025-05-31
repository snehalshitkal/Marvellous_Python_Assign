'''
Accept 5 number from user.Find and print largest number 
'''
number = []
for i in range(5):
    print("Enter numbers:")
    num=int(input())
    number.append(num)
    
if number:
    larg = number[0]
    for num in number:
        if num > larg:
            larg = num
    print("largest number:",larg)