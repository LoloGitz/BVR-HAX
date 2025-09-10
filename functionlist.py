def parse(numlist: list, func: callable) -> list:
    result = []
    for i in numlist:
        result.append(func(i))

    return result

def thefunction(n: int) -> int:
    return n * 2

print( parse([1, 2, 4], thefunction) )