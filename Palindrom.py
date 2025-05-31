'''
Write a function that accept string and check whether it is a palindrom
input   radar
output  radar   
'''
def Palindrom(string):
    string= string.lower().replace(" "," ")
    return string == string[::-1]

def main():
    print("Enter String:")
    str = input()
    if Palindrom(str):
        print("Palindrom:")
    else:
        print("not Palindrom:")
if __name__ =="__main__":
    main()