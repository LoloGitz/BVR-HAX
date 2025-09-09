def fibonacci(number: int) -> int:
    fib = [0, 1]

    if (number <= 1):
        return fib[number]
    
    for i in range(number - 1):
        fib_length = len(fib) - 1
        fib.append(fib[fib_length - 1] + fib[fib_length])

    return fib[len(fib) - 1]


print(fibonacci(8))
