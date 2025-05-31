'''
Celsius to Fahrenheit converter
F = (C * 9/5)+32
'''
def main():
    print("Enter Temperature:")
    Celsius = float(input())
    Fahrenheit = (Celsius * (9/5))+32

    print("Temperature in Fahrenheit:",Fahrenheit)
if __name__ =="__main__":
    main()