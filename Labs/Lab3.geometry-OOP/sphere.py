from geometry_shape import Shape
from circle import Circle
from math import pi
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines


class Sphere(Circle):
    def __init__(self, x: float, y: float, z:float, radius: float) -> None:
        """A subclass of circle to represent sphere with (x, y, z) of the midpoint and radius"""
        super().__init__(x,y,radius)
        self.z = z

    @property
    def z(self) -> float:
        """Read-only property, can't set the z"""
        return self._z
    
    @z.setter
    def z(self, value: float) -> None:
        """Setter for z with error handling"""
        self._z = Shape.validate_number(value)
    
    def area(self) -> float:
        """Return the surface area of sphere"""
        return 4*pi*self.radius**2

    def perimeter(self) -> None:
        return NotImplemented # as we don't want define the perimeter method of sphere.
    
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
    
    def plot_sphere(self, x_point=None, y_point=None, z_point=None) -> None:
        """Draw sphere and a point"""
        # Reference: https://stackoverflow.com/questions/11140163/plotting-a-3d-cube-a-sphere-and-a-vector-in-matplotlib
        # Reference: https://stackoverflow.com/questions/40460960/how-to-plot-a-sphere-when-we-are-given-a-central-point-and-a-radius-size
        
        fig = plt.figure(dpi=100, figsize=(10,4))
        ax = plt.subplot(projection='3d')
        ax.set_aspect("auto")

        # draw sphere
        u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:20j]
        x = self.x+self.radius*np.cos(u)*np.sin(v)
        y = self.y+self.radius*np.sin(u)*np.sin(v)
        z = self.z+self.radius*np.cos(v)
        ax.plot_wireframe(x, y, z, color="blue",alpha=0.5)
        
        # draw midpoint and grid
        ax.plot(self.x, self.y, self.z, 's', color ="b")
        ax.grid()

        # draw any point to check
        if x_point !=None and y_point !=None:
           ax.plot(x_point,y_point, z_point, color='red', marker='*')
        
        # create legend
        shape = mlines.Line2D([], [], color='blue', marker='s', linestyle='None', markerfacecolor="white", markersize=6, label=f'Sphere: Radius: {self.radius}')
        midpoint_of_shape= mlines.Line2D([], [], color='blue', marker='s', linestyle='None', markersize=4, label=f'Midpoint of sphere: ({self.x}, {self.y}, {self.z})')
        point_to_check = mlines.Line2D([], [], color='red', marker='*', linestyle='None', markersize=4, label=f'Point to check: ({x_point}, {y_point}, {z_point})')
        
        plt.legend(handles=[shape, midpoint_of_shape, point_to_check], loc="upper right", fontsize='x-small')

        # create title and plot show
        ax.set(title="Plot sphere and point")
        plt.show()

    def __repr__(self) -> str:
        """Present the instance"""
        return f"Sphere with center point: ({self.x}, {self.y}, {self.z}) with radius: {self.radius}"