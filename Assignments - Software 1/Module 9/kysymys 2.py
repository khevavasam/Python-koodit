class Car:
    def __init__(self, license_plate: str, maximum_speed: int):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, delta_speed: int):
        self.current_speed = max(0, min(self.maximum_speed, self.current_speed + delta_speed))
