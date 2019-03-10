import collections
import statistics


class Color:
    def __init__(self, r, g, b):
        self.red = int(r)
        self.green = int(g)
        self.blue = int(b)
        self._normalize()

    def __add__(self, other: "Color"):
        return Color(
            self.red + other.red,
            self.green + other.green,
            self.blue + other.blue,
        )

    def __radd__(self, other: "Color"):
        return self + other

    def __mul__(self, other: "Color"):
        if isinstance(other, Color):
            return Color(
                statistics.mean((self.red, other.red)),
                statistics.mean((self.green, other.green)),
                statistics.mean((self.blue, other.blue)),
            )
        return Color(
            other * self.red,
            other * self.green,
            other * self.blue,
        )

    def __rmul__(self, other: "Color"):
        return self * other

    def __str__(self):
        return "Color{}".format(self.to_tuple())

    def to_tuple(self):
        return (
            self.red,
            self.green,
            self.blue,
        )

    def _normalize(self):
        max_color = max(self.red, self.green, self.blue)
        c = 255 / max_color if max_color > 0 else 1
        if c <= 1:
            self.red = int(c * self.red)
            self.green = int(c * self.green)
            self.blue = int(c * self.blue)
