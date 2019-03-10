from prt.color import Color


class Light:
    def __init__(self, intensity: float, diffuse: Color, specular: Color):
        self.intensity = intensity
        self.diffuse = diffuse
        self.specular = specular


class PhongLight(Light):
    def __init__(self, location: "Point", intensity: float, diffuse: Color, specular: Color):
        super().__init__(intensity, diffuse, specular)
        self.location = location

    def light(self, ray: "Ray", distance: float, normal: "Vector"):
        pass


class BlinnPhongLight(Light):
    def __init__(self, direction: "Vector", intensity: float, diffuse: Color, specular: Color):
        super().__init__(intensity, diffuse, specular)
        self.direction = direction.normalize()  # Just to be sure it's a unit vector

    def light(self, ray: "Ray", distance: float, normal: "Vector", shape: "Shape"):
        # Lambertian Diffuse
        diffuse = self.diffuse * self.intensity * max(0, normal * self.direction)
        # Blinn-Phong Specular
        halfway = (self.direction + ray.direction).normalize()
        specular = shape.specular * self.intensity * (max(0, normal * halfway) ** shape.shininess)

        color = (diffuse  * self.diffuse)  * (diffuse  * shape.color) +\
                (specular * self.specular) * (specular * shape.color)
        return color
