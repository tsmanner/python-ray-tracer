import PIL.Image
import statistics

from prt.ray import Ray
from prt.point import Point
from prt.sphere import Sphere
from prt.vector import Vector
from prt.volume import Volume


def test_main(top, bottom, left, right, near, resolution_factor):
    x_pixels = 16 * resolution_factor
    y_pixels = 9 * resolution_factor

    pixel_width = (right - left) / x_pixels
    pixel_height = (bottom - top) / y_pixels

    print(pixel_width, pixel_height)

    eye = Point(
        (right - left) / 2 + left,
        (bottom - top) / 2 + top,
        0
    )

    volume = Volume()
    volume.shapes.add(
        Sphere(
            Point(0, 0, -3),  # Center
            1,                # Radius
            (0, 127, 0)       # Color
        )
    )
    volume.shapes.add(
        Sphere(
            Point(2, 0, -2),  # Center
            .5,               # Radius
            (127, 0, 0)       # Color
        )
    )
    volume.shapes.add(
        Sphere(
            Point(1, 1, -2),  # Center
            1,               # Radius
            (0, 0, 127)       # Color
        )
    )

    u = Vector(1, 0, 0)
    v = Vector(0, -1, 0)
    w = Vector(0, 0, -1)
    print("eye", eye)
    print("u", u)
    print("v", v)
    print("w", w)

    basex = 1
    basey = 0
    basez = near

    rays = [
        Ray(eye, Point(basex, basey, near)),
    ]
    for i in range(1, 3):
        x = basex + pixel_width * i
        y = basey + pixel_width * i
        z = basez

        rays += [
            Ray(eye, Point(-x,  0, z)),
            Ray(eye, Point(+x,  0, z)),
            Ray(eye, Point( 1, -y, z)),
            Ray(eye, Point( 1, +y, z)),
        ]

    for i, ray in enumerate(rays):
        for shape in volume.shapes:
            intersection = shape.intersection(ray)
            if intersection and intersection[0] >= 0:
                print(
                    "{}:  H  {} {} {:<.3f} {} {}".format(
                        i, ray.start_point, ray.direction, round(intersection[0], 2), intersection[1], shape.center
                    )
                )
            else:
                print(
                    "{}:     {} {}".format(
                        i, ray.start_point, ray.direction
                    )
                )


def main(top, bottom, left, right, near, resolution_factor):
    x_pixels = 16 * resolution_factor
    y_pixels = 9 * resolution_factor

    pixel_width = (right - left) / x_pixels
    pixel_height = (bottom - top) / y_pixels

    eye = Point(
        (right - left) / 2 + left,
        (bottom - top) / 2 + top,
        0
    )

    volume = Volume()
    volume.shapes.add(
        Sphere(
            Point(0, 0, -3),  # Center
            1,                # Radius
            (0, 127, 0)       # Color
        )
    )
    volume.shapes.add(
        Sphere(
            Point(2, 0, -2),  # Center
            .5,               # Radius
            (127, 0, 0)       # Color
        )
    )
    volume.shapes.add(
        Sphere(
            Point(1, 1, -2),  # Center
            1,               # Radius
            (0, 0, 127)       # Color
        )
    )

    u = Vector(1, 0, 0)
    v = Vector(0, -1, 0)
    w = Vector(0, 0, -1)

    # Single light source, straight above the scene (from the light source is straight down)
    light = Vector(0, 1, 0)

    background_color = (0, 0, 0)

    image = PIL.Image.new("RGB", (x_pixels, y_pixels))
    pixelmap = image.load()

    for y in range(y_pixels):
        for x in range(x_pixels):
            pixelmap[x, y] = background_color
            start_point = Point(
                (x + 0.5) * pixel_width + left,
                (y + 0.5) * pixel_height + top,
                near
            )
            ray = Ray(eye, start_point)
            last_distance = None
            for shape in volume.shapes:
                intersection = shape.intersection(ray)
                if intersection and intersection[0] > 0 and (last_distance is None or intersection[0] < last_distance):
                    distance, normal = intersection
                    last_distance = distance
                    # Reflect the direction with respect to the normal
                    # r = d - 2*(n*d)n
                    reflected = ray.direction - 2 * (normal * ray.direction) * normal
                    # print("HIT", start_point, round(intersection[0], 3), intersection[1])
                    pixelmap[x, y] = shape.color
                    # print(start_point, shape.intersection(ray, discriminant), round(shape.hit(ray), 2))

    image.save("rawr.png", "PNG")


if __name__ == "__main__":
    # scale = 75 for 1280x720
    mx, my = 1, 1.778
    scale = 75
    # test_main(-mx, mx, -my, my, -1, scale)
    main(-mx, mx, -my, my, -1, scale)
