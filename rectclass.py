class rectangle:
    def getdata(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def showdata(self):
        print("Length=",self.length)
        print("Breadth=",self.breadth)
    def area(self):
        return(self.length * self.breadth)

a = int(input("Enter length:"))
b = int(input("Enter breadth:"))
r1 = rectangle()
r1.getdata(a,b)
r1.showdata()
print("The area of the rectangle is:",r1.area())

