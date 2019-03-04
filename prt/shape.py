class Shape:
    def __init__(self):
        pass

    def hit(self, point: "Point"):
        raise NotImplementedError(
            "{} must implement hit(self, point)!".format(
                self.__class__.__name__
            )
        )
