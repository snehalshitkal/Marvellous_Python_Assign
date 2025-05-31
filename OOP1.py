class Demo:
    value = 0

    def __init__(self,iNo1,iNo2):
        self.no1 = iNo1
        self.no2 = iNo2

    def Fun(self):
        print("Inside Fun Function:")
        print(self.no1)
        print(self.no2)

    def Gun(self):
        print("Inside Gun Function:")
        print(self.no1)
        print(self.no2)

def main():
    obj1 = Demo(11,21)
    obj2= Demo(51,101)

    obj1.Fun()
    obj1.Gun()
    obj2.Fun()
    obj2.Gun()

if __name__ =="__main__":
    main()