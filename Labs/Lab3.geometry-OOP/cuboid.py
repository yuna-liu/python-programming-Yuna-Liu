from geometry_shape import Shape
from rectangle import Rectangle
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
import matplotlib.lines as mlines

class Cuboid(Rectangle):
    def __init__(self, x: float, y: float, z:float, side1: float, side2:float, side3:float) -> None:
        """A subclass of rectangle to represent cuboid with (x, y, z) of the midpoint, and sides(length, width, height)"""
        """side1 is the length on the horizontal line of the xy coordinate."""
        """side2 is the length on the vertical line of the xy coordinate."""
        """side3 is the height of cuboid."""
        super().__init__(x,y,side1,side2)
        self.z = z
        self.side3 = side3

    @property
    def z(self) -> float:
        """Read-only property, can't set the z"""
        return self._z
    
    @z.setter
    def z(self, value: float) -> None:
        """Setter for z with error handling"""
        self._z = Shape.validate_number(value)
    
    @property
    def side3(self) -> float:
        """Read-only property, can't set the side3"""
        return self._side3
    
    @side3.setter
    def side3(self, value: float) -> None:
        """Setter for side with error handling"""
        self._side3 = Shape.validate_positive_number(value)
    
    def area(self) -> float:
        """Return the surface area of cuboid"""
        return 2*(self.side1*self.side2+self.side1*self.side3+self.side2*self.side3)
    
    def perimeter(self) -> float:
        """Return the perimeter of cuboid"""
        return 4*(self.side1+self.side2+self.side3)
    
    def volume(self) -> float:
        """Return the volume of cuboid"""
        return self.side1*self.side2*self.side3

    def is_inside(self,x_point:float, y_point:float, z_point:float) -> bool:
        """Return whether a point is in a cuboid"""
        #|x_point-self.x|<= 0.5*self.side --> self.x - 0.5*self.side <= x_point <= self.x + 0.5*self.side
        #|y_point-self.y|<= 0.5*self.side --> self.y - 0.5*self.side <= y_point <= self.y + 0.5*self.side
        #|z_point-self.z|<= 0.5*self.side --> self.z - 0.5*self.side <= z_point <= self.z + 0.5*self.side
        return Shape.hori_ver_dis(self.x, x_point) <= 0.5*self.side1 and Shape.hori_ver_dis(self.y, y_point) <= 0.5*self.side2 and Shape.hori_ver_dis(self.z, z_point) <= 0.5*self.side3

    def translate(self, x_move:float, y_move:float,z_move:float) -> None:
        """A method to move x by x_move, move y by y_move, and move z by z_move"""
        super().translate(x_move, y_move)
        self._z = self.z + Shape.validate_number(z_move) 

    def __eq__(self, other) -> bool:
        """Return if two cuboid are equal. The conditions are they should be the same type, volume, area and perimeter"""
        return type(self) == type(self) and self.volume()==other.volume() and self.area()==other.area() and self.perimeter()==other.perimeter()
 
    def plot_cuboid(self,x_point=None, y_point=None, z_point=None) -> None:
        """Draw cuboid and a point"""
        # Reference: https://stackoverflow.com/questions/30715083/python-plotting-a-wireframe-3d-cuboid

        fig = plt.figure(dpi=100,figsize=(10,4))
        ax = plt.subplot(projection='3d')
        #ax.set_aspect("equal")
        # NotImplementedError: Axes3D currently only supports the aspect argument 'auto'. You passed in 'equal'

        # draw cuboid
        r1 = [-0.5*self.side1, 0.5*self.side1]
        r2 = [-0.5*self.side2, 0.5*self.side2]
        r3 = [-0.5*self.side3, 0.5*self.side3]
        center =[self.x,self.y,self.z]

        for s, e in combinations(np.array(list(product(r1,r2,r3))), 2):
            s=np.array(center)+np.array(s)
            e=np.array(center)+np.array(e)
            #ax.scatter3D(*center, color="b") draw centerpoint with color blue and shape *.
            if np.linalg.norm(s-e) == 2*r1[1] or np.linalg.norm(s-e) == 2*r2[1] or np.linalg.norm(s-e) == 2*r3[1]:
                zip(s,e)
                ax.plot3D(*zip(s,e), color="b")  
        
        # draw midpoint and grid
        ax.plot(self.x, self.y, self.y,'s', color ="b")
        ax.grid()

        # draw any point to check
        if x_point !=None and y_point !=None and z_point !=None:
            ax.plot(x_point,y_point,z_point, color='red', marker='*')

        # create legend
        shape = mlines.Line2D([], [], color='blue', marker='s', linestyle='None', markerfacecolor="white", markersize=6, label=f'Cuboid: (width: {self.side1}, length: {self.side2}, height: {self.side3})')
        midpoint_of_shape= mlines.Line2D([], [], color='blue', marker='s', linestyle='None', markersize=4, label=f'Midpoint of cuboid: ({self.x}, {self.y}, {self.z})')
        point_to_check = mlines.Line2D([], [], color='red', marker='*', linestyle='None', markersize=4, label=f'Point to check: ({x_point}, {y_point}, {z_point})')
        
        plt.legend(handles=[shape, midpoint_of_shape, point_to_check], loc="upper right", framealpha= 0.2, fontsize='x-small')

        # create title and plot show
        ax.set(title="Plot cuboid and point")
        plt.show()

    def __repr__(self) -> str:
        """Present the instance"""
        return f"cuboid with center point: ({self.x}, {self.y}, {self.z}) with side3: ({self.side1}, {self.side2}, {self.side3})."   

