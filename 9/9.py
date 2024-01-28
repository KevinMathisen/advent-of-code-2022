input = open("input.txt")
cont = input.read()


"""
cont = R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


ls = list(cont.split("\n"))
ls.remove("")

headPosition = [0, 0]
tailPosition = [0, 0]
tailVisited = []

# Moves tail after head
def moveTail():
		
	xDelta = headPosition[0] - tailPosition[0]
	yDelta = headPosition[1] - tailPosition[1]

	x2dif = False
	y2dif = False

	if xDelta > 1:
		tailPosition[0] += 1
		x2dif = True
	elif xDelta < -1:
		tailPosition[0] -= 1
		x2dif = True
	
	if yDelta > 1:
		tailPosition[1] += 1
		y2dif = True
	elif yDelta < -1:
		tailPosition[1] -= 1
		y2dif = True

	if xDelta > 0 and y2dif:
		tailPosition[0] += 1
	elif xDelta < 0 and y2dif:
		tailPosition[0] -= 1
		
	if yDelta > 0 and x2dif:
		tailPosition[1] += 1
	elif yDelta < 0 and x2dif:
		tailPosition[1] -= 1

# Move head by instruction
def moveHead(direction):
	if direction == 'U':
		headPosition[1] -= 1
	elif direction == 'D':
		headPosition[1] += 1
	elif direction == 'R':
		headPosition[0] += 1
	elif direction == 'L':
		headPosition[0] -= 1
	


# Task 1
def task1():

	tailVisited.append(str(tailPosition))

	# for each line
	for line in ls:
		line = line.split(' ')
		# for each motion
		for i in range(int(line[1])):
			moveHead(line[0])
			moveTail()
			if str(tailPosition) not in tailVisited:
				tailVisited.append(str(tailPosition))

	return len(tailVisited)

# Task 2 -----------------------------------------

headPosition2 = [0, 0]
knotsPosition = []
for i in range(9):
	knotsPosition.append([0, 0])
tailVisited2 = []

# Moves tail after head, num -> 0-8
def moveKnot(num):

	if num == 0:
		xDelta = headPosition2[0] - knotsPosition[num][0]
		yDelta = headPosition2[1] - knotsPosition[num][1]
	else:
		xDelta = knotsPosition[num-1][0] - knotsPosition[num][0]
		yDelta = knotsPosition[num-1][1] - knotsPosition[num][1]

	x2dif = False
	y2dif = False

	if xDelta > 1:
		knotsPosition[num][0] += 1
		x2dif = True
	elif xDelta < -1:
		knotsPosition[num][0] -= 1
		x2dif = True
	
	if yDelta > 1:
		knotsPosition[num][1] += 1
		y2dif = True
	elif yDelta < -1:
		knotsPosition[num][1] -= 1
		y2dif = True

	if y2dif and x2dif:
		return

	if xDelta > 0 and y2dif:
		knotsPosition[num][0] += 1
	elif xDelta < 0 and y2dif:
		knotsPosition[num][0] -= 1
		
	if yDelta > 0 and x2dif:
		knotsPosition[num][1] += 1
	elif yDelta < 0 and x2dif:
		knotsPosition[num][1] -= 1

# Move head by instruction
def moveHead2(direction):
	if direction == 'U':
		headPosition2[1] -= 1
	elif direction == 'D':
		headPosition2[1] += 1
	elif direction == 'R':
		headPosition2[0] += 1
	elif direction == 'L':
		headPosition2[0] -= 1

# Task 2
def task2():
	tailVisited2.append(str(knotsPosition[8]))

	# for each line
	for line in ls:
		line = line.split(' ')
		# for each motion
		for i in range(int(line[1])):
			moveHead2(line[0])
			for j in range(9):
				moveKnot(j)
			if str(knotsPosition[8]) not in tailVisited2:
				tailVisited2.append(str(knotsPosition[8]))

	return len(tailVisited2)


print(task1())

print(task2())
	


		