def main():
    print("Enter Number:")
    no = int(input())
    i = 0
    while(no!=0):
        no = no / 10
        i = i + 1 
    print("Number of digit",i) 

if __name__ =="__main__":
    main()