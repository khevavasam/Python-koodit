import random

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0.0

    def accelerate(self, delta_speed):
        self.current_speed = max(0, min(self.maximum_speed, self.current_speed + delta_speed))

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance  # km
        self.cars = cars

    def hour_passes(self):
        for c in self.cars:
            c.accelerate(random.randint(-10, 15))
            c.drive(1)

    def print_status(self):
        print(f"{'Plate':<8} {'Max':>6} {'Speed':>7} {'Distance':>10}")
        print("-" * 33)
        for c in self.cars:
            print(f"{c.license_plate:<8} {c.maximum_speed:>6} {c.current_speed:>7} {c.travelled_distance:>10.1f}")

    def race_finished(self):
        return any(c.travelled_distance >= self.distance for c in self.cars)
