# Week 1.5, Session 2: Task 1

# Add type hints to the Point class

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x and y coordinates.
        """

        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordinates must be numeric values.")

        self.x = x
        self.y = y


# Test program

p = Point("two", "one")
print(p.distance())
