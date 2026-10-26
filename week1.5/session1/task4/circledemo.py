# Week 1.5, Session 1: Task 4
import math
class Circle:
    """
    A Point in 2D space.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self):

        """
        calculates the distance between the two points.
        """
        return math.hypot(self.x, self.y)
    def distance_to(self, point):
        """returns the distance from this point to the specified point.
        """
        return math.hypot(self.x - point.x, self.y - point.y)

    p = Point(1.5, 4.2)
    q = Point(3.7, 2.6)
    print(p.distance_to(q))
# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle
