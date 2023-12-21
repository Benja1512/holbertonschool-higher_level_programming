#!/usr/bin/python3
"""class main inherited"""

Rectangle = __import('9-rectangle.py').Rectangle

class Square(Rectangle):
    """class implemented"""

def __init__(self, size):
    """"method implemented"""    
    self.integer_validator('size', size)
    self.__size = size
    super().__init__(self.__size, self.__size)
