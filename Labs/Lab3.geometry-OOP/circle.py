
from geometry_shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        """A subclass to represent circle with x-coordinate, y-coordinate and radius"""
        super().__init__(x,y)
        self.radius = radius
    
    @property
    def radius(self) -> float:
        """ Read-only property, can't set the radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        """ Setter for for radius with error handling"""
        self._radius = Shape.validate_positive_number(value)
    
    def area(self) -> float:
        """Return the area of circle"""
        return float(pi*(self.radius**2))
    
    def perimeter(self) -> float:
        """Return the perimeter of circle"""
        return 2*pi*self.radius

    def is_inside(self,x_point:float, y_point:float) -> bool:
        """return whether a point is in a circle"""
        mid_to_point = Shape.eu_dis(self.x, x_point, self.y, y_point)
        return mid_to_point <= self.radius
 
    # to compare whether two shapes have the same area
    def __eq__(self, other) -> bool:
        """Return if two circles are equal"""
        return type(self) == type(other) and self.area() == other.area()

    def __repr__(self) -> str:
        """present the instance"""
        return f"Circle with center point: ({self.x}, {self.y}) with radius: {self.radius}" 