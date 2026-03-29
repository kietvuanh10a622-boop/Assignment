cities = []

for i in range(5):
    name = input(f"Enter a city {i+1}: ")
    cities.append(name) 

print("\n List of the city you entered:")

for city in cities:
    print(city)