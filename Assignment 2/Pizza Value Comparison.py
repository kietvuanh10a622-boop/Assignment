import math

def calculate_unit_price(diameter_cm, price_usd):
    # Convert diameter to radius in meters
    radius_m = (diameter_cm / 2) / 100
    # Area = πr²
    area_m2 = math.pi * (radius_m ** 2)
    # Return price per square meter
    return price_usd / area_m2
 calculate_unit_price(diameter_cm, price_usd)
def compare_pizzas():
    # Pizza 1
    d1 = float(input("Enter diameter of pizza 1 (cm): "))
    p1 = float(input("Enter price of pizza 1 (USD): "))
    
    # Pizza 2
    d2 = float(input("Enter diameter of pizza 2 (cm): "))
    p2 = float(input("Enter price of pizza 2 (USD): "))
    
    unit_price1 = calculate_unit_price(d1, p1)
    unit_price2 = calculate_unit_price(d2, p2)
    
    print(f"\nPizza 1 unit price: ${unit_price1:.2f}/m²")
    print(f"Pizza 2 unit price: ${unit_price2:.2f}/m²")
    
    if unit_price1 < unit_price2:
        print("Pizza 1 provides better value for money.")
    elif unit_price2 < unit_price1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same unit price.")

# Example of how to run the main pizza program:
# compare_pizzas()
compare_pizzas()