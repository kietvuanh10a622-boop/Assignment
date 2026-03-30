class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]
        print(f"Building created with {num_elevators} elevators (Floors {bottom}-{top}).")

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\n--- Running Elevator #{elevator_number + 1} to floor {destination_floor} ---")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print(f"Error: Elevator #{elevator_number + 1} does not exist.")


my_building = Building(1, 10, 3)

my_building.run_elevator(0, 5)

my_building.run_elevator(1, 8)

my_building.run_elevator(0, 1)