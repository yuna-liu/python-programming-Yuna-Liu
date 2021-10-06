from geometry_shape import Shape
from circle import Circle
from rectangle import Rectangle
from cube import Cube
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

    def test_create_str_shape(self) -> None:
        with self.assertRaises(TypeError):
            Shape("1",1)
        with self.assertRaises(TypeError):
            Shape(1, "1")

    def test_validate_str_number(self):
        with self.assertRaises(TypeError):
            Shape.validate_number("two")

    def test_validate_positive_number(self):
        list_of_test = [0, -1]
        for test_one in list_of_test:
            with self.assertRaises(ValueError):
                Shape.validate_positive_number(test_one)

    def test_validate_positive_number_str(self):       
        with self.assertRaises(TypeError):
            Shape.validate_positive_number ("one")

    def test_hori_ver_dis(self) -> float:
        dis = Shape.hori_ver_dis(self.x, self.y)
        self.assertEqual(dis, abs(2-1))

    def test_eu_dis(self) -> float:
        dis = Shape.eu_dis(0,1,0,2)
        self.assertEqual(dis, sqrt(1**2+2**2))

    def test_translate(self):
        shape_1 = self.create_shape()
        shape_1.translate(5,5)
        self.assertEqual((shape_1.x, shape_1.y), (1+5,2+5))
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

    def test_create_circle_str_radius(self):
        with self.assertRaises(TypeError):
           Circle(0,0, "1")

    def test_create_circle_negative_and_zero_radius(self):
        for one_test in [-1, 0]:
            with self.assertRaises(ValueError):
                Circle(0,0, one_test)
    
    def test_area(self):
        circle_1 = Circle(0,0,1)
        self.assertEqual(circle_1.area(), pi*(self.radius)**2)

    def test_perimeter(self):
        circle_1 = Circle(0,0,1)
        self.assertEqual(circle_1.perimeter(), 2*pi*self.radius)

    def test_is_inside(self):
        circle_1 = Circle(0,0,1)
        self.assertEqual(circle_1.is_inside(0.5,0.5), True)
        circle_2 = Circle(1,1,1)
        self.assertEqual(circle_2.is_inside(0.1,0.1), False)

    def test__eq__(self):
        circle_1 = Circle(0,0,1)
        circle_2 = Circle(1,1,1)
        self.assertEqual(circle_1==circle_2, True)

if __name__ == "__main__":
    unittest.main()