import random
import math
import os
import time

load_iterations = 4
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
    global tiles_loaded
    global tiles_to_load

    ratio = round(tiles_loaded / tiles_to_load * 100) / 100
    ratio_bar = math.floor(ratio * 10)  

    clear_terminal()
    print(
        "loading map... " 
        + str(round(ratio * 100))
        + "%\n-[ " + ("■" * ratio_bar)
        + ("□" * (10 - ratio_bar))
        + " ]-"
    )
    

def generateNoise(x: int, y: int, iterations: int, batch: dict = None) -> dict:
    global tiles_loaded
    result = {}
    lowest, highest = 1, 0

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
                        new_value += batch[yy][xx]
                        neighbors += 1
                    
                weight = new_value / neighbors

            lowest, highest = min(lowest, weight), max(highest, weight)
            result[y_i][x_i] = weight

            tiles_loaded += 1
            if (tiles_loaded % math.floor(tiles_to_load / 100) == 0):
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
    
tick = time.time()
noise = generateNoise(load_size, load_size, load_iterations)
print(time.time() - tick)

# for y in noise:
#     y_values = noise[y]
#     for x in y_values:
#         weight = y_values[x]
#         print(x, y, weight) -- debug

while True:
    clear_terminal()

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

        print('',end='\r')