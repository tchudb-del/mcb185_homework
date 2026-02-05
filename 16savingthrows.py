import random

dcs = [5, 10, 15]

trials = 100

for dc in dcs:
    print("DC:", dc)

    success = 0
    for i in range(trials):
        roll = random.randint(1, 20)
        if roll >= dc:
            success += 1
    print(" Normal success rate:", success / trials)

    success = 0
    for i in range(trials):
        roll1 = random.randint(1, 20)
        roll2 = random.randint(1, 20)
        roll = max(roll1, roll2)
        if roll >= dc:
            success += 1
    print(" Advantage success rate:", success / trials)

    success = 0
    for i in range(trials):
        roll1 = random.randint(1, 20)
        roll2 = random.randint(1, 20)
        roll = min(roll1, roll2)
        if roll >= dc:
            success += 1
    print(" Disadvantage success rate:", success / trials)

