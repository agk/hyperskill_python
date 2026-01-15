import math

angle_b = 35
angle_c = 105
side_b = 7

# angle_a = 180 - angle_c - angle_b
# angle_a_rad = math.radians(angle_a)

side_c = side_b * math.sin(math.radians(angle_c)) / math.sin(math.radians(angle_b))
print(round(side_c, 1))
