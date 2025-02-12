import math

def regular_polygon_area(sides, length):
    return (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))

sides = 4
length = 25
area = regular_polygon_area(sides, length)

print(f"Input number of sides: {sides}")
print(f"Input the length of a side: {length}")
print(f"The area of the polygon is: {area:.1f}")
