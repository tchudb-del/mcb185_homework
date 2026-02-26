import sys
import random

people = int(sys.argv[1])
calendar = int(sys.argv[2])
iterations = int(sys.argv[3])

sames = 0
for _ in range(iterations):
	days = [0] * calender
	for _ in range(people):
		birthday = random.randint(0, calendar-1)
		days[birthday] += 1

	same_birthday = False
	for v in calendar:
		if v > 1:
			same_birthday = True
	if same_birthday: sames += 1

print(sames/iterations)




