import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

sames = 0
for _ in range(trials):
	classroom = []
	for i in range(people):
		birthday = random.randint(0, day-1)
		classroom.append(birthday)

	same_birthday = False
	for i in range(0, len(classroom)):
		for j in range(i+1, len(classroom)):
			if classroom[i] == classroom[j]:
				same_birthday = True
				break
			classroom.append(birthday)
		if same_birthday: sames +=1

print(sames/trials)
