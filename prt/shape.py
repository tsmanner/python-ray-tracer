class Shape:
    def __init__(self):
        pass

    def intersection(self, ray: "Ray"):
        raise NotImplementedError(
            "{} must implement intersection(self, point)!".format(
                self.__class__.__name__
            )
        )
