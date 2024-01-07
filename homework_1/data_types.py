import math

# Task 1

first_name = "Yurii"
last_name = "lykhitskyi"


full_name = first_name + " " + last_name
print(full_name)
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

first_name = "\t" + first_name + "   \n"
print(first_name)

trimmed_name = first_name.strip()
print(trimmed_name)


# Task 2

radius = 3

circumference = 2 * math.pi * radius
area = math.pi * radius**2

print(f"Length of the circle with radius {radius}: {circumference:.2f} units")
print(f"Area of the circle with radius {radius}: {area:.2f} square units")


# Task 3

current_exchange_rate = 38.5
amount_in_uah = 1000

amount_in_usd = round(amount_in_uah / current_exchange_rate, 2)

print(f"Current exchange rate: {amount_in_usd} usd for {amount_in_uah} uah")
