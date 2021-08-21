class Rectangle: 
    def __init__(self, width, height):
        self.height, self.width = height, width

    def rotate(self):
        self.height, self.width = (self.width, self.height) if self.height < self.width else (self.height, self.width)
        
    def get_dimensions(self):
        return self.height, self.width
    
    def get_area(self):
        return self.height * self.width
    
    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"
    
    def __repr__(self):
        return self.__str__()