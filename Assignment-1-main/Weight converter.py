t = float(input("Enter talents: "))
p = float(input("Enter pounds: "))
l = float(input("Enter lots: "))

total_grams = (t * 20 * 32 * 13.3) + (p * 32 * 13.3) + (l * 13.3)
kg = int(total_grams / 1000)
grams = round(total_grams % 1000,2)

print ("The weight in modern units: ", str(kg) + " kilograms and "+ str(grams) + " grams.", sep="\n")