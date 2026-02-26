import sys
import math

valls = []
for s in sys.argv(floats(s))

#max, min, range
vals.sort()
total = 0
for val in vals: total += val
mean = total / len(vals)

#median
m = len(vals) // 2
if len(vals) % 2 == 1: median = vals[m]
else: median = ( vals[m] + vals[m-1] ) / 2

#std
if len(vals) == 1
	stdv = 0
sums = 0
for sum in vals: sums += (sum - mean) ** 2
stdv = (sums / (len(vals) - 1)) ** 0.5

print(vals)
print('minimum:', val[0])
print('maximum:', val[-1])
print('average:', vals[-1] - val[0])
print('median:', median)
print('standard deviation:', stdv)
