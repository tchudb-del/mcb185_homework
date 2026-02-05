import random

trials = 100000

dies = 0
stabilizes = 0
revives = 0

for i in range(trials):
    successes = 0
    failures = 0
    done = False

    while done == False:
        roll = random.randint(1, 20)

        if roll == 20:
            revives += 1
            done = True

        elif roll == 1:
            failures += 2
            if failures >= 3:
                dies += 1
                done = True

        elif roll < 10:
            failures += 1
            if failures >= 3:
                dies += 1
                done = True

        else:
            successes += 1
            if successes >= 3:
                stabilizes += 1
                done = True

print("Trials:", trials)
print("Die probability:", dies / trials)
print("Stabilize probability:", stabilizes / trials)
print("Revive probability:", revives / trials)

