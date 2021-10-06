from math import pi
from math import sqrt

class Shape:
    """A class to represent geometry shape with x-coordinate and y-coordinate"""
    def __init__(self, x: float, y:float) -> None: #x: x coordinate, y: y coordinate
        self.x = x
        self.y = y

    @property
    def x(self)-> float:
        """Read-only property, can't set the x-cooridnate"""
        return self._x
    
    @property
    def y(self) -> float:
        """Read-only property, can't set the y-cooridnate"""
        return self._y

    @x.setter
    def x(self, value: float) -> None:
        """Setter for x-coordinate with error handling"""
        self._x = Shape.validate_number(value)

    @y.setter
    def y(self, value: float) -> None:
        """Setter for y-coordinate with error handling"""
        self._y = Shape.validate_number(value)

    @staticmethod
    def validate_number(value):
        """Validates if value is a number, in the sense of either integer or float """
        if not isinstance(value, (int,float)):
            raise TypeError (f"integer or float needed here, not {type(value)}.")
        return value

    @staticmethod
    def validate_positive_number(value):
        """Validates if value is a positive number, in the sense of either integer or float """
        if not isinstance(value, (int, float)):
            raise TypeError (f"integer or float number needed here, not {type(value)}.")
        if value <= 0:
            raise ValueError (f"positive number needed here. {value} is not ok.")
        return value

    @staticmethod
    def eu_dis(x1:float, x2:float, y1:float, y2:float, z1=0, z2=0) -> float:
        """Return euclidean distance between two points: (x1, y1, z1) and (x2, y2, z2)"""
        """by default, z1=0 and z2=0 to get 2D distance."""
        x1 = Shape.validate_number(x1)
        y1 = Shape.validate_number(y1)
        z1 = Shape.validate_number(z1)
        x2 = Shape.validate_number(x2)
        y2 = Shape.validate_number(y2)
        z2 = Shape.validate_number(z2)
        return sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)

    @staticmethod      
    def hori_ver_dis(n1:float, n2:float) -> float:
        """Return the horizontal or vertical distance of two points."""
        """For example: abs(x2-x1) is the horizontal distance between two x-coordinates"""
        """abs(y2-y1) is the vertical distance between two y-coordinates"""
        n1 = Shape.validate_number(n1)
        n2 = Shape.validate_number(n2)
        return abs(n1-n2)

    def __eq__(self, other) -> bool:
        """Return if two shapes are equal"""
        pass
    
        
    def translate(self, x_move:float, y_move:float) -> None:
        """A method to move x by x_move, and move y by y_move"""
        self._x =  self.x + Shape.validate_number(x_move)
        self._y =  self.y + Shape.validate_number(y_move)

    def __repr__(self) -> str:
        """Present the information of instance"""
        return f"Shape with center point: ({self.x}, {self.y})."