import math

from array import array


class Vector2d:
    typecode = 'd'
    # __slots__ = ('__x', '__y')

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __str__(self):  # 打印结果
        return str(tuple(self))

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.x}, {self.y})'

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __bool__(self):
        if self.x or self.y:
            return True
        return False

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        raise AttributeError('can not set attribute')

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


v1 = Vector2d(3, 4)
print(v1.x, v1.y)
print(v1)
