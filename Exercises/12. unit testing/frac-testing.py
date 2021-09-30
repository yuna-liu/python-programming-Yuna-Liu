from frac import Frac
import unittest

class TestFrac(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1, 2
    def create_frac(self) -> "Frac":
        return Frac(self.x, self.y)

    def test_create_frac(self) -> None:
        f_1 = self.create_frac()
        self.assertEqual((f_1.nominator, f_1.denominator),(self.x, self.y))

    def test_negative_nominator(self):
        with self.assertRaises(ValueError):
            f = Frac(-1,6)

    def test_negative_denominator(self):
        with self.assertRaises(ValueError):
            f = Frac(1,-6)

    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            f = Frac(1,0)

    def test_str_nominator(self):
        with self.assertRaises(TypeError):
            f = Frac("20",100)    
    
    def test_str_nominator(self):
        with self.assertRaises(TypeError):
            f = Frac(20,"100")

# test __eq__ for two fractions that are equal.
    def test_2_fracs_equal(self):
        f_1 = self.create_frac()
        f_2 = Frac(1, 2)
        self.assertEqual(f_1, f_2)
    
    def test_2_fracs_not_equal(self):
        f_1 = self.create_frac()
        f_2 = Frac(1, 3)
        self.assertNotEqual(f_1, f_2)
    
    # test simplify(), which based on __eq__ is tested.
    def test_2_fracs_equal(self):
        f_2 = self.create_frac()
        f_1 = Frac(2, 4)
        self.assertEqual(f_1, f_2)
        
    def test_simplify(self):
        f_1 = self.create_frac()
        f_2 = Frac(4,8)
        self.assertEqual(f_1, f_2.simplify())

    def test_add(self):
        f_1 = self.create_frac()
        f_2 = Frac(1,3)
        self.assertEqual(f_1+f_2, Frac(5,6))

    def test_sub(self):
        f_1 = self.create_frac()
        f_2 = Frac(1,3)
        self.assertEqual(f_1-f_2, Frac(1,6))

    def test_truediv(self):
        f_1 = self.create_frac()
        f_2 = Frac(1,4)
        self.assertEqual(f_1/f_2, Frac(2,1))

    def test_mul(self):
        f_1 = self.create_frac()
        f_2 = Frac(1,4)
        self.assertEqual(f_1*f_2, Frac(1,8))








if __name__ == '__main__':
    unittest.main()


