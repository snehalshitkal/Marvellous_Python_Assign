'''
Accept single character from user and check it vowel(a,e,i,o,u)
if not print it consonant
'''

def main():
    print("Enter character:")
    ch = (input())
    if(ch =='a' or ch == 'e'or ch == 'i'or ch == 'o'or ch == 'u'):
        print("It is Vowels")
    else:
        print("It is Consonant:") 
if __name__ == "__main__":
    main()