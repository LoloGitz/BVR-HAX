import random
import math

random.seed(0)

def generateNoise(x: int, y: int, neighbor: int) -> list:
    result = []

    for x_i in range(x):
        result[x_i] = []
        for y_i in range(y):
            result[x_i][y_i] = random.randint(0, 1)


for i in noise:
    print()
    for o in i:
        if(o == 0):
            print('-',end='')
        else:
            print('#',end='')