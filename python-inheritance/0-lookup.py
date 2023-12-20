#!/usr/bin/python3
def lookup(obj):
    """Lookup all atributes in Class
    Args:
        obj: object class
    Returns:
        Na
    """
    return [i for i in dir(obj)]
