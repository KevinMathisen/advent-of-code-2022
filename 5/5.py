input = open("input.txt")
cont = input.read()


"""
cont =    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

ls = list(cont.split("\n\n"))

startcrates = ls[0].split('\n')
instructions = ls[1].split('\n')
instructions.remove("")


# Create storage list ----------------
storage = []
for i in range(9):
	storage.append([])

for row in startcrates:
	chars = []
	for i in range(9):
		chars.append(' ')
	
	chars[0] = row[1]
	chars[1] = row[5]
	chars[2] = row[9]
	chars[3] = row[13]
	chars[4] = row[17]
	chars[5] = row[21]
	chars[6] = row[25]
	chars[7] = row[29]
	chars[8] = row[33]

	for n in range(len(chars)):
		if chars[n].isupper():
			storage[n].insert(0, chars[n])

print(storage)

# Create instuctions list ---------------------
instr = []

for instruction in instructions:
	instruction = instruction.split(' ')
	instr.append([int(instruction[1]), int(instruction[3]), int(instruction[5])])

print(instr)


# Task 1
def task1():
	
	# do each instruction
	for instruction in instr:
		# For each move
		for n in range(instruction[0]):
			# Add the crate to the new stack
			storage[instruction[2]-1].append(storage[instruction[1]-1][-1])
			# Remove create from old stack
			storage[instruction[1]-1].pop()

	# add each top crate to list
	output = ''
	for stack in storage:
		output += stack[-1]


	return output

# Task 2
def task2():
	
	# do each instruction
	for instruction in instr:
		tempstack = []
		# For each move, move to tempstack
		for n in range(instruction[0]):
			# Add the crate to the tempstack
			tempstack.append(storage[instruction[1]-1][-1])
			# Remove create from old stack
			storage[instruction[1]-1].pop()

		# For each move, move from tempstack
		for n in range(instruction[0]):
			# Add the crate to the new stack
			storage[instruction[2]-1].append(tempstack[-1])
			# Remove create from tempstack
			tempstack.pop()

	# add each top crate to list
	output = ''
	for stack in storage:
		output += stack[-1]


	return output



#print(task1())

print(task2())
	


		