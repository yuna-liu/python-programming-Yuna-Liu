from math import pi
from math import sqrt

class Shape:
    def __init__(self, x: float, y:float, type:str) -> None: #x: x coordinate, y: y coordinate
        self.x = x
        self.y = y
        self.type = type

    @property
    def x(self)-> float:
        return self._x
    
    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self, value: float) -> None:
        self._x = Shape.validate_number(value)

    @y.setter
    def y(self, value: float) -> None:
        self._y = Shape.validate_number(value)

    @staticmethod
    def validate_number(value):
        if not isinstance(value, (int,float)):
            raise TypeError (f"integer or float needed here, not {type(value)}.")
        else:
            return value

    @staticmethod
    def validate_non_negative_number(value):
        if not isinstance(value, (int, float)):
            raise TypeError (f"integer or float number needed here, not {type(value)}.")
        if value < 0:
            raise ValueError (f"non-negative number needed here. {value} is negative.")
        else:
            return value

    @staticmethod
    def validate_positive_number(value):
        if not isinstance(value, (int, float)):
            raise TypeError (f"integer or float number needed here, not {type(value)}.")
        if value <= 0:
            raise ValueError (f"positive number needed here. {value} is not ok.")
        else:
            return value

    # calculate euclidean distance between two points: self(x1, y1, z1) and any point(x2, y2, z2)
    # by default, z1=0 and z2=0 to get 2D distance.
    @staticmethod
    def eu_dis(x1:float, x2:float, y1:float, y2:float, z1=0, z2=0) -> float:
        x2_valid = Shape.validate_number(x2)
        y2_valid = Shape.validate_number(y2)
        z2_valid = Shape.validate_number(z2)
        return sqrt((x2_valid-x1)**2+(y2_valid-y1)**2+(z2_valid-z1)**2)

    # to calculate the horizontal or vertical distance of the midpoint and any point
    # for example: abs(x2-x1) is the horizontal distance between two x-coordinates
    # abs(y2-y1) is the vertical distance between two y-coordinates
    # n1 stands for the self
    # n2 stands for any point
    @staticmethod      
    def hori_ver_dis(n1:float, n2:float) -> float:
        n2_valid = Shape.validate_number(n2)
        return abs(n1-n2_valid)

          
    # to compare whether two shapes have the same area
    def __eq__(self, other) -> bool:
        if self.type == other.type and self.area() == other.area():
            return True
        else:
            return False
    
    # a translation method to move x by x_move, and move y by y_move
    def translate(self, x_move:float, y_move:float) -> None:
        self._x =  self.x + Shape.validate_number(x_move)
        self._y =  self.y + Shape.validate_number(y_move)

    def __repr__(self) -> str:
        return f"{self.type} with center point: ({self.x}, {self.y})."