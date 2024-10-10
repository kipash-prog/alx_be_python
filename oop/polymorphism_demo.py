class Shape:
    def area(self):
        raise "NotImplementedError"
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length *self.width
       
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius  = radius
        
    def area(self):
        return self.radius * self.radius * 3.14
       