import random

def find_value():
    try:
        total_points = int(input("How many random points should be generated? "))
        points_inside_circle = 0

        for _ in range(total_points):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)

            # Check if point is inside the unit circle
            if x**2 + y**2 < 1:
                points_inside_circle += 1

        pi_approximation = 4 * (points_inside_circle / total_points)
        print(f"Approximation of pi: {pi_approximation}")
        
    except (ValueError, ZeroDivisionError):
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    find_value()