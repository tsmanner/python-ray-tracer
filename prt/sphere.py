import math

from prt.point import Point
from prt.shape import Shape
from prt.vector import Vector


class Sphere(Shape):
    def __init__(self, center: "Point", radius: float, color: tuple, *args):
        super().__init__(color, *args)
        self.center = center
        self.radius = radius

    def intersection(self, ray: "Ray"):
        """
        Line - Sphere Intersection
        Line:
            x points on line
            o origin of line
            d distance along line
            l line unit vector
            x = o + d*l
        Sphere:
            x points on surface of sphere
            c center point
            r radius
            ||x - c||^2 = r^2
        Intersection:
            Any point, x, that satisfies both equations.
            Solve for d
            ||(o + d*l) - c||^2 = r^2
        """

        o = Vector(ray.start_point)
        l = ray.direction
        c = Vector(self.center)
        r = self.radius

        omc = o - c
        discriminant = (l * (omc))**2 - (((omc)*(omc)) - r**2)

        if discriminant >= 0:
            dp = ( -(l * (omc)) + math.sqrt( discriminant ) )
            dm = ( -(l * (omc)) - math.sqrt( discriminant ) )
            d = dp if dm < 0 else dm
            # d = min(dp, dm)
            """ Intersection point is direction times distance plus origin """
            point = Point(o + d * l)
            # print("Intersection at {}".format(point))
            if round(abs(Vector(point - self.center)), 10) != round(self.radius, 10):
                print("Point Not On Surface! {} != {}".format(abs(Vector(point - self.center)), self.radius))
            return d, self.normal(point)

    def normal(self, point: "Point"):
        return (Vector(point) - self.center).normalize()

    def __str__(self):
        return "Sphere({} {})".format(self.radius, self.center)
