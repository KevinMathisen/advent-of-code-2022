input = open("input.txt")
cont = input.read()


"""
cont = 498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


ls = list(cont.split("\n"))
ls.remove("")
rocks = []
startingPos = [500, 0]

def drawLine(start, end):
	startx = start[0]
	starty = start[1]
	endx = end[0]
	endy = end[1]

	deltax = 0
	deltay = 0

	if startx != endx:
		if startx > endx:
			temp = startx
			startx = endx
			endx = temp


		for x in range(startx, endx+1):
			grid[starty][x] = '#'

	else:
		if starty > endy:
			temp = starty
			starty = endy
			endy = temp


		for y in range(starty, endy+1):
			grid[y][startx] = '#'

def set_up():

	max_x = 0
	min_x = 1000
	max_y = 0
	min_y = 1000

	for i in range(len(ls)):
		line = ls[i].split(' -> ')
		rock = []

		# For each coordinate
		for j in range(len(line)):
			x = int(line[j].split(',')[0])
			y = int(line[j].split(',')[1])

			if x > max_x:
				max_x = x
			if x < min_x:
				min_x = x
			if y > max_y:
				max_y = y
			if y < min_y:
				min_y = y

			rock.append([x, y])
		
		rocks.append(rock)

	max_x += 2
	min_x -= 1
	max_y += 3
	min_y -= 1

	startingPos[0] -= min_x

	for i in range(len(rocks)): 
		for j in range(len(rocks[i])):
			rocks[i][j][0] -= min_x

	global grid
	grid = []

	for y in range(max_y):
		grid_line = []

		if y == max_y - 1:
			for x in range(max_x-min_x):
				grid_line.append('#')
		else:				
			for x in range(max_x-min_x):
				grid_line.append('.')

		grid.append(grid_line)
		
	for rock in rocks:
		for corNum in range(len(rock)-1):
			drawLine(rock[corNum], rock[corNum+1])
	
	grid[startingPos[1]][startingPos[0]] = '+'

	for line in grid:
		print(line)

def set_up2():

	max_x = 0
	min_x = 1000
	max_y = 0
	min_y = 1000

	for i in range(len(ls)):
		line = ls[i].split(' -> ')
		rock = []

		# For each coordinate
		for j in range(len(line)):
			x = int(line[j].split(',')[0])
			y = int(line[j].split(',')[1])

			if x > max_x:
				max_x = x
			if x < min_x:
				min_x = x
			if y > max_y:
				max_y = y
			if y < min_y:
				min_y = y

			rock.append([x, y])
		
		rocks.append(rock)

	max_x = 1000
	min_x = 0
	max_y += 3
	min_y -= 1

	global grid
	grid = []

	for y in range(max_y):
		grid_line = []

		if y == max_y - 1:
			for x in range(max_x):
				grid_line.append('#')
		else:				
			for x in range(max_x):
				grid_line.append('.')

		grid.append(grid_line)
		
	for rock in rocks:
		for corNum in range(len(rock)-1):
			drawLine(rock[corNum], rock[corNum+1])
	
	grid[startingPos[1]][startingPos[0]] = '+'

	print("y of grid:" + str(len(grid)))
	print("x of grid:" + str(len(grid[0])))

# return True if landed, False if abyss
def moveSand(x, y):
	# if sand has reached abyss
	if y == len(grid)-1:
		return False


	# If sand can fall
	if grid[y+1][x] == '.':
		return moveSand(x, y+1)

	# if sand can fall to left
	elif x > 0 and grid[y+1][x-1] == '.': 
		return moveSand(x-1, y+1)

	# if sand can fall to right
	elif x < len(grid[0])-1 and grid[y+1][x+1] == '.':
		return moveSand(x+1, y+1)
	
	elif y == 0:
		return False
	# if sand cant fall
	else:
		grid[y][x] = 'o'
		return True

#set_up()
set_up2()



# Task 1
def task1():
	rest = 0
	
	while True:
		landed = moveSand(startingPos[0], startingPos[1])
		print("sand moved")
		if not landed:
			break

		rest += 1

	return rest

# Task 2
def task2():
	rest = 0
	
	while True:
		landed = moveSand(startingPos[0], startingPos[1])
		print("sand moved")
		if not landed:
			break

		rest += 1

	return rest+1


#print(task1())

print(task2())
	

