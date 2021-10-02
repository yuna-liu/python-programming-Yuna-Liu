from geometry_shape import Shape
from math import pi


class Sphere(Shape):
    def __init__(self, x: float, y: float, z:float, radius: float, type="sphere") -> None:
        super().__init__(x,y,type)
        self.z = z
        self.radius = radius

    @property
    def z(self) -> float:
        return self._z
    
    @z.setter
    def z(self, value: float) -> None:
        self._z = Shape.validate_number(value)
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = Shape.validate_positive_number(value)
    
    def area(self) -> float:
        return 4*pi*self.radius**2
    
    def perimeter(self) -> float:
        return 2*pi*self.radius

    # return whether a point is in a shape
    # x_point, y_point, z_point are checked valid through Shape.eu_dis() method.
    def is_inside(self,x_point:float, y_point:float, z_point:float) -> bool:
        mid_to_point = Shape.eu_dis(self.x, x_point, self.y, y_point, self.z, z_point)
        if mid_to_point <= self.radius:
            return True
        else:
            return False

    def translate(self, x_move:float, y_move:float,z_move:float) -> None:
        super().translate(x_move, y_move)
        self._z = self.z + Shape.validate_number(z_move) 
 
    def __repr__(self) -> str:
        return f"{self.type} with center point: ({self.x}, {self.y}, {self.z}) with radius: {self.radius}"  