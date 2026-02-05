import math

for a in range(1, 100):
    for b in range(a, 100):
        c = math.sqrt(a*a + b*b)
        if c % 1 == 0:
            print(a, b, int(c))
