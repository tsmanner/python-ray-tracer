class Volume:
    def __init__(self):
        self.shapes = set()

    def hit(self, point):
        for shape in self.shapes:
            if shape.hit(point):
                yield shape
