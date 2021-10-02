from geometry_shape import Shape

class Cube(Shape):
    def __init__(self, x: float, y: float, z:float, side: float, type="cube") -> None:
        super().__init__(x,y,type)
        self.z = z
        self.side = side

    @property
    def z(self) -> float:
        return self._z
    
    @z.setter
    def z(self, value: float) -> None:
        self._z = Shape.validate_number(value)
    
    @property
    def side(self) -> float:
        return self._side
    
    @side.setter
    def side(self, value: float) -> None:
        self._side = Shape.validate_positive_number(value)
    
    def area(self) -> float:
        return 6*self.side**2
    
    def perimeter(self) -> float:
        return 12*self.side

    # return whether a point is in a shape.
    # x_point, y_point, z_point are checked valid through Shape.hori_ver_dis() method.
    def is_inside(self,x_point:float, y_point:float, z_point:float) -> bool:
        if Shape.hori_ver_dis(self.x, x_point) <= 0.5*self.side and Shape.hori_ver_dis(self.y, y_point) <= 0.5*self.side and Shape.hori_ver_dis(self.z, z_point) <= 0.5*self.side:
            return True
        else:
            return False

    def translate(self, x_move:float, y_move:float,z_move:float) -> None:
        super().translate(x_move, y_move)
        self._z = self.z + Shape.validate_number(z_move) 
 
    def __repr__(self) -> str:
        return f"{self.type} with center point: ({self.x}, {self.y}, {self.z}) with side length: {self.side}"   