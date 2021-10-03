
from geometry_shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x,y)
        self.radius = radius
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = Shape.validate_positive_number(value)
    
    def area(self) -> float:
        return float(pi*(self.radius**2))
    
    def perimeter(self) -> float:
        return 2*pi*self.radius

    # return whether a point is in a shape
    # x_point, y_point are checked valid through Shape.eu_dis() method.
    def is_inside(self,x_point:float, y_point:float) -> bool:
        mid_to_point = Shape.eu_dis(self.x, x_point, self.y, y_point)
        if mid_to_point <= self.radius:
            return True
        else:
            return False
 
    # to compare whether two shapes have the same area
    def __eq__(self, other) -> bool:
        if type(self) == type(other) and self.area() == other.area():
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Circle with center point: ({self.x}, {self.y}) with radius: {self.radius}" 