from functools import reduce


class Point(tuple):
    def __new__(cls, *args):
        if len(args) != 3:
            raise ValueError("Point requires exactly 3 arguments")
        return tuple.__new__(cls, args)

    def __add__(self, other):
        return Point(self[0] + other[0], self[1] + other[1], self[2] + other[2])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Point(self[0] - other[0], self[1] - other[1], self[2] - other[2])

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        return Point(*(other * item for item in self))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __neg__(self):
        return Point(
            -self[0],
            -self[1],
            -self[2]
        )

    def __eq__(self, other):
        if isinstance(other, Point):
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
        return '({:< 4.2f}, {:< 4.2f}, {:< 4.2f})'.format(*self)
