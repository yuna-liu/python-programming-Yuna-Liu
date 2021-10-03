from geometry_shape import Shape

class Rectangle(Shape):
    def __init__(self, x: float, y: float, side1: float, side2: float) -> None: 

        #side1 is the length on the horizontal line of the rectangle.
        #side2 is the length on the vertical line of the rectangle.

        super().__init__(x,y)
        self.side1 = side1
        self.side2 = side2
    
    @property
    def side1(self) -> float:
        return self._side1
    
    @side1.setter
    def side1(self, value: float) -> None:
        self._side1 = Shape.validate_positive_number(value)

    @property
    def side2(self) -> float:
        return self._side2
    
    @side2.setter
    def side2(self, value: float) -> None:
        self._side2 = Shape.validate_positive_number(value)
    
    def area(self) -> float:
        return self.side1*self.side2
    
    def perimeter(self) -> float:
        return 2*(self.side1+self.side2)

    # return whether a point is in a shape
    # x_point and y_point are checked valid through method Shape.hori_ver_dis()
    def is_inside(self, x_point:float, y_point:float) -> bool:
        if Shape.hori_ver_dis(self.x, x_point) <= 0.5*self.side1 and Shape.hori_ver_dis(self.y, y_point) <= 0.5*self.side2:
            return True
        else:
            return False
    
    def __eq__(self, other) -> bool:
        if type(self) == type(self) and self.area() == other.area() and self.side1 == other.side1 and self.side2 == other.side2:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Rectangle with center point: ({self.x}, {self.y}) with (horizontal side, vertical side): ({self.side1}, {self.side2})."  