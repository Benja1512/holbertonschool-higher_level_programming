#!/usr/bin/python3
"""function to know if an object is an instance"""

def is_kind_of_class(obj, a_class):
    """a function 
    
    Arg:
        obj(any): to check if an object is an instance
        a_class: the class match te type og obj
   Return:
        true is an object is an instance or false if obj is not
    """
    if isinstance(obj, a_class):
        return True
    return False
