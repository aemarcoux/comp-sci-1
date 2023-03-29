# Author: Alexander Marcoux
# Date: 20 February 2023
# Purpose: Extra Credit "System" class

from math import *
from ecbody import Body

G = 6.67384e-11  # gravitational constant


class System:
    def __init__(self, solar_system):
        self.solar_system = solar_system

    def compute_acceleration(self, n):
        # total ax, ay useful for when more than one body/planet is added
        total_ax = 0  # total acceleration of the system (sum of the acceleration of the bodies)
        total_ay = 0

        for planet in self.solar_system:
            # if the planet is compared to itself, there will be no distance/acc
            if planet == self.solar_system[n]:
                pass

            else:
                # distance between planets in both x and y direction
                dx = planet.x - self.solar_system[n].x
                dy = planet.y - self.solar_system[n].y

                # total distance
                distance = sqrt(dx**2 + dy**2)

                # acceleration due to gravity/planet mass
                a = (G * planet.mass) / (distance**2)

                # acceleration of x and y components
                ax = a * dx / distance
                ay = a * dy / distance

                total_ax = total_ax + ax
                total_ay = total_ay + ay

        return total_ax, total_ay

    def update(self, timestep):
        # using the calculated acceleration to update the position of the planets
        for planet in self.solar_system:
            planet.update_position(timestep)

        for index in range(len(self.solar_system)):
            (total_ax, total_ay) = self.compute_acceleration(index)
            self.solar_system[index].update_velocity(total_ax, total_ay, timestep)

    def draw(self, cx, cy, pixels_per_meter):
        for planet in self.solar_system:
            planet.draw(cx, cy, pixels_per_meter)