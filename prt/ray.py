from prt.vector import Vector


class Ray:
    def __init__(self, eye, start_point):
        self.start_point = eye
        self.direction = Vector(start_point - eye).normalize()
