import PIL.Image
import statistics

from prt.ray import Ray
from prt.point import Point
from prt.sphere import Sphere
from prt.volume import Volume


if __name__ == "__main__":
    # resolution_factor = 75  # 1280 x 720
    step = 0.5
    resolution_factor = 20
    pixel_width = 16 * resolution_factor
    pixel_height = 9 * resolution_factor

    image = PIL.Image.new("RGB", (pixel_width, pixel_height))
    pixelmap = image.load()

    top = -4.5
    bottom = 4.5
    left = -8
    right = 8
    front = 1
    back = 10

    x_increment = (right - left) / pixel_width
    y_increment = (top - bottom) / pixel_height

    eye = Point(0, 0, 0)

    volume = Volume()
    volume.shapes.add(
        Sphere(
            Point(3, 0, 5),
            3,
            (0, 127, 0)
        )
    )
    volume.shapes.add(
        Sphere(
            Point(0, 3, 2),
            2,
            (0, 0, 127)
        )
    )

    # pixel_ray = lambda sp: Ray(sp - (0, 0, front), sp)  # Orthographic
    pixel_ray = lambda sp: Ray(eye, sp)                 # Perspective

    for y in range(pixel_height):
        for x in range(pixel_width):
            hit = False
            start_point = Point(
                x * x_increment + left,
                y * y_increment - top,
                front
            )
            ray = pixel_ray(start_point)
            for point, shape in ray.trace(volume, step, back):
                pixelmap[x, y] = shape.color
                # print(" ", shape)
                hit = True
                break
            if not hit:
                pixelmap[x, y] = (0, 0, 0)
                # pixelmap[x, y] = (x, y, x ^ y)

    image.save("rawr.png", "PNG")
