
input = open("input.txt")
cont = input.read()


"""
cont = 30373
25512
65332
33549
35390
"""


ls = list(cont.split("\n"))
ls.remove("")

trees = []

for line in ls:
	treeLine = []
	for i in range(len(line)):
		treeLine.append(int(line[i]))

	trees.append(treeLine)

minX = 0
maxX = len(trees[0])-1
minY = 0
maxY = len(trees)-1

print(trees)


def treeOnEdge(x, y):
	return x == minX or x == maxX or y == minY or y == maxY

# Find if a direction of trees are under a certain height
def isClear(height, x, y, deltaX, deltaY):
	# For each tree in direction until we get to end
	while True:
		
		# Check if there are more trees to check
		if treeOnEdge(x, y):
			break

		# Move in line for next tree
		x += deltaX
		y += deltaY

		# Check if the tree is over the reqired height
		if trees[y][x] >= height:
			return False
		
	return True
		


# Find is tree is visible, from coordinates and grid
def isVisible(x, y):
	height = trees[y][x]

	# Check if tree on edge
	if treeOnEdge(x, y):
		return True

	# Check each direction is clear north, east, south, and west:
	elif isClear(height, x, y, 0, -1) or isClear(height, x, y, 1, 0) or isClear(height, x, y, 0, 1) or isClear(height, x, y, -1, 0):
		return True
	
	return False


# Task 1
def task1():
	treesVisible = 0

	for y in range(len(trees)):
		for x in range(len(trees[y])):
			if isVisible(x, y):
				treesVisible += 1

	return treesVisible

# Get score in one direction
def getScoreDir(height, x, y, deltaX, deltaY):
	score = 0

	# For each tree in direction until we get to end or same height
	while True:
		
		# Check if there are more trees to check
		if treeOnEdge(x, y):
			break

		# Move in line for next tree
		x += deltaX
		y += deltaY

		# Add tree count
		score += 1

		# Check if the tree is over the reqired height
		if trees[y][x] >= height:
			break
		
		

		

	return score

# Get the scenic score for a tree
def getScenicScore(x, y):
	height = trees[y][x]

	# Check if tree on edge
	if treeOnEdge(x, y):
		return 0

	# Get score for each direction:
	north = getScoreDir(height, x, y, 0, -1)
	east = getScoreDir(height, x, y, 1, 0)
	south = getScoreDir(height, x, y, 0, 1)
	west = getScoreDir(height, x, y, -1, 0)
	
	return north*east*south*west


# Task 2
def task2():

	maxScenicScore = 0

	for y in range(len(trees)):
		for x in range(len(trees[y])):
			scenicScore = getScenicScore(x, y)
			if scenicScore > maxScenicScore:
				maxScenicScore = scenicScore

	return maxScenicScore


print(task1())

print(task2())
	


		