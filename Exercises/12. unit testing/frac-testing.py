from frac import Frac
import unittest

class TestFrac(unittest.TestCase):
    """ def setUP(self) -> None:
        self.x, self.y = 1, 2
    def create_frac(self) -> "Frac":
        return Frac(self.x, self.y)
    # testing starts here - all tests must start with the word test_
    def test_create_frac(self) -> None:
        self.assertEqual(Frac(self.x, self.y),self.x/self.y)"""
    def test_create_frac(self) -> None:
        self.assertEqual(Frac(1, 2), 1/2)

if __name__ == '__main__':
    unittest.main()


