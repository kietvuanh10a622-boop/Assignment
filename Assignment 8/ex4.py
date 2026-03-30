import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, change_in_speed):
        self.current_speed = max(0, min(self.max_speed, self.current_speed + change_in_speed))

    def drive(self, hours):
        self.distance_traveled += self.current_speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            acceleration = random.randint(-10, 15)
            car.accelerate(acceleration)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name} | Distance: {self.distance} km")
        print(f"{'Reg Num':<10} | {'Max Speed':<10} | {'Current Spd':<12} | {'Distance':<10}")
        print("-" * 55)
        for car in self.cars:
            print(f"{car.registration_number:<10} | {car.max_speed:>3} km/h   | "
                  f"{car.current_speed:>3} km/h     | {car.distance_traveled:>6.1f} km")

    def race_finished(self):
        for car in self.cars:
            if car.distance_traveled >= self.distance:
                return True
        return False


participating_cars = []
for i in range(1, 11):
    max_spd = random.randint(100, 200)
    participating_cars.append(Car(f"ABC-{i}", max_spd))

derby = Race("Grand Demolition Derby", 8000, participating_cars)

hours_elapsed = 0
while not derby.race_finished():
    derby.hour_passes()
    hours_elapsed += 1
    
    if hours_elapsed % 10 == 0:
        print(f"\n--- Hour {hours_elapsed} Status ---")
        derby.print_status()

print(f"\n RACE FINISHED after {hours_elapsed} hours! ")
derby.print_status()