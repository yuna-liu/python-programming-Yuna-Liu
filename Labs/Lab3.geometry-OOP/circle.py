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

    def plot_circle(self,x_point=None, y_point=None) -> None:
        """Draw circle and a point"""
        # draw cirlce
        data_to_plot = plt.Circle((self.x, self.y), self.radius, color="b", fill=False, clip_on=False)
        fig, ax = plt.subplots(dpi=100,figsize=(10,4))

        # draw any point to check and set xlim and ylim
        if x_point !=None and y_point !=None:
            ax.plot(x_point,y_point, color='red', marker='*')
            if self.is_inside(x_point, y_point):
                ax.set_xlim(self.x-self.radius-1, self.x+self.radius+1)
                ax.set_ylim(self.y-self.radius-1, self.y+self.radius+1)
            else:
                ax.set_xlim(-x_point-1, x_point+1)
                ax.set_ylim(-y_point-1, y_point+1)
                # The "-1" in each of ax.set_xlim and ax.set_ylim is motivated to evoid drawing on the figure boundary.
        

        ax.set_aspect('equal')
        ax.add_patch(data_to_plot)

        # draw midpoint and grid
        ax.plot(self.x, self.y,'s', color ="b")
        ax.grid()

        # create legend
        # Reference: https://stackoverflow.com/questions/47391702/matplotlib-making-a-colored-markers-legend-from-scratch
        # Reference: https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html
        shape = mlines.Line2D([], [], color='blue', marker='o', linestyle='None', markerfacecolor="white", markersize=6, label=f'Circle:(({x_point}, {y_point}), Radius: {self.radius})')
        midpoint_of_shape= mlines.Line2D([], [], color='blue', marker='s', linestyle='None', markersize=4, label=f'Midpoint of circle: ({self.x}, {self.y})')
        point_to_check = mlines.Line2D([], [], color='red', marker='*', linestyle='None', markersize=4, label=f'Point to check:({x_point}, {y_point})')
        
        plt.legend(handles=[shape, midpoint_of_shape, point_to_check], loc="upper right", framealpha= 0.2, fontsize='small')

        # create title and plot show
        ax.set(title="Plot circle and point")
        plt.show()

    