from geometry_shape import Shape
from math import sqrt
import unittest

class TestShape(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1, 2

    def create_shape(self) -> "Shape":
        return Shape(self.x, self.y)

    def test_create_shape(self) -> None:
        shape_1 = self.create_shape()
        self.assertEqual((shape_1.x, shape_1.y),(self.x, self.y))

    def test_create_invalid_x_shape(self) -> None:
        with self.assertRaises(TypeError):
            Shape("1",1)

    def test_create_invalid_y_shape(self) -> None:
        with self.assertRaises(TypeError):
            Shape(1, "1")

    def test_validate_number(self):
        with self.assertRaises(TypeError):
            Shape.validate_number("two")

    def test_validate_positive_number(self):
        list_of_test = [0, -1]
        for test_one in list_of_test:
            with self.assertRaises(ValueError):
                shape = Shape(test_one)

    def test_validate_str_number(self):       
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




if __name__ == "__main__":
    unittest.main()