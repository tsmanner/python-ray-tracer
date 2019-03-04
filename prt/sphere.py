from prt.shape import Shape
from prt.vector import Vector


class Sphere(Shape):
    def __init__(self, center: "Point", radius: float, color: tuple):
        super().__init__()
        self.center = center
        self.radius = radius
        self.color = color

    def hit(self, point: "Point"):
        # Hit if the distance between the point and the center of
        # the sphere is less than or equal to the radius
        return abs(Vector(*(point - self.center))) <= self.radius

    def normal(self, point: "Point"):
        return Vector(*(point - self.center)).normalize()

    def __str__(self):
        return "Sphere({} {})".format(self.radius, self.center)
