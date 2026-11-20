# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """
    def __init__(self, x, y):
        """
        Creates a Point, given x and y coordinates.
        self.x = x
        self.y = y

    def distance(self):
        """
        Calculates the distance from the origin to this point.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, point):
        """
        Returns the distance from this point to the specified point.
        """
        return math.hypot(self.x - point.x, self.y - point.y)

 #demonstrating use of point class
p = Point(1.5, 4.2)
q = Point(3.7, 2.6)
print(f"Distance from origin to p: {p.distance()}")
print(f"Distance from p to q: {p.distance_to(q)}")

    # Add constructor here

    # Add distance() method here

    # Add distance_to() method here
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
