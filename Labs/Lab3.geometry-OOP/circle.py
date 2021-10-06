
from geometry_shape import Shape
from math import pi
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


class Circle(Shape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        """A subclass to represent circle with (x, y) of the midpoint and radius"""
        super().__init__(x,y)
        self.radius = radius
    
    @property
    def radius(self) -> float:
        """Read-only property, can't set the radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        """Setter for radius with error handling"""
        self._radius = Shape.validate_positive_number(value)
    
    def area(self) -> float:
        """Return the area of circle"""
        return float(pi*(self.radius**2))
    
    def perimeter(self) -> float:
        """Return the perimeter of circle"""
        return 2*pi*self.radius

    def is_inside(self,x_point:float, y_point:float) -> bool:
        """Return whether a point is in a circle"""
        mid_to_point = Shape.eu_dis(self.x, x_point, self.y, y_point)
        return mid_to_point <= self.radius
 
    # to compare whether two shapes have the same area
    def __eq__(self, other) -> bool:
        """Return if two circles are equal. The conditions are they have the same type and the same radius"""
        return type(self) == type(other) and self.radius == other.radius

    def __repr__(self) -> str:
        """Present the instance"""
        return f"Circle with center point: ({self.x}, {self.y}) with radius: {self.radius}" 

    def plot_circle(self,x_point=None, y_point=None):
        circle_to_plot = plt.Circle((self.x, self.y), self.radius, color="b", fill=False, clip_on=False)
        fig, ax = plt.subplots(dpi=150,figsize=(10,4))
        ax.set_xlim(self.x-self.radius-2, self.x+self.radius+2)
        ax.set_ylim(self.y-self.radius-2, self.y+self.radius+2)
        ax.set_aspect('equal')
        ax.add_patch(circle_to_plot)
        ax.plot(self.x, self.y,'s', color ="b")

        if x_point !=None and y_point !=None:
            ax.plot(x_point,y_point, color='red', marker='*')

        #https://stackoverflow.com/questions/47391702/matplotlib-making-a-colored-markers-legend-from-scratch
        midpoint_of_circle= mlines.Line2D([], [], color='blue', marker='s', linestyle='None', markersize=10, label=f'Midpoint: ({self.x}, {self.y}); Radius: {self.radius}')
        pont_to_check = mlines.Line2D([], [], color='red', marker='*', linestyle='None', markersize=10, label=f'Point to check:({x_point}, {y_point})')
        plt.legend(handles=[midpoint_of_circle, pont_to_check])

        ax.set(title="Plot circle and point")

    