class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Floor: {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Floor: {self.current_floor}")

    def go_to_floor(self, target):
        if target < self.bottom_floor:
            target = self.bottom_floor
        if target > self.top_floor:
            target = self.top_floor
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, index, target_floor):
        if 0 <= index < len(self.elevators):
            self.elevators[index].go_to_floor(target_floor)
