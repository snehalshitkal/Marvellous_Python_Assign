'''
write a recursive fun to print pattern
*
*   *
*   *   *
*   *   *   *
'''

i = 0
def Pattern(row):
    global i 
    if(row >= i):
        if (col > i + 1):
            print("*",i+1)
        Pattern(row)

def main():
    Pattern(4)

if __name__ == "__main__":
    main()