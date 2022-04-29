import math


class Shapes:
    """
    Class for calculating the area of Circles, Squares, Triangle, and rectangles
    """

    def __init__(self, radius, side, length, width, height, base):
        """
        Initialization of different variables within functions of Shapes
        :param radius: Radius of circle
        :param side: Side of square
        :param length: Length of side for rectangle
        :param width: Width of side for rectangle
        :param height: Height of triangle
        :param base: Base length of triangle
        """
        self.__radius = radius
        self.__side = side
        self.__length = length
        self.__width = width
        self.__height = height
        self.__base = base

    def circle(self):
        """
        Function to calculate the area of a circle, given the radius
        :return: Area of circle
        """
        if type(self.__radius) != int and type(
                self.__radius) != float:  # Checks for non-integer and non-float type inputs
            raise TypeError('Not numeric input')

        if self.__radius <= 0:  # Checks if radius is less than or equal to zero
            if self.__radius == 0:  # Raises ValueError when radius is zero
                raise ValueError('zero input')
            else:  # Raises Value error when radius is negative
                raise ValueError('negative input')

        return math.pi * (self.__radius * self.__radius)

    def square(self):
        """
        Function to calculate the area of a square, given the side length
        :return: Area of square
        """
        if type(self.__side) != int and type(self.__side) != float:   # Checks for non-integer and non-float type inputs
            raise TypeError('Not numeric input')

        if self.__side <= 0:   # Checks if side length is less than or equal to zero
            if self.__side == 0:   # Raises ValueError when side is zero
                raise ValueError('zero input')
            else:   # Raises ValueError when side is negative
                raise ValueError('negative input')

        return pow(self.__side, 2)

    def rectangle(self):
        """
        Function to calculate the area of a rectangle, given the length and width
        :return: Area of rectangle
        """
        if (type(self.__length) != int and type(self.__length) != float) or (
                type(self.__width) != int and type(self.__width) != float):   # Checks for incorrect input types
            raise TypeError('Not numeric input')

        if (self.__length <= 0) or (self.__width <= 0):   # Checks for negative values
            if (self.__length == 0) or (self.__width == 0):   # Raises ValueError for inputs equal to zero
                raise ValueError('zero input')
            else:   # Raises ValueError for negative input values
                raise ValueError('negative input')

        return self.__length * self.__width

    def triangle(self):
        """
        Function to calculate the area of a triangle, given the base and height
        :return: Area of triangle
        """
        if (type(self.__base) != int and type(self.__base) != float) or (
                type(self.__height) != int and type(self.__height) != float):   # Checks for incorrect variable types
            raise TypeError('Not numeric input')

        if (self.__base <= 0) or (self.__height <= 0):   # Checks for negative values
            if (self.__base == 0) or (self.__height == 0):   # Raises ValueError for inputs equal to zero
                raise ValueError('zero input')
            else:   # Raises ValueError for negative inputs
                raise ValueError('negative input')

        return (1 / 2) * self.__base * self.__height
