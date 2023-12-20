#!/usr/bin/python3
""" function if object is an instance of a class"""


def inherits_from(obj, a_class):
    """a methos that an obj is an instance of a class inherited diretly of inderectlu
    Args:
        obj(any): to check.
        a_class: to match the type of obj to.
    Returns:  
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
