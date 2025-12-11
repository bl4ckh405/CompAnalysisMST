import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        # Formatted string representation of coordinates
        return f"({self.x}, {self.y})"

    def __repr__(self):
        # official string representation of points
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        # check if two points are equal
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        # hash function for points in dict
        return hash((self.x, self.y))

    