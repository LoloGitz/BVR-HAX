import random
import math
import os
import time

load_iterations = 1
load_size = 50

tiles_loaded = 0
tiles_to_load = load_size ** 2 * load_iterations

random.seed()

def clear_terminal():
    if os.name == "nt": # windows
        os.system("cls")
    else: # other (macOS or linux)
        os.system("clear")

def updateLoading():
    clear_terminal()

    global tiles_to_load
    global tiles_loaded    
    tiles_loaded += 1
    print("loading map... " + str(tiles_loaded / tiles_to_load * 1000) + "%")

def generateNoise(x: int, y: int, iterations: int, batch: dict = None) -> dict:
    result = {}

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
            updateLoading()
                    
    if (iterations > 1):
        return generateNoise(x, y, iterations - 1, result)
    else:
        filt = {}

        for y_i in range(y):
            filt[y_i] = {}
            for x_i in range(x):
                weight = result[y_i][x_i]
                filt[y_i][x_i] = (weight - lowest) / (highest - lowest)

        return filt
    
noise = generateNoise(load_size, load_size, load_iterations)

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
        if(weight >= 0.7):
            print('🟩',end='')
        elif (weight >= 0.55):
            print('🟨',end='')
        else:
            print('🟦',end='')
        