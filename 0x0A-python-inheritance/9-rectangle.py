#!/usr/bin/python3
""" This module defines a class Rectangle """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Instantiation with width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Return description of the rectangle """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """ Return area of the rectangle """
        return self.__width * self.__height