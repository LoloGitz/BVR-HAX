import random
import math
import os
import time
import asyncio

pip install keyboard
import keyboard

load_iterations = 4
load_x = 10
load_y = 10
camera_range_x = 21
camera_range_y = 20

tiles_loaded = 0
tiles_to_load = load_x * load_y * load_iterations

random.seed()

def update_terminal(message: str = None) -> None:
    if os.name == 'nt':  # If the operating system is Windows
        os.system('cls')
    else:  # If the operating system is macOS or Linux
        os.system('clear')
    
    if (message != None):
        print(message)

def updateLoading():
    global tiles_loaded
    global tiles_to_load

    ratio = round(tiles_loaded / tiles_to_load * 100) / 100
    ratio_bar = math.floor(ratio * 10)  

    update_terminal(
        "loading map... " 
        + str(round(ratio * 100))
        + "%\n-[ " + ("■" * ratio_bar)
        + ("□" * (10 - ratio_bar))
        + " ]-"
    )
    
#update_terminal()

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
noise = generateNoise(load_x, load_y, load_iterations)
print("loadtime: " + str(time.time() - tick))

time.sleep(1)

camera_pos_x = round(load_x / 2)
camera_pos_y = round(load_y / 2)

async def display():
    try:
        while True: 
            display = ""

            if keyboard.is_pressed("w"):
                camera_pos_x += 1

            for cam_iy in range(camera_range_y):
                for cam_ix in range(camera_range_x):
                    xx = camera_pos_x + (cam_ix % camera_range_x) - math.floor(camera_range_x / 2)
                    yy = camera_pos_y + cam_iy - math.floor(camera_range_y / 2)

                    if (xx >= 0 and xx <= (load_x - 1) and yy >= 0 and yy <= (load_y - 1)):
                        weight = noise[yy][xx]
                    else:
                        weight = -1

                    if (weight == -1):
                        display += "⬛"
                    elif (weight >= 0.7):
                        display += "🟩"
                    elif (weight >= 0.55):
                        display += "🟨"
                    else:
                        display += "🟦"
                    
                display += "\n"
                
            
            update_terminal(display)
            await asyncio.sleep(1/30)

    except asyncio.CancelledError:
        print("cancelled!")

    finally:
        print("finished!")

asyncio.run(display())