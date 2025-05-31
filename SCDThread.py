'''
Create thread as small,capital,digits.
All thread accept string parameter.
Small thread display number of small character.
Capital thread display numbr of Capital character.
Digit thread dispaly Number of digit.
display id and name of each thread.
'''
import threading

def SmallDisplay(input_string):
    print("Display id",threading.get_ident())
    print("Name of Thread:",threading.current_thread().name)
    count = sum(1 for ch in input_string if ch.islower())
    print(count)
    
def CapitalDisplay(input_string):
    print("Display id",threading.get_ident())
    print("Name of Thread:",threading.current_thread().name)
    count = sum(1 for ch in input_string if ch.isupper())
    print(count)
    

def DigitDisplay(input_string):
    print("Display id",threading.get_ident())
    print("Name of Thread:",threading.current_thread().name)
    #count = 0
    count = sum(1 for ch in input_string if ch.isdigit())
    print(count)
    

def main():
    string = "SnehalShitkal23"
    Small = threading.Thread(target=SmallDisplay,args=(string,))
    Capital = threading.Thread(target = CapitalDisplay,args=(string,))
    Digit = threading.Thread(target = DigitDisplay,args=(string,))

    Small.start()
    Capital.start()
    Digit.start()
    Small.join()
    Capital.join()
    Digit.join()

if __name__ =="__main__":
    main()