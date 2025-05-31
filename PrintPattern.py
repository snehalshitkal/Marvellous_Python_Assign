'''
print Triangle pattern using nested loop
*
*   *
*   *   *
*   *   *   *
'''
print("Enter number")
no=int(input())
for i in range(0,no):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
