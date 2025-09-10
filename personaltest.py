import random
import math
import copy

random.seed()

def generateNoise(x: int, y: int, iterations: int, batch: dict = None) -> dict:
    result = {}

    # print(batch)

    lowest = 1
    highest = 0

    for y_i in range(y):
        result[y_i] = {}
        for x_i in range(x):
            weight = 0
            if (batch == None):
                weight = random.uniform(0, 1)
            else:
                new_value = 0
                neighbors = 0
                

                for i in range(9):
                    xx = x_i + ((i % 3) - 1)
                    yy = y_i + (math.floor(i / 3) - 1)
                    
                    if (xx >= 0 and xx <= (x - 1) and yy >= 0 and yy <= (y - 1)):
                         # print(xx, yy)
                        new_value += batch[yy][xx]
                        neighbors += 1
                    
                weight = new_value / neighbors

            lowest = min(lowest, weight)
            highest = max(highest, weight)
            result[y_i][x_i] = weight
                    
    if (iterations > 1):
        print(iterations)
        return generateNoise(x, y, iterations - 1, result.copy())
    else:
        print(lowest, highest)

        filt = {}

        for y_i in range(y):
            filt[y_i] = {}
            for x_i in range(x):
                weight = result[y_i][x_i]
                filt[y_i][x_i] = (weight - lowest) / highest

        return filt
    

noise = generateNoise(50, 10, 5)

# for y in noise:
#     y_values = noise[y]
#     for x in y_values:
#         weight = y_values[x]
#         print(x, y, weight) -- debug

for y in noise:
    y_values = noise[y]
    print()
    for x in y_values:
        weight = y_values[x]
        if(weight >= 0.6):
            print('🟩',end='')
        elif (weight >= 0.5):
            print('🟨',end='')
        elif (weight >= 0.4):
            print('💠',end='')
        else:
            print('🟦',end='')
        