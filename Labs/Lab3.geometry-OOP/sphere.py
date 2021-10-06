from geometry_shape import Shape
from math import pi


class Sphere(Shape):
    def __init__(self, x: float, y: float, z:float, radius: float) -> None:
        """A subclass to represent sphere with (x, y, z) of the midpoint and radius"""
        super().__init__(x,y)
        self.z = z
        self.radius = radius

    @property
    def z(self) -> float:
        """Read-only property, can't set the z"""
        return self._z
    
    @z.setter
    def z(self, value: float) -> None:
        """Setter for z with error handling"""
        self._z = Shape.validate_number(value)
    
    @property
    def radius(self) -> float:
        """Read-only property, can't set the radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        """Setter for radius with error handling"""
        self._radius = Shape.validate_positive_number(value)
    
    def surface_area(self) -> float:
        """Return the surface area of sphere"""
        return 4*pi*self.radius**2
    
    def volume(self) -> float:
        """Return the volume of sphere"""
        return (4/3)*pi*self.radius**3

    def is_inside(self,x_point:float, y_point:float, z_point:float) -> bool:
        """Return whether a point is in a sphere."""
        mid_to_point = Shape.eu_dis(self.x, x_point, self.y, y_point, self.z, z_point)
        return mid_to_point <= self.radius

    def translate(self, x_move:float, y_move:float,z_move:float) -> None:
        """A method to move x by x_move, move y by y_move, and move z by z_move"""
        super().translate(x_move, y_move)
        self._z = self.z + Shape.validate_number(z_move) 

    def __eq__(self, other) -> bool:
        """Return if two spheres are equal. The conditions are they should be the same type, and the radius are equal"""
        return type(self) == type(other) and self.radius == other.radius
 
    def __repr__(self) -> str:
        """Present the instance"""
        return f"Sphere with center point: ({self.x}, {self.y}, {self.z}) with radius: {self.radius}"