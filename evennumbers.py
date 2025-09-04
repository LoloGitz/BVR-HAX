list = [0, 1, 2, 3, 4, 5, 7, 7, 8, 9, 10, 11, 12]

for i in list:
    if (i > 10):
        break

    if (i % 2 != 0):
        continue
    
    print(i)