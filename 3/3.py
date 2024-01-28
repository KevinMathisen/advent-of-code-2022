input = open("input.txt")
cont = input.read()


"""
cont = vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

ls = list(cont.split("\n"))
ls.remove("")

def getPrio(char):
	if char.islower():
		prio = ord(char) - ord('a') + 1
	else:
		prio = ord(char) - ord('A') + 1 + 26

	return prio


# Task 1
def task1():
	sum = 0
	for rucksack in ls:
		commonItem = ''
		for item in rucksack[:int(len(rucksack)/2)]:
			for item2 in rucksack[int(len(rucksack)/2):]:
				if item == item2:
					commonItem = item
					break
			
			if commonItem != '':
				break

		sum += getPrio(commonItem)

	return sum

# Task 2
def task2():
	sum = 0
	for groupNum in range(int(len(ls)/3)):
		commonItem = ''
		for item1 in ls[groupNum*3]:
			for item2 in ls[groupNum*3+1]:
				if item1 == item2:
					for item3 in ls[groupNum*3+2]:
						if item1 == item3:
							commonItem = item1
							break
				
				if commonItem != '':
					break

			if commonItem != '':
				break

		sum += getPrio(commonItem)

	return sum

print(task1())

print(task2())
	


		