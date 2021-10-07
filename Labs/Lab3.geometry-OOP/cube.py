from geometry_shape import Shape
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib
from mpl_toolkits import mplot3d
import numpy as np


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations


class Cube(Shape):
    def __init__(self, x: float, y: float, z:float, side: float) -> None:
        """A subclass to represent cube with (x, y, z) of the midpoint, and side"""
        super().__init__(x,y)
        self.z = z
        self.side = side

    @property
    def z(self) -> float:
        """Read-only property, can't set the z"""
        return self._z
    
    @z.setter
    def z(self, value: float) -> None:
        """Setter for z with error handling"""
        self._z = Shape.validate_number(value)
    
    @property
    def side(self) -> float:
        """Read-only property, can't set the side"""
        return self._side
    
    @side.setter
    def side(self, value: float) -> None:
        """Setter for side with error handling"""
        self._side = Shape.validate_positive_number(value)
    
    def area(self) -> float:
        """Return the surface area of cube"""
        return 6*self.side**2
    
    def perimeter(self) -> float:
        """Return the perimeter of cube"""
        return 12*self.side
    
    def volume(self) -> float:
        """Return the volume of cube"""
        return self.side**3

    def is_inside(self,x_point:float, y_point:float, z_point:float) -> bool:
        """Return whether a point is in a cube"""
        #|x_point-self.x|<= 0.5*self.side --> self.x - 0.5*self.side <= x_point <= self.x + 0.5*self.side
        #|y_point-self.y|<= 0.5*self.side --> self.y - 0.5*self.side <= y_point <= self.y + 0.5*self.side
        #|z_point-self.z|<= 0.5*self.side --> self.z - 0.5*self.side <= z_point <= self.z + 0.5*self.side
        return Shape.hori_ver_dis(self.x, x_point) <= 0.5*self.side and Shape.hori_ver_dis(self.y, y_point) <= 0.5*self.side and Shape.hori_ver_dis(self.z, z_point) <= 0.5*self.side

    def translate(self, x_move:float, y_move:float,z_move:float) -> None:
        """A method to move x by x_move, move y by y_move, and move z by z_move"""
        super().translate(x_move, y_move)
        self._z = self.z + Shape.validate_number(z_move) 

    def __eq__(self, other) -> bool:
        """Return if two spheres are equal. The conditions are they should be the same type, and the sides are equal"""
        return type(self) == type(self) and self.side == other.side
 
    def plot_cube(self,x_point=None, y_point=None, z_point=None):
        fig = plt.figure()
        ax = plt.subplot(projection='3d')
        ax.set_aspect("auto")

        # draw cube
        r = [self.x-0.5*self.side, self.x+0.5*self.side]
        for s, e in combinations(np.array(list(product(r, r, r))), 2):
            if np.sum(np.abs(s-e)) == r[1]-r[0]:
                ax.plot3D(*zip(s, e), color="b")

        ax.plot(self.x, self.y, self.y,'s', color ="b")
        ax.grid()

        if x_point !=None and y_point !=None and z_point !=None:
            ax.plot(x_point,y_point,z_point, color='red', marker='*')



    def __repr__(self) -> str:
        """Present the instance"""
        return f"Cube with center point: ({self.x}, {self.y}, {self.z}) with side length: {self.side}"   

