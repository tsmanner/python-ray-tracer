from prt.vector import Vector


class Ray:
    def __init__(self, eye, start_point):
        self.eye = eye
        self.start_point = start_point
        self.direction = Vector(*(self.start_point - self.eye)).normalize()

    def trace(self, volume, step, max_distance):
        increment = self.direction * step
        current = self.start_point
        for i in range(int(max_distance / step)):
            # print(self.start_point, current, Vector(*current).normalize())

            for shape in volume.hit(current):
                yield current, shape
            current += increment

            # current = self.eye + i * (self.start_point - self.eye)
            # for shape in volume.hit(current):
            #     yield current, shape
            # current += increment
