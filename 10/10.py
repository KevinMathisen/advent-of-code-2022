input = open("input.txt")
cont = input.read()


"""
cont = addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""


ls = list(cont.split("\n"))
ls.remove("")
	
# find if correct cycle
def corCycle(num):
	#return num == 20 or num == 60 or num == 100 or num == 140 or num == 180 or num == 220
	return (num-20)%40 == 0


# Task 1
def task1():

	cycle = 0
	x = 1

	sum = 0

	for instruction in ls:


		if 'noop' in instruction:
			cycle += 1
			if corCycle(cycle):
				sum += x*cycle

		elif 'addx' in instruction:
			cycle += 1
			if corCycle(cycle):
				sum += x*cycle
			
			cycle += 1
			if corCycle(cycle):
				sum += x*cycle

			# Happends when this cycle is completed
			x += int(instruction.split(' ')[1])

		else:
			print('invalid instruction')

	return sum


	

# Task 2

# execute a cycle
def doCycle(cycle, x, sum):
	

	# Draw pixle
	# Get pixel location from cycle
	pixelX = cycle%40-1
	pixelY = cycle//40

	# Check if sprite overlaps current pixle
	if pixelX == x-1 or pixelX == x or pixelX == x+1:
		# Draw correct pixel
		screen[pixelY][pixelX] = '#'




# create screen
screen = []
for rowNum in range(6):
	row = []
	for pixelNum in range(40):
		row.append('.')
	screen.append(row)


# Task 1
def task2():

	cycle = 0
	x = 1

	for instruction in ls:


		if 'noop' in instruction:
			# Start cycle
			cycle += 1
			doCycle(cycle, x, sum)

		elif 'addx' in instruction:
			# Start cycle
			cycle += 1
			doCycle(cycle, x, sum)
			
			# Start cycle
			cycle += 1
			doCycle(cycle, x, sum)

			# Happends when this cycle is completed
			x += int(instruction.split(' ')[1])

		else:
			print('invalid instruction')

	


print(task1())

task2()
for row in screen:
	print(row)
	


		