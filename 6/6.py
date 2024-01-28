from collections import Counter

input = open("input.txt")
cont = input.read()


"""
cont = bvwbjplbgvbhsrlpgdmjqwftvncz
"""

'''
ls = list(cont.split("\n"))
instructions.remove("")
'''

# Task 1
def task1():

	# for each character in data-stream:
	for i in range(len(cont)):
		# Dont process first 3 characters
		if i < 3:
			continue

		# If last 4 chars all unique:
		char4 = str(cont[i] + cont[i-1] + cont[i-2] + cont[i-3])
		distinct = len(Counter(char4))
		length = len(char4)
		if distinct == length:
			return i+1

	return -1

# Task 2
def task2():

	# for each character in data-stream:
	for i in range(len(cont)):
		# Dont process first 13 characters
		if i < 13:
			continue

		# If last 14 chars all unique:
		char4 = ''
		for j in range(14):
			char4 += cont[i-j]
		
		distinct = len(Counter(char4))
		length = len(char4)
		if distinct == length:
			return i+1

	return -1


print(task1())

print(task2())
	


		