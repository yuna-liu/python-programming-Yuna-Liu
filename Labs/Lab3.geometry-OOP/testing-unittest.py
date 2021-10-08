from geometry_shape import Shape
from circle import Circle
from rectangle import Rectangle
from cuboid import Cuboid
from sphere import Sphere
from math import sqrt
from math import pi
import unittest

class TestShape(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1, 2

    def create_shape(self) -> "Shape":
        return Shape(self.x, self.y)

    def test_create_shape(self) -> None:
        shape_1 = self.create_shape()
        self.assertEqual((shape_1.x, shape_1.y),(self.x, self.y))

    def test_create_shape_with_str(self) -> None:
        with self.assertRaises(TypeError):
            Shape("1",1)
        with self.assertRaises(TypeError):
            Shape(1, "1")

    def test_validate_number_with_str(self):
        with self.assertRaises(TypeError):
            Shape.validate_number("two")

    def test_validate_positive_number_with_zero_neg(self):
        list_of_test = [0, -1]
        for test_one in list_of_test:
            with self.assertRaises(ValueError):
                Shape.validate_positive_number(test_one)

    def test_validate_positive_number_with_str(self):       
        with self.assertRaises(TypeError):
            Shape.validate_positive_number ("one")

    def test_hori_ver_dis(self) -> float:
        dis = Shape.hori_ver_dis(self.x, self.y)
        self.assertEqual(dis, abs(2-1))
    
    def test_hori_ver_dis_with_str(self) -> float:
        with self.assertRaises(TypeError):
            Shape.hori_ver_dis("two", 1)

    def test_eu_dis(self) -> float:
        dis = Shape.eu_dis(0,1,0,2)
        self.assertEqual(dis, sqrt(1**2+2**2))

    def test_eu_dis_with_str(self) -> float:
        with self.assertRaises(TypeError):
            Shape.eu_dis("0",1,0,2)

    def test_translate(self):
        shape_1 = self.create_shape()
        shape_1.translate(5,5)
        self.assertEqual((shape_1.x, shape_1.y), (self.x+5,self.y+5))

    def test_translate_with_str(self):
        shape_1 = self.create_shape()
        with self.assertRaises(TypeError):
            shape_1.translate("5", 5)
        with self.assertRaises(TypeError):
            shape_1.translate(5, "5")

class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 0, 0
        self.radius = 1

    def create_circle(self) -> "Circle":
        return Circle(self.x, self.y, self.radius)

    def test_create_circle(self):
        circle_1 = self.create_circle()
        self.assertEqual((circle_1.x, circle_1.y, circle_1.radius),(self.x, self.y, self.radius))

    def test_create_circle_with_str_radius(self):
        with self.assertRaises(TypeError):
           Circle(0,0, "1")

    def test_create_circle_with_negative_and_zero_radius(self):
        for one_test in [-1, 0]:
            with self.assertRaises(ValueError):
                Circle(0,0, one_test)
    
    def test_area(self):
        circle_1 = Circle(0,0,1)
        self.assertEqual(circle_1.area(), pi*(self.radius)**2)
    
    def test_area_with_str(self):
        with self.assertRaises(TypeError):
           Circle.area("0",0, 1)
    
    def test_area_with_zero_and_neg_radius(self):
        with self.assertRaises(TypeError):
           Circle.area(0, 0, -1)
        with self.assertRaises(TypeError):
           Circle.area(0, 0, 0)
        
    def test_perimeter(self):
        circle_1 = Circle(0,0,1)
        self.assertEqual(circle_1.perimeter(), 2*pi*self.radius)

    def test_perimeter_with_str(self):
        with self.assertRaises(TypeError):
           Circle.perimeter("0",0, 1)
    
    def test_perimeter_with_neg_radius(self):
        with self.assertRaises(TypeError):
           Circle.perimeter(0, 0, -1)

    def test_is_inside(self):
        circle_1 = Circle(0,0,1)
        self.assertEqual(circle_1.is_inside(0.5,0.5), True)
        circle_2 = Circle(1,1,1)
        self.assertEqual(circle_2.is_inside(0.1,0.1), False)

    def test_is_inside_with_str(self):
        circle_1 = Circle(0,0,1)
        with self.assertRaises(TypeError):
            circle_1.is_inside("0.5",0.5)
            circle_1.is_inside(0.5,"0.5")

    def test__eq__(self):
        circle_1 = Circle(0,0,1)
        circle_2 = Circle(1,1,1)
        circle_3 = Circle(1,1,2)
        self.assertEqual(circle_1==circle_2, True)
        self.assertEqual(circle_1==circle_3, False)

class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 0, 0
        self.side1, self.side2 = 1,2

    def create_rectangle(self) -> "Rectangle":
        return Rectangle(self.x, self.y, self.side1, self.side2)

    def test_create_rectangle(self):
        rectangle_1 = self.create_rectangle()
        self.assertEqual((rectangle_1.x, rectangle_1.y, rectangle_1.side1, rectangle_1.side2),(self.x, self.y, self.side1, self.side2))

    def test_create_rectangle_with_str_sides(self):
        with self.assertRaises(TypeError):
            Rectangle(0,0, "1", 2)
            Rectangle(0,0, 1, "2")

    def test_create_rectangle_with_negative_and_zero_sides(self):
        for one_test in [-1, 0]:
            with self.assertRaises(ValueError):
                Rectangle(0,0, one_test, 2)
                Rectangle(0,0, 1, one_test)
    
    def test_area(self):
        rectangle_1 = self.create_rectangle()
        self.assertEqual(rectangle_1.area(), self.side1*self.side2)

    def test_area_with_str_sides(self):
        with self.assertRaises(TypeError):
           Rectangle.area(0, 0, "1", 1)
        with self.assertRaises(TypeError):
           Rectangle.area(0, 0, 1, "1")
    
    def test_area_with_zero_neg_sides(self):
        with self.assertRaises(TypeError):
           Rectangle.area(0, 0, 0, 1)
        with self.assertRaises(TypeError):
           Rectangle.area(0, 0, -1, -1)

    def test_perimeter(self):
        rectangle_1 = self.create_rectangle()
        self.assertEqual(rectangle_1.perimeter(), 2*(self.side1+self.side2))
   
    def test_perimeter_with_str_sides(self):
        with self.assertRaises(TypeError):
           Rectangle.perimeter(0, 0, "1", 1)
        with self.assertRaises(TypeError):
           Rectangle.perimeter(0, 0, 1, "1")

    def test_perimeter_with_zero_and_neg_sides(self):
        with self.assertRaises(TypeError):
           Rectangle.perimeter(0, 0, 0, 1)
        with self.assertRaises(TypeError):
           Rectangle.perimeter(0, 0, 1, -1)

    def test_is_inside(self):
        rectangle_1 = Rectangle(0,0,1,2)
        self.assertEqual(rectangle_1.is_inside(0.5,0.5), True)
        rectangle_2 = Rectangle(1,1,1,2)
        self.assertEqual(rectangle_2.is_inside(0.1,0.1), False)
        
    def test_is_inside_with_str_sides(self):
        rectangle_1 = Rectangle(0,0,1,2)
        with self.assertRaises(TypeError):
            rectangle_1.is_inside("0.5",0.5)
            rectangle_1.is_inside(0.5,"0.5")
       
    def test__eq__(self):
        rectangle_1 = Rectangle(0,0,1,2)
        rectangle_2 = Rectangle(1,1,1,2)
        rectangle_3 = Rectangle(0,0,2,1)
        rectangle_4 = Rectangle(0,0,1,1)
        self.assertEqual(rectangle_1==rectangle_2, True)
        self.assertEqual(rectangle_1==rectangle_3, True)
        self.assertEqual(rectangle_1==rectangle_4, False)

class TestSphere(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y, self.z = 0, 0, 0
        self.radius = 1

    def create_sphere(self) -> "Sphere":
        return Sphere(self.x, self.y, self.z, self.radius)

    def test_create_sphere(self):
        sphere_1 = self.create_sphere()
        self.assertEqual((sphere_1.x, sphere_1.y, sphere_1.z, sphere_1.radius),(self.x, self.y, self.z, self.radius))

    def test_create_sphere_with_str(self):
        with self.assertRaises(TypeError):
           Sphere(0,0, 0, "1")
        with self.assertRaises(TypeError):
           Sphere(0,0, "0", 1)

    def test_create_sphere_with_negative_and_zero_radius(self):
        for one_test in [-1, 0]:
            with self.assertRaises(ValueError):
                Sphere(0,0,0, one_test)
    
    def test_area(self):
        sphere_1 = Sphere(0,0,0,1)
        self.assertEqual(sphere_1.area(), 4*pi*self.radius**2)

    def test_area_with_str(self):
        with self.assertRaises(TypeError):
           Sphere.area(0,0, 0, "1")

    def test_area_with_zero_and_neg_radius(self):
        with self.assertRaises(TypeError):
           Sphere.area(0,0, 0, 0)
        with self.assertRaises(TypeError):
           Sphere.area(0,0, 0, -1)

    def test_perimeter(self):
        sphere_1 = Sphere(0,0,0,1)
        self.assertEqual(sphere_1.perimeter(), NotImplemented)

    def test_volume(self):
        sphere_1 = Sphere(0,0,0,1)
        self.assertEqual(sphere_1.volume(), (4/3)*pi*self.radius**3)

    def test_volume_with_str_radius(self):
        with self.assertRaises(TypeError):
           Sphere.volume(0,0, 0, "1")

    def test_volume_with_zero_and_neg_radius(self):
        with self.assertRaises(TypeError):
           Sphere.volume(0,0, 0, 0)
        with self.assertRaises(TypeError):
           Sphere.volume(0,0, 0, -1)

    def test_is_inside(self):
        sphere_1 = Sphere(0,0,0,1)
        self.assertEqual(sphere_1.is_inside(0.5,0.5,0.5), True)
        sphere_2 = Sphere(1,1,1,1)
        self.assertEqual(sphere_2.is_inside(0.1,0.1,0.1), False)
        with self.assertRaises(TypeError):
           sphere_1.is_inside("0.5",0.5,0.5)
           sphere_1.is_inside(0.5,"0.5",0.5)
           sphere_1.is_inside(0.5,0.5,"0.5")

    def test_translate(self):
        sphere_1 = self.create_sphere()
        sphere_1.translate(5,5,5)
        self.assertEqual((sphere_1.x, sphere_1.y, sphere_1.z, sphere_1.radius), (self.x+5,self.y+5,self.z+5,self.radius))
 
    def test_translate_with_str(self):
        sphere_1 = self.create_sphere()
        with self.assertRaises(TypeError):
            sphere_1.translate("5", 5, 5)
            sphere_1.translate(5, "5", 5)
            sphere_1.translate(5, 5, "5")

    def test__eq__(self):
        sphere_1 = Sphere(0,0,0,1)
        sphere_2 = Sphere(1,1,1,1)
        sphere_3 = Sphere(0,0,0,2)
        self.assertEqual(sphere_1==sphere_2, True)
        self.assertEqual(sphere_1==sphere_3, False)

class TestCuboid(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y, self.z = 0, 0, 0
        self.side1, self.side2, self.side3 = 1,2,3

    def create_cuboid(self) -> "Cuboid":
        return Cuboid(self.x, self.y, self.z, self.side1, self.side2, self.side3)

    def test_create_cuboid(self):
        cuboid_1 = self.create_cuboid()
        self.assertEqual((cuboid_1.x, cuboid_1.y, cuboid_1.z, cuboid_1.side1, cuboid_1.side2, cuboid_1.side3),(self.x, self.y, self.z, self.side1, self.side2, self.side3))

    def test_create_cuboid_str_sides(self):
        with self.assertRaises(TypeError):
            Cuboid(0,0, 0, "1", 2, 3)
        with self.assertRaises(TypeError):
            Cuboid(0,0, 0, 1, "2", 3)
        with self.assertRaises(TypeError):
            Cuboid(0,0, 0, 1, 2, "3")

    def test_create_cuboid_with_neg_and_zero_sides(self):
        for one_test in [-1, 0]:
            with self.assertRaises(ValueError):
                Cuboid(0,0,0, one_test, 2, 3)
    
    def test_area(self):
        cuboid_1 = self.create_cuboid()
        self.assertEqual(cuboid_1.area(), 2*(self.side1*self.side2+self.side1*self.side3+self.side2*self.side3))
    
    def test_area_with_str_sides(self):
        with self.assertRaises(TypeError):
            Cuboid.area(0,0, 0, 1, "2", 3)
        with self.assertRaises(TypeError):
            Cuboid.area(0,0, 0, 1, 2, "3")

    def test_area_with_zero_and_neg_sides(self):
        with self.assertRaises(TypeError):
            Cuboid.area(0,0, 0, 1, 0, 3)
        with self.assertRaises(TypeError):
            Cuboid.area(0,0, 0, 1, 2, -3)

    def test_perimeter(self):
        cuboid_1 = self.create_cuboid()
        self.assertEqual(cuboid_1.perimeter(), 4*(self.side1+self.side2+self.side3))
    
    def test_perimeter_with_str_sides(self):
        with self.assertRaises(TypeError):
            Cuboid.perimeter(0,0, 0, 1, "2", 3)
        with self.assertRaises(TypeError):
            Cuboid.perimeter(0,0, 0, 1, 2, "3")

    def test_perimeter_with_zero_and_neg_sides(self):
        with self.assertRaises(TypeError):
            Cuboid.perimeter(0,0, 0, 1, 0, 3)
        with self.assertRaises(TypeError):
            Cuboid.perimeter(0,0, 0, 1, 2, -3)

    def test_volume(self):
        cuboid_1 = self.create_cuboid()
        self.assertEqual(cuboid_1.volume(), self.side1*self.side2*self.side3)

    def test_volume_with_str_sides(self):
        with self.assertRaises(TypeError):
            Cuboid.volume(0,0, 0, 1, "2", 3)
        with self.assertRaises(TypeError):
            Cuboid.volume(0,0, 0, 1, 2, "3")

    def test_volume_with_zero_and_neg_sides(self):
        with self.assertRaises(TypeError):
            Cuboid.volume(0,0, 0, 1, 0, 3)
        with self.assertRaises(TypeError):
            Cuboid.volume(0,0, 0, 1, 2, -3)

    def test_is_inside(self):
        cuboid_1 = self.create_cuboid()
        self.assertEqual(cuboid_1.is_inside(0.5,0.5,0.5), True)
        cuboid_2 = Cuboid(1,1,1,1,2,4)
        self.assertEqual(cuboid_2.is_inside(0.1,0.1,0.1), False)
        
    def test_is_inside_with_str(self):
        with self.assertRaises(TypeError):
            cuboid_1 = self.create_cuboid()
            cuboid_1.is_inside("0.5",0.5,0.5)
            cuboid_1.is_inside(0.5,"0.5",0.5)
            cuboid_1.is_inside(0.5,0.5,"0.5")

    def test_translate(self):
        cuboid_1 = self.create_cuboid()
        cuboid_1.translate(5,5,5)
        self.assertEqual((cuboid_1.x, cuboid_1.y, cuboid_1.z, cuboid_1.side1, cuboid_1.side2, cuboid_1.side3), (self.x+5,self.y+5,self.z+5,self.side1, self.side2, self.side3))
        
    def test_translate_with_str(self):  
        cuboid_1 = self.create_cuboid()
        with self.assertRaises(TypeError):
            cuboid_1.translate("5", 5, 5)
            cuboid_1.translate(5, "5", 5)
            cuboid_1.translate(5, 5, "5")

    def test__eq__(self):
        cuboid_1 = Cuboid(0,0,0,1,2,3)
        cuboid_2 = Cuboid(1,1,1,1,3,3)
        cuboid_3 = Cuboid(0,0,0,2,1,3)
        self.assertEqual(cuboid_1==cuboid_2, False)
        self.assertEqual(cuboid_1==cuboid_3, True)

if __name__ == "__main__":
    unittest.main()