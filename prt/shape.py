class Shape:
    def __init__(self, color: "Color", ambient_coef=None, diffuse_coef=None, specular_coef=None, shininess=None):
        self.color = color
        self.ambient = ambient_coef
        self.diffuse = diffuse_coef
        self.specular = specular_coef
        self.shininess = shininess

    def intersection(self, ray: "Ray"):
        raise NotImplementedError(
            "{} must implement intersection(self, point)!".format(
                self.__class__.__name__
            )
        )
