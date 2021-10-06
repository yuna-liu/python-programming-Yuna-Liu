from geometry_shape import Shape

class Rectangle(Shape):
    def __init__(self, x: float, y: float, side1: float, side2: float) -> None: 
        """A subclass to represent rectangle with (x, y) of the midpoint, length and width"""
        """side1 is the length on the horizontal line of the rectangle."""
        """side2 is the length on the vertical line of the rectangle."""
        super().__init__(x,y)
        self.side1 = side1
        self.side2 = side2
    
    @property
    def side1(self) -> float:
        """Read-only property, can't set the side1"""
        return self._side1
    
    @side1.setter
    def side1(self, value: float) -> None:
        """Setter for side1 with error handling"""
        self._side1 = Shape.validate_positive_number(value)

    @property
    def side2(self) -> float:
        """Read-only property, can't set the side2"""
        return self._side2
    
    @side2.setter
    def side2(self, value: float) -> None:
        """Setter for side2 with error handling"""
        self._side2 = Shape.validate_positive_number(value)
    
    def area(self) -> float:
        """Return the area of rectangle"""
        return self.side1*self.side2
    
    def perimeter(self) -> float:
        """Return the perimeter of rectangle"""
        return 2*(self.side1+self.side2)
    
    def is_inside(self, x_point:float, y_point:float) -> bool:
        """Return whether a point is in a rectangle"""
        #|x_point-self.x|<= 0.5*self.side1 --> -0.5*self.side1 <= x_point-self.x <=0.5*self.side1
        #--> self.x - 0.5*self.side1 <= x_point <= self.x + 0.5*self.side1
        #Similary, |y_point-self.y|<= 0.5*self.side2 --> self.y - 0.5*self.side1 <= y_point <= self.y + 0.5*self.side1
        return (Shape.hori_ver_dis(self.x, x_point) <= 0.5*self.side1) and (Shape.hori_ver_dis(self.y, y_point) <= 0.5*self.side2)
    
    def __eq__(self, other) -> bool:
        """Return if two rectangles are equal"""
        """The conditions are: (1) both shapes have the same type"""
        """(2) both shapes have the same area"""
        """(3) meanwhile the side1 of the first shape should be the same as either the side1 or side2 of the other shape."""
        return (type(self) == type(self)) and (self.area() == other.area()) and ((self.side1 == other.side1) or (self.side1 == other.side2))

    def __repr__(self) -> str:
        """Present the instance"""
        return f"Rectangle with center point: ({self.x}, {self.y}) with (horizontal side, vertical side): ({self.side1}, {self.side2})."  