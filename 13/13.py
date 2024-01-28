import json

input = open("input.txt")
cont = input.read()


"""
cont = [1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


ls = list(cont.split("\n\n"))
#ls.remove("")
	
def set_up():
	global packets
	packets = []

	for pairsNum in range(len(ls)):
		pair_str = ls[pairsNum].split('\n')
		pair = []

		if pairsNum == len(ls) -1:
			pair_str.remove("")

		pair.append(json.loads(pair_str[0]))
		pair.append(json.loads(pair_str[1]))

		packets.append(pair)

def set_up2():
	ls2 = list(cont.split("\n"))
	ls2 = list(filter(None, ls2))

	global packets2
	packets2 = []

	for packetNum in range(len(ls2)):

		packets2.append(json.loads(ls2[packetNum]))

	packets2.append([[2]])
	packets2.append([[6]])

set_up()
set_up2()
#print(packets)
print(packets2)

# Compares two lists/packets
# Return 1 if right order, 2 if wrong order, 0 if not decided
def compare(left, right):

	i = 0

	# Go trough all values in packets/lists
	while True:

		# if left ran out of items first
		if i == len(left) and i < len(right):
			return 1
		# if right ran out of items first
		elif i == len(right) and i < len(left):
			return 2
		# if both ran out at the same time
		elif i == len(right) and i == len(left):
			return 0
		
		leftValue = left[i]
		rightValue = right[i]
	
		# If both values are integers
		if type(leftValue) is int and type(rightValue) is int:
			if leftValue < rightValue:
				return 1
			elif leftValue > rightValue:
				return 2
			
		# If both values are lists
		elif type(leftValue) is list and type(rightValue) is list:		
			
			# Check if lists are in right order
			result = compare(leftValue, rightValue)
			# If lists order were found (is 1 or 2)
			if result != 0:
				return result
			
		# if one value is an interger
		elif type(leftValue) == int:
			# Check if lists are in right order
			result = compare([leftValue], rightValue)
			# If lists order were found (is 1 or 2)
			if result != 0:
				return result
	
		elif type(rightValue) == int:
			# Check if lists are in right order
			result = compare(leftValue, [rightValue])
			# If lists order were found (is 1 or 2)
			if result != 0:
				return result
		
		# iterate to next values
		i += 1

	

# Task 1
def task1():
	rightOrder = []

	for packetNum in range(len(packets)):
		order = compare(packets[packetNum][0], packets[packetNum][1])
		if order == 1:
			rightOrder.append(packetNum+1)

	sum = 0
	for i in rightOrder:
		sum += i

	return sum

# Task 2
def task2():
	global packets2
	
	# For each packet, compare with all trailing packets
	for i in range(len(packets2)):
		for j in range(i+1, len(packets2)):

			# Compare packets
			result = compare(packets2[i], packets2[j])

			# Switch positions if wrong order
			if result == 2:
				temp = packets2[i]
				packets2[i] = packets2[j]
				packets2[j] = temp

	# Get index of dividers
	index1 = 0
	index2 = 0
	for i in range(len(packets2)):
		if packets2[i] == [[2]]:
			index1 = i+1
		if packets2[i] == [[6]]:
			index2 = i+1

	return index1 * index2


print(task1())

print(task2())
	

