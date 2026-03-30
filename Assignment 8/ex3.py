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

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\n--- Running Elevator #{elevator_number + 1} to floor {destination_floor} ---")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print(f"Error: Elevator #{elevator_number + 1} does not exist.")

    def fire_alarm(self):
        print("\n!!! FIRE ALARM ACTIVATED !!!")
        print("Returning all elevators to the bottom floor...")
        for i, elevator in enumerate(self.elevators):
            print(f"Evacuating Elevator #{i + 1}:")
            elevator.go_to_floor(self.bottom)
        print("All elevators are now safely at the bottom floor.")


my_building = Building(1, 10, 3)

my_building.run_elevator(0, 7)  
my_building.run_elevator(1, 4)  
my_building.run_elevator(2, 9)  

my_building.fire_alarm()