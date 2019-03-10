from functools import reduce
import math


class Vector(tuple):
    def __new__(cls, *args):
        if len(args) == 1:
            return tuple.__new__(cls, args[0])
        if len(args) != 3:
            raise ValueError("Vector requires exactly 3 arguments")
        return tuple.__new__(cls, args)

    def __abs__(self):
        return math.sqrt(sum(item ** 2 for item in self))

    def __add__(self, other):
        return Vector(self[0] + other[0], self[1] + other[1], self[2] + other[2])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Vector(self[0] - other[0], self[1] - other[1], self[2] - other[2])

    def __rsub__(self, other):
        return self.__sub__(other)


    def __mul__(self, other):
        """
        a1b1 + a2b2 + a3b3 - ...
        """
        if isinstance(other, Vector):
            return self[0] * other[0] + self[1] * other[1] + self[2] * other[2]
        return Vector(*(other * item for item in self))

    def __rmul__(self, other):
        """ Must define rmul so that int * Vector doesn't concatenate it with itself """
        return self.__mul__(other)

    def __truediv__(self, other):
        return Vector(
            (self[0] / other) if other != 0 else 0,
            (self[1] / other) if other != 0 else 0,
            (self[2] / other) if other != 0 else 0
        )
        # return Vector(*(item / other for item in self))

    def __matmul__(self, other):
        """
        Cx = Ay * Bz - Az * By
        Cy = Bx * Az - Ax * Bz
        Cz = Ax * By - Bx * Ay
        """
        return Vector(
            self[1] * other[2] - self[2] * other[1],
            self[2] * other[0] - self[0] * other[2],
            self[0] * other[1] - self[1] * other[0]
        )

    def __neg__(self):
        return Vector(
            -self[0],
            -self[1],
            -self[2]
        )

    def __eq__(self, other):
        if isinstance(other, Vector):
            return reduce(
                lambda a, b: a and b,
                zip(
                    (round(item, 10) for item in self),
                    (round(item, 10) for item in other)
                )
            )
        return False

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'v ({:< 4.2f}, {:< 4.2f}, {:< 4.2f})'.format(*self)

    def normalize(self):
        return self / abs(self)
