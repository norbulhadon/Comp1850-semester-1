# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """
    A Point in 2D space.
    """
    def __init__(self, x, y):
        """
        Creates a Point, given x and y coordinates.
        """
        self.x = x
        self.y = y

    def distance(self):
        """
        Calculates the distance from the origin (0,0) to this point.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, point):
        """
        Returns the distance from this point to the specified point.
        """
        return math.hypot(self.x - point.x, self.y - point.y)
    
# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
class Circle:
    """
    A circle with a centre point and radius
    """
    def __init__(self, centre, radius):
        """
        Creates a Circle, given a centre point and radius.
        """
        self.centre = centre
        self.radius = radius

    #  - A method area(), returning the area of the circle
    def area(self):
        """
        Returns the area of the circle.
        """
        return math.pi * self.radius ** 2

    #  - A method perimeter(), returning the perimeter of the circle
    def perimeter(self):
        """
        Returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


# Don't add any testing code to this file!
