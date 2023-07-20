import random
key0 = []
while len(key0) < 10:
    while True:
        candidate = random.randint(0, 9)
        if candidate in key0:
            continue
        key0.append(candidate)

key1 = []
while len(key1) < 10:
    while True:
        candidate = random.randint(10, 19)
        if candidate in key1:
            continue
        key1.append(candidate)
