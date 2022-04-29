import unittest
from Shapes import *


class MyTestCase(unittest.TestCase):

    def test_Circle(self):
        c = Circle(5)
        self.assertEqual(c.circ_area(), (math.pi * 25))
        c = Circle(0.1)
        self.assertAlmostEqual(c.circ_area(), 0.01, delta=0.1)

        with self.assertRaises(TypeError):
            c = Circle('0.1')
            c.circ_area()

        with self.assertRaises(ValueError):
            c = Circle(-1)
            c.circ_area()
            c = Circle(0)
            c.circ_area()

    def test_square(self):
        s = Square(10)
        self.assertEqual(s.sq_area(), 100)
        s = Square(0.1)
        self.assertAlmostEqual(s.sq_area(), 0.01, delta=0.1)

        with self.assertRaises(TypeError):
            s = Square('0.1')
            s.sq_area()

        with self.assertRaises(ValueError):
            s = Square(-1)
            s.sq_area()
            s = Square(0)
            s.sq_area()

    def test_rectangle(self):
        r = Rectangle(5, 2)
        self.assertEqual(r.rect_area(), 10)
        r = Rectangle(2.5, 1)
        self.assertAlmostEqual(r.rect_area(), 2.5, delta=0.1)
        r = Rectangle(1, 2.5)
        self.assertAlmostEqual(r.rect_area(), 2.5, delta=0.1)
        r = Rectangle(2.5, 3.5)
        self.assertAlmostEqual(r.rect_area(), 8.75, delta=0.1)

        with self.assertRaises(TypeError):
            r = Rectangle('0.1', 2)
            r.rect_area()('0.1', 2)
            r = Rectangle(6, '2')
            r.rect_area()(6, '2')
            r = Rectangle('3', '5')
            r.rect_area()('3', '5')

        with self.assertRaises(ValueError):
            r = Rectangle(-1, 3)
            r.rect_area()
            r = Rectangle(2, -5)
            r.rect_area()
            r = Rectangle(-1, -2)
            r.rect_area()
            r = Rectangle(0, 1)
            r.rect_area()
            r = Rectangle(6, 0)
            r.rect_area()
            r = Rectangle(0, 0)
            r.rect_area()

    def test_triangle(self):
        t = Triangle(4, 3)
        self.assertEqual(t.tri_area(), 6)
        t = Triangle(1.5, 1)
        self.assertAlmostEqual(t.tri_area(), 0.75, delta=0.1)
        t = Triangle(1, 1.5)
        self.assertAlmostEqual(t.tri_area(), 0.75, delta=0.1)
        t = Triangle(1.5, 3.4)
        self.assertAlmostEqual(t.tri_area(), 2.55, delta=0.1)

        with self.assertRaises(TypeError):
            t = Triangle('0.1', 2)
            t.tri_area()
            t = Triangle(6, '2')
            t.tri_area()
            t = Triangle('3', '5')
            t.tri_area()

        with self.assertRaises(ValueError):
            t = Triangle(-1, 3)
            t.tri_area()
            t = Triangle(2, -5)
            t.tri_area()
            t = Triangle(-1, -2)
            t.tri_area()
            t = Triangle(0, 1)
            t.tri_area()
            t = Triangle(6, 0)
            t.tri_area()
            t = Triangle(0, 0)
            t.tri_area()


if __name__ == '__main__':
    unittest.main()
