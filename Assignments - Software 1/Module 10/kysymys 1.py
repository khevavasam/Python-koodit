class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current_floor = self.bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Floor: {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Floor: {self.current_floor}")

    def go_to_floor(self, target):
        if target < self.bottom:
            target = self.bottom
        if target > self.top:
            target = self.top
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()
