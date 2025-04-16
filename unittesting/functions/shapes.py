import math 



class Shape:
    def area():
        pass

    def perimeter():
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius
        #super().__init__()
    def area(self):
        return math.pi * self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
    

        
            