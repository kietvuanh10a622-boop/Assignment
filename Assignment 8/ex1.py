class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current_floor = bottom_floor
        print(f"Elevator initialized. Range: {self.bottom}-{self.top}. Starting at floor {self.current_floor}.")

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")
        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")
        else:
            print("Already at the bottom floor.")

    def go_to_floor(self, target_floor):
        if target_floor > self.top or target_floor < self.bottom:
            print(f"Error: Floor {target_floor} is out of reach.")
            return

        print(f"--- Moving to floor {target_floor} ---")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {self.current_floor}")

h = Elevator(1, 10)

h.go_to_floor(5)

h.go_to_floor(1)