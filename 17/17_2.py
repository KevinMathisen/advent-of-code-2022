input = open("input.txt")
cont = input.read()


"""
cont = >>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""

inn = """####

.#.
###
.#.

###
..#
..#

#
#
#
#

##
##"""

cont = cont.rstrip('\n')


inn = inn.split('\n\n')

#ls = list(cont.split("\n"))
#ls.remove("")
	
def setup():
	global environment 
	environment = []
	floor = []
	for i in range(7):
		floor.append('#')

	environment.append(floor)
	for i in range(3):
		level = []
		for j in range(7):
			level.append('.')

	global rocks
	rocks = []

	for input in inn: 
		figure = []
		input = input.split('\n')
		for row in input:
			figure.append(row)

		rocks.append(figure)

	global len_rocks
	len_rocks = 1000000

	global highest_rock
	highest_rock = 0

	global wind_num
	wind_num = 0
			
setup()
print(environment)
print(rocks)

def no_collision_right(x, y, rock):

	for i in range(len(rock)):
		for j in range(len(rock[i])):
			
			if rock[i][j] == '.':
				continue

			x_piece = x+j
			y_piece = y+i
			
			if environment[y_piece][x_piece+1] == '#':
				return False
			
	return True

def no_collision_left(x, y, rock):

	for i in range(len(rock)):
		for j in range(len(rock[i])):
			
			if rock[i][j] == '.':
				continue

			x_piece = x+j
			y_piece = y+i
			
			if environment[y_piece][x_piece-1] == '#':
				return False
			
	return True

# Get coordinates from wind
def wind_push(x, y, symbol, width, rock):
	# todo better collision
	if x + width-1 >= 6 and symbol == '>':
		return x, y
	elif x <= 0 and symbol == '<':
		return x, y
	if symbol == '>' and no_collision_right(x, y, rock):
		return x+1, y
	elif symbol == '<' and no_collision_left(x, y, rock):
		return x-1, y
	
	return x, y

def check_collision(rock, x, y):
	
	for i in range(len(rock)):
		for j in range(len(rock[i])):
			# For every piece of rock
			piece = rock[i][j]

			if piece == '.':
				continue

			x_piece = x+j
			y_piece = y+i

			if environment[y_piece-1][x_piece] == '#':
				return True
				

	return False

def save_rock(rock, x, y):
	global highest_rock  
	for i in range(len(rock)):
		for j in range(len(rock[i])):
			# For every piece of rock
			piece = rock[i][j]

			if piece == '.':
				continue

			x_piece = x+j
			y_piece = y+i

			environment[y_piece][x_piece] = '#'

	# update highest rock
	for y in range(len(environment)):
		for x in range(7):
			if environment[-(y+1)][x] == '#':
				highest_rock = len(environment)-y-1 
				return


def fall(rock, x, y):
	# check if collisin if fall
	if check_collision(rock, x, y): 
		# then save rock to environment
		save_rock(rock, x, y)

		return False

	# return true
	return True

def spawn_rock():
	# Expand environment
	desired_length = highest_rock+8
	expand_length = desired_length-len(environment)
	for i in range(expand_length):
		line = []
		for j in range(7):
			line.append('.')
		environment.append(line)

	# Get coordinates of new rock
	x = 2
	y = highest_rock + 4

	return x, y

def print_env():
	for i in range(len(environment)):
		line = ''
		for j in range(len(environment[i])):
			line+=environment[-i-1][j]
		print(line)

def get_next_wind():
	global wind_num
	wind = cont[wind_num]
	wind_num = (wind_num+1)%len(cont)
	return wind

def rock_cycle(i):
	# get x, y, spawn rock
	x, y = spawn_rock()

	# get rock type
	rock = rocks[i%len(rocks)]

	# get width of rock
	width = len(rock[0])

	# Simulate falling
	falling = True
	while falling:
		# push wind
		direction = get_next_wind()
		x, y = wind_push(x, y, direction, width, rock)

		# Try to fall
		if fall(rock, x, y):
			y -= 1
		else:
			falling = False

def detect_cycle():

	# start at comparing half of all rocks, down to only last 2 rocks
		# maybe only try to find identical to start

	# all rocks are saved as a number in the env
	# choose ranges to compare, which start at same rock and wind
	# then compare if all equivalent rocks are at the same place 
	# if no difference until end, save the ranges

	pass

def task1():
	# for each rock
	for i in range(len_rocks):
		if i == len(rocks)*4:
			print_env()
			print(1)
		
		rock_cycle(i)
		
		#print_env()
		#print('\n\n')

		# Try to detect if there is a cycle
		cycle = detect_cycle()
		# if there was a cycle
		if len(cycle) != 0:
			break
	
	# Calculate length missing
	# total_length / cycle_length (int) -> amount of cycles
	# remaining = total_length - amount_cycles*cycle_length

	# for each rock for missing rocks, calculate
		# go from start until length needed, then add to total height

	# return highest rock

	return highest_rock

# Task 2
def task2():
	

	return 0


print(task1())
print(task2())

#print_env()