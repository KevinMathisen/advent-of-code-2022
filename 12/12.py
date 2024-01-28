input = open("input.txt")
cont = input.read()


"""
cont = Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


ls = list(cont.split("\n"))
ls.remove("")

# Info if all tiles, including: Elevation, lowest found distance from start, and previous tile for said distance
tiles = []
#unvisited_tiles = []
to_visist = []

def set_up_data():
	global tiles
	tiles = []
	global to_visist
	to_visist = []

	
	startY = 0
	startX = 0
	endY = 0
	endX = 0
	
	# for each row
	for i in range(len(ls)):
		tiles_row = []

		# for each letter/tile
		for j in range(len(ls[i])):
			letter = ls[i][j]

			# Get elevation of TILE
			if letter == 'S':
				elevation = 0
				startY = i
				startX = j
			elif letter == 'E':
				elevation = ord('z') - ord('a')
				endY = i
				endX = j
			else:
				elevation = ord(letter) - ord('a')
		
			# Set initial high distance
			distance = 1000
			# Not previous tile at start
			prev_tile_x = 0
			prev_tile_y = 0

			# save tile info
			tiles_row.append([elevation, distance, prev_tile_x, prev_tile_y])
			# save unvisisted tiles for faster traversing
			#unvisited_tiles.append([j, i])

		tiles.append(tiles_row)

	
	#print(unvisited_tiles)

	return startX, startY, endX, endY
		

# Initialize start tile to 0 distance
def initialize(startX, startY):
	# Remove startTile from unvisisted
	#unvisited_tiles[startY].pop(startX)

	# Set distance from start to 0
	tiles[startY][startX][1] = 0
	# Add startTile coordinates, along with distance to to_visist tiles
	to_visist.append([startX, startY, 0])


# Return the coordinates of the next tile we want to evalute neighbours
def get_coordinates_next_tile():
	lowest_distance = 1000
	coordinates_next_tile = [0, 0]

	# For each tile we should visit (One if its neighbours have been visited)
	for tile in to_visist:
		
		# If lowest distance from start and should visit
		if tile[2] < lowest_distance:
			# Save distance from start and coordinates
			lowest_distance = tile[2]
			coordinates_next_tile = [tile[0], tile[1]]

	# Return the coordinates of the next tile we want to evalute neighbours
	return coordinates_next_tile[0], coordinates_next_tile[1]


# Check if we have found new best path to a neighbour
def check_neighbour(x, y, x_prev, y_prev, elevation_prev, distance_prev):
	# check if the neighbour is reachable
	if tiles[y][x][0] > elevation_prev + 1:
		return
	
	prev_distance = tiles[y][x][1]

	# Check if neighbour already has a lower distance
	if prev_distance <= distance_prev + 1:
		return
	
	# Has found new lowest path:
	tiles[y][x][1] = distance_prev + 1
	tiles[y][x][2] = x_prev
	tiles[y][x][3] = y_prev

	# Mark this tile as a possible new tile to find neighbours for
	to_visist.append([x, y, distance_prev + 1])



# Check if we have found new best path to each neighbour of tile
def traverse_neighbours_of_tile(x, y):
	elevation = tiles[y][x][0]
	distance = tiles[y][x][1]
	
	# Check each neighbour
	if y > 0:
		check_neighbour(x, y-1, x, y, elevation, distance)
	if x < max_x:
		check_neighbour(x+1, y, x, y, elevation, distance)
	if y < max_y:
		check_neighbour(x, y+1, x, y, elevation, distance)
	if x > 0:
		check_neighbour(x-1, y, x, y, elevation, distance)

	# Mark tile as visisted, by removing it from tiles to visit
	to_visist.remove([x, y, distance])


def move():

	# Find which tile we want to look at
	x, y = get_coordinates_next_tile()

	# Check each neigbour of tile
	traverse_neighbours_of_tile(x, y)


# -----------------------------


startX, startY, endX, endY = set_up_data()
max_x = len(tiles[0]) - 1
max_y = len(tiles) - 1

# Task 1
def task1():

	# Initialize the pathfinding
	initialize(startX, startY)

	# continue pathfinding until there are no more tiles to evaluate 
	while len(to_visist) != 0:
		move()

	return tiles[endY][endX][1]



# Task 2
def get_startingpoints():
	possible_startingpoints = []

	# Get each possible starting point
	for i in range(len(tiles)):
		for j in range(len(tiles[i])):
			if tiles[i][j][0] == 0:
				possible_startingpoints.append([j, i])

	return possible_startingpoints

def test_startingpoint(startX, startY):

	set_up_data() 

	initialize(startX, startY)

	# continue pathfinding until there are no more tiles to evaluate 
	while len(to_visist) != 0:
		move()

	return tiles[endY][endX][1]

def task2():
	
	#Get each possible starting point
	possible_startingpoints = get_startingpoints()

	print("amount of starting pos: " + str(len(possible_startingpoints)))

	lowestPath = 1000
	bestX = -1
	bestY = -1

	# For each start point
	for startingPoint in possible_startingpoints:
		# Get path length to top
		pathLenth = test_startingpoint(startingPoint[0], startingPoint[1])
		# if pathlength is lowest so far
		if pathLenth < lowestPath:
			lowestPath = pathLenth
			bestX = startingPoint[0]
			bestY = startingPoint[1]
			print("New lowest path found")
	
	return lowestPath



print(task1())

print(task2())
	

