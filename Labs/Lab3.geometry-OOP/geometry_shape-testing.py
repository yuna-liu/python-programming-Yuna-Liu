from geometry_shape import Shape
from math import sqrt
import unittest

class TestShape(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1, 2
        self.type = "circle"

    def create_shape(self) -> "Shape":
        return Shape(self.x, self.y, self.type)

    def test_create_shape(self) -> None:
        shape_1 = self.create_shape()
        self.assertEqual((shape_1.x, shape_1.y, shape_1.type),(self.x, self.y, self.type))

    def test_create_invalid_x_shape(self) -> None:
        with self.assertRaises(TypeError):
            Shape("1",1, "circle")

    def test_create_invalid_y_shape(self) -> None:
        with self.assertRaises(TypeError):
            Shape(1, "1", "circle")

    def test_validate_number(self):
        with self.assertRaises(TypeError):
            Shape.validate_number("two")

    def test_validate_positive_number(self):
        with self.assertRaises(ValueError):
            Shape.validate_positive_number (0)
        with self.assertRaises(TypeError):
            Shape.validate_positive_number ("one")

    def test_validate_str(self):
        with self.assertRaises(TypeError):
            Shape.validate_str(1)


    def test_hori_ver_dis(self) -> float:
        dis = Shape.hori_ver_dis(self.x, self.y)
        self.assertEqual(dis, abs(2-1))

    def test_eu_dis(self) -> float:
        dis = Shape.eu_dis(0,1,0,2)
        self.assertEqual(dis, sqrt(1**2+2**2))

    def test_create_invalid_type_shape(self) -> None:
        with self.assertRaises(TypeError):
            Shape(1, 1, 1.945)

    def test_translate(self):
        shape_1 = self.create_shape()
        shape_1.translate(5,5)
        self.assertEqual((shape_1.x, shape_1.y), (1+5,2+5))


if __name__ == "__main__":
    unittest.main()