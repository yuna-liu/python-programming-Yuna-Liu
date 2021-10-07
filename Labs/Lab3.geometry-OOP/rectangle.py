from geometry_shape import Shape
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib

class Rectangle(Shape):
    def __init__(self, x: float, y: float, side1: float, side2: float) -> None: 
        """A subclass to represent rectangle with (x, y) of the midpoint, length and width"""
        """side1 is the length on the horizontal line of the rectangle."""
        """side2 is the length on the vertical line of the rectangle."""
        super().__init__(x,y)
        self.side1 = side1
        self.side2 = side2
    
    @property
    def side1(self) -> float:
        """Read-only property, can't set the side1"""
        return self._side1
    
    @side1.setter
    def side1(self, value: float) -> None:
        """Setter for side1 with error handling"""
        self._side1 = Shape.validate_positive_number(value)

    @property
    def side2(self) -> float:
        """Read-only property, can't set the side2"""
        return self._side2
    
    @side2.setter
    def side2(self, value: float) -> None:
        """Setter for side2 with error handling"""
        self._side2 = Shape.validate_positive_number(value)
    
    def area(self) -> float:
        """Return the area of rectangle"""
        return self.side1*self.side2
    
    def perimeter(self) -> float:
        """Return the perimeter of rectangle"""
        return 2*(self.side1+self.side2)
    
    def is_inside(self, x_point:float, y_point:float) -> bool:
        """Return whether a point is in a rectangle"""
        #|x_point-self.x|<= 0.5*self.side1 --> -0.5*self.side1 <= x_point-self.x <=0.5*self.side1
        #--> self.x - 0.5*self.side1 <= x_point <= self.x + 0.5*self.side1
        #Similary, |y_point-self.y|<= 0.5*self.side2 --> self.y - 0.5*self.side1 <= y_point <= self.y + 0.5*self.side1
        return (Shape.hori_ver_dis(self.x, x_point) <= 0.5*self.side1) and (Shape.hori_ver_dis(self.y, y_point) <= 0.5*self.side2)
    
    def __eq__(self, other) -> bool:
        """Return if two rectangles are equal"""
        """The conditions are: (1) both shapes have the same type"""
        """(2) both shapes have the same area"""
        """(3) meanwhile the side1 of the first shape should be the same as either the side1 or side2 of the other shape."""
        return type(self) == type(self) and self.area() == other.area() and (self.side1 == other.side1 or self.side1 == other.side2)

    def __repr__(self) -> str:
        """Present the instance"""
        return f"Rectangle with center point: ({self.x}, {self.y}) with (horizontal side, vertical side): ({self.side1}, {self.side2})."  

    def plot_rectangle(self,x_point=None, y_point=None):
        data_to_plot = matplotlib.patches.Rectangle((self.x-0.5*self.side1, self.y-0.5*self.side2), self.side1, self.side2, color="b", fill=False, linewidth = 2)
        #https://www.pythonpool.com/matplotlib-draw-rectangle/
        #matplotlib.patches.Rectangle((x,y), width, height)
        #x,y: This parameter represents the lower left point from which the rectangle plotting will start.
        fig, ax = plt.subplots(dpi=150,figsize=(10,4))
        ax.set_xlim(self.x-0.5*self.side1-1, self.x+0.5*self.side1+1)
        ax.set_ylim(self.y-0.5*self.side2-1, self.y+0.5*self.side2+1)
        ax.add_patch(data_to_plot)
        ax.plot(self.x, self.y,'s', color ="b")
        ax.grid()

        if x_point !=None and y_point !=None:
            ax.plot(x_point,y_point, color='red', marker='*')

        #https://stackoverflow.com/questions/47391702/matplotlib-making-a-colored-markers-legend-from-scratch
        shape = mlines.Line2D([], [], color='blue', marker='s', linestyle='None', markerfacecolor="white", markersize=10, label=f'Rectangle: (width: {self.side1}, height: {self.side2})')
        midpoint_of_shape= mlines.Line2D([], [], color='blue', marker='s', linestyle='None', markersize=6, label=f'Midpoint of rectangle: ({self.x}, {self.y})')
        point_to_check = mlines.Line2D([], [], color='red', marker='*', linestyle='None', markersize=6, label=f'Point to check: ({x_point}, {y_point})')
        
        plt.legend(handles=[shape, midpoint_of_shape, point_to_check])

        ax.set(title="Plot rectangle and point")