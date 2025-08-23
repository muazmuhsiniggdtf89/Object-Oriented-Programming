class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)  
print(newRectangle.rectangle_area())      
