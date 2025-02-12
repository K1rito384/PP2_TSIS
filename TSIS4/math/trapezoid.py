def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height

height = 5
base1 = 5
base2 = 6
area = trapezoid_area(height, base1, base2)

print(f"Height: {height}")
print(f"Base, first value: {base1}")
print(f"Base, second value: {base2}")
print(f"Expected Output: {area}")
