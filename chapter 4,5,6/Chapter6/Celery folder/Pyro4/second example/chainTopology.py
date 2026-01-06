import math
import Pyro4


def mensuration_calculations():
    """Calculate various 2D and 3D shapes measurements"""

    # Define dimensions
    r = 7.5
    l, b, h = 12, 8, 5
    a = 6

    # 2D Shapes
    area_circle = math.pi * r ** 2
    peri_circle = 2 * math.pi * r

    area_rect = l * b
    peri_rect = 2 * (l + b)

    area_square = a ** 2
    peri_square = 4 * a

    area_triangle = 0.5 * b * h

    # 3D Shapes
    sa_cube = 6 * a ** 2
    vol_cube = a ** 3

    sa_cuboid = 2 * (l*b + b*h + h*l)
    vol_cuboid = l * b * h

    sa_cylinder = 2 * math.pi * r * (r + h)
    vol_cylinder = math.pi * r ** 2 * h

    # Total
    total = (
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )

    return total


@Pyro4.expose
class Chain(object):
    def __init__(self, name, current_server):
        self.name = name
        self.current_serverName = current_server
        self.current_server = None

    def process(self, message):
        if self.current_server is None:
            self.current_server = Pyro4.core.Proxy(
                "PYRONAME:example.chainTopology." + self.current_serverName
            )

        if self.name in message:
            print("Back at %s; the chain is closed!" % self.name)

            # 🔹 Mensuration calculation added here
            mensuration_result = mensuration_calculations()

            return [
                "complete at " + self.name,
                f"mensuration total = {mensuration_result:.2f}"
            ]

        else:
            print("%s forwarding the message to the object %s" %
                  (self.name, self.current_serverName))

            message.append(self.name)
            result = self.current_server.process(message)
            result.insert(0, "passed on from " + self.name)
            return result
