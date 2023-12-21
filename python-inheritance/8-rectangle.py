#!/usr/bin/python3
""" an inheritance rectangle class """

def __init__(self, width, height):
    """ declare the private variable"""

    self.__width = int
    self.__height = int
    """
        Positive Integer
    Args:
        width(int): validate positive integer
        height(int): valitdate positive integer
    """ 
    if type(value) != int:
        raise TypeError("{}" must be an integerr.format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
