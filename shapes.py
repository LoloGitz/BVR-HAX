import math

def shape(x: float, y: float, shape: str) -> float:
    if shape == "square" or shape == "rectangle":
        return x * y
    elif shape == "triangle":
        return x * y / 2
    elif shape == "circle":
        return x ** 2 * math.pi
    

print(shape(215, 147, "triangle")) 