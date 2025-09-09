def flatten(stack: list) -> list:
    flat = []

    for i in stack:
        if isinstance(i, list):
            flat.extend(flatten(i))
        else:
            flat.append(i)     
    
    return flat

stack = [1, [2, [3, 4, 5], 6], 7]
flat = flatten(stack)

print(flat)