class Block:
    def __init__(self, height, W):
        self.height = height
        self.rectangle_widths = 0 
        self.full = False
        self.rectangles = []
        self.W = W
        
    def add_rectangle(self, rectangle):
        self.rectangle_widths += rectangle.width
        self.rectangles.append(rectangle)
        if self.rectangle_widths >= 1-self.W:
            self.full = True
                    
    def get_full(self):
        return self.full

    def __str__(self):
        return f"Block({self.height})"
    
    def __repr__(self):
        return self.__str__()
