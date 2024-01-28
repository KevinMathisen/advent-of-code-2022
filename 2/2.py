input = open("input.txt")
cont = input.read()


"""
cont = A Y
B X
C Z
"""

ls = list(cont.split("\n"))
ls.remove("")

for n in range(0,len(ls)):
	ls[n] = ls[n].split(' ')
	print(str(ls[n]))

def calculateScore(O, R):
	scoreShape = 1
	scoreOutcome = 0


	if R == 'Y':
		scoreOutcome = 3
		if O == 'B':
			scoreShape = 2
		if O == 'C': 
			scoreShape = 3
	elif R == 'Z': 
		scoreOutcome = 6
		if O == 'A':
			scoreShape = 2
		elif O == 'B':
			scoreShape = 3

	else:
		if O == 'A':
			scoreShape = 3
		elif O == 'C':
			scoreShape = 2
	


	return scoreShape+scoreOutcome

totalScore = 0
for round in ls:
	totalScore += calculateScore(round[0], round[1])

print(totalScore)

input.close()