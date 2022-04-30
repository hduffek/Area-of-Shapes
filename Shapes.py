import math


class Circle:
    """
    Class to calculate the area of a circle, given the radius
    :return: Area of circle
    """
    def __init__(self, radius):   # Initialization method to set variable to class
        self.radius = radius

    def circ_area(self):
        """
        Method to carry out area of circle calculation, while checking for valid inputs
        :return: pi * (radius ** 2)
        """
        if type(self.radius) != int and type(
                self.radius) != float:  # Checks for non-integer and non-float type inputs
            raise TypeError('Not numeric input')

        if self.radius <= 0:  # Checks if radius is less than or equal to zero
            if self.radius == 0:  # Raises ValueError when radius is zero
                raise ValueError('zero input')
            else:  # Raises Value error when radius is negative
                raise ValueError('negative input')

        return math.pi * (self.radius * self.radius)


class Square:
    """
    Class to calculate the area of a square, given the side length
    :return: Area of square
    """
    def __init__(self, side):   # Initialization method to set variable to class
        self.side = side

    def sq_area(self):
        """
        Method to carry out area of square calculation, while checking for valid inputs
        :return: side ** 2
        """
        if type(self.side) != int and type(self.side) != float:   # Checks for non-integer and non-float type inputs
            raise TypeError('Not numeric input')

        if self.side <= 0:   # Checks if side length is less than or equal to zero
            if self.side == 0:   # Raises ValueError when side is zero
                raise ValueError('zero input')
            else:   # Raises ValueError when side is negative
                raise ValueError('negative input')

        return pow(self.side, 2)


class Rectangle:
    """
    Class to calculate the area of a rectangle, given the length and width
    :return: Area of rectangle
    """
    def __init__(self, length, width):   # Initialization method to set variables to class
        self.length = length
        self.width = width

    def rect_area(self):
        """
        Method to carry out area of rectangle calculation, while checking for valid inputs
        :return: length * width
        """
        if (type(self.length) != int and type(self.length) != float) or (
                type(self.width) != int and type(self.width) != float):   # Checks for incorrect input types
            raise TypeError('Not numeric input')

        if (self.length <= 0) or (self.width <= 0):   # Checks for negative values
            if (self.length == 0) or (self.width == 0):   # Raises ValueError for inputs equal to zero
                raise ValueError('zero input')
            else:   # Raises ValueError for negative input values
                raise ValueError('negative input')

        return self.length * self.width


class Triangle:
    """
    Class to calculate the area of a triangle, given the base and height
    :return: Area of triangle
    """
    def __init__(self, base, height):   # Initialization method to set variables to class
        self.base = base
        self.height = height

    def tri_area(self):
        """
        Method to carry out area of triangle calculation, while checking for valid inputs
        :return: (1/2) * base * height
        """
        if (type(self.base) != int and type(self.base) != float) or (
                type(self.height) != int and type(self.height) != float):   # Checks for incorrect variable types
            raise TypeError('Not numeric input')

        if (self.base <= 0) or (self.height <= 0):   # Checks for negative values
            if (self.base == 0) or (self.height == 0):   # Raises ValueError for inputs equal to zero
                raise ValueError('zero input')
            else:   # Raises ValueError for negative inputs
                raise ValueError('negative input')

        return (1 / 2) * self.base * self.height


def main():
    c = Circle(5)
    print(c.circ_area())


if __name__ == '__main__':
    main()
