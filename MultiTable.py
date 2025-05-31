'''
Accept number from user print it multiplication up to 10.
enter no : 7
7 * 1 = 7
7 * 2 = 14
.....
7 * 10 = 70
'''

def main():
    print("Accept Number from user:")
    no = int(input())
    mul = 1
    for i in range(1,11):
        mul= i * no
        print(f"{no}   X   {i}  = ",mul)

if __name__ =="__main__":
    main()