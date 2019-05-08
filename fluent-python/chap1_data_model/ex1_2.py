from math import hypot


class Vector:
    """
    矢量类
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def __abs__(self):
        """hypot(x, y): sqrt(x*x + y*y)"""
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __bool__(self):
        return bool(abs(self))

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
