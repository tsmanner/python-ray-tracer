from prt.vector import Vector


class Ray:
    def __init__(self, eye, direction):
        self.eye = eye
        self.pixel = direction
        self.start_point = eye
        self.direction = Vector(direction - eye).normalize()
