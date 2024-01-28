input = open("input.txt")
cont = input.read()


"""
cont = 2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

ls = list(cont.split("\n"))
ls.remove("")

for n in range(len(ls)):
	ls[n] = ls[n].split(',')
	for j in range(len(ls[n])):
		ls[n][j] = ls[n][j].split('-')
		ls[n][j][0] = int(ls[n][j][0])
		ls[n][j][1] = int(ls[n][j][1])
print(ls)

def checkIfInside(pair):
	# First is inside second

	if (pair[0][0] >= pair[1][0]) and (pair[0][1] <= pair[1][1]):
		return True
	# Second is inside first
	elif (pair[0][0] <= pair[1][0]) and (pair[0][1] >= pair[1][1]):
		return True

	return False


def checkIfOverlap(pair):
	if pair[0][1] < pair[1][0] or pair[1][1] < pair[0][0]: 
		return False
	return True

def task1():
	sum = 0
	
	for pair in ls:
		if checkIfInside(pair):
			sum+=1

	return sum

# Task 2
def task2():
	sum = 0
	
	for pair in ls:
		if checkIfOverlap(pair):
			sum+=1

	return sum
	return 0

print(task1())

print(task2())
	


		