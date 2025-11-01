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
