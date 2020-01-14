# Enter you module contents here
"""Triangle module """
__version__ = """V1.0"""
__author__ = """author: bikash jaiswal"""

import math


def hypothenuse(a, b):
    """  returns the length of the hypothenuse 
    when given the lengths of two other sides of a right-angled triangle"""
    return float(math.sqrt(a ** 2 + b ** 2))


def area(a, b):
    """ return area of right-angled triangle when two sides, 
    perpendicular to each other, are given as parameters."""
    return (a*b)/2
