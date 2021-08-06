pi=3.14
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return pi*(self.radius**2)
    def circumference(self):
        return (2*pi*(self.radius))
r = int(input("Enter radius of the circle:"))
cr = circle(r)
print("Area:",cr.area())
print("Circumference:",cr.circumference())
