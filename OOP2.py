class Circle:
    PI = 3.14

    def __init__(self,iRad):
        self.Radius = iRad
       

    
        
    def CalulateArea(self):
        Area = 0.0
        Area = Circle.PI * self.Radius  * self.Radius
        return Area

    def CalculateCircumference(self):
        Circumference = 0.0
        Circumference = 2 * Circle.PI * self.Radius
        return Circumference

    def Display(self):
        print("Inside Display:")

        ret = self.CalulateArea()
        print("Area of Circle are :",ret)

        ret = self.CalculateCircumference()
        print("Area of Circumference:",ret)

def main():
    print("Accept Radius from user:")
    radius = float(input())
 
    obj = Circle(radius)
   
    obj.Display()

if __name__ =="__main__":
    main()