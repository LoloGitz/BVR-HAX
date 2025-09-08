import random
import math


loops = 100000000
hits = 0

for i in range(loops):
    random_x = random.uniform(-1, 1)
    random_y = random.uniform(-1, 1)
    distance = (random_x ** 2) + (random_y ** 2)

    if (distance <= 1):
        hits += 1


print(  hits / loops * 4 )

