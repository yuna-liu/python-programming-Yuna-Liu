from geometry_shape import Shape
from circle import Circle
import unittest

class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1, 2
        self.radius= 1

    def create_circle(self) -> "Circle":
        return Circle(self.x, self.y, self.radius)

    def test_create_circle(self) -> None:
        circle1 = self.create_circle()
        self.assertEqual((circle1.x, circle1.y, circle1.radius), (self.x,self.y,self.radius))

if __name__ == "__main__":
    unittest.main()
