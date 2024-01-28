input = open("input.txt")
cont = input.read()


"""
cont = Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


ls = list(cont.split("\n\n"))
monkeys = []
itemsInspected = []

for monkey in ls:
	monkeyStuff = {}

	monkey = monkey.split('\n')

	monkeyStuff["items"] = monkey[1][18:].split(', ')
	monkeyStuff["operator"] = monkey[2][23]
	monkeyStuff["value"] = monkey[2][25:]
	monkeyStuff["divisibleBy"] = int(monkey[3][21:])
	monkeyStuff["ifTrue"] = int(monkey[4][29])
	monkeyStuff["ifFalse"] = int(monkey[5][30])

	monkeys.append(monkeyStuff)
	itemsInspected.append(0)
	
print(monkeys)

# Get product of divisible by
prodDivs = 1
for i in range(len(monkeys)):
	prodDivs = prodDivs*monkeys[i]["divisibleBy"]


def calculator(operation, a, b):
	a = int(a)
	b = int(b)
	if operation == '+':
		return a+b
	elif operation == '*':
		return a*b

# inspecting an item
def inspectItem(monkeyNum):
	# Get item to inspect
	worryLevel = monkeys[monkeyNum]["items"][0]

	# calculate new worry level
	if 'old' in monkeys[monkeyNum]["value"]:
		worryLevel = calculator(monkeys[monkeyNum]["operator"], worryLevel, worryLevel)
	else:
		worryLevel = calculator(monkeys[monkeyNum]["operator"], worryLevel, monkeys[monkeyNum]["value"])

	# Task 1
	# worryLevel = worryLevel//3

	# Task 2
	worryLevel = worryLevel%prodDivs


	# Check which monkey to trow to
	if worryLevel%monkeys[monkeyNum]["divisibleBy"] == 0:
		destMonkey = monkeys[monkeyNum]["ifTrue"]
	else:
		destMonkey = monkeys[monkeyNum]["ifFalse"]

	# Trow item
	monkeys[monkeyNum]["items"].pop(0)

	monkeys[destMonkey]["items"].append(worryLevel)

# Do a round
def doRound():
	for monkeyNum in range(len(monkeys)):
		for itemNum in range(len(monkeys[monkeyNum]["items"])):
			inspectItem(monkeyNum)
			itemsInspected[monkeyNum] += 1

# Task 1 and 2
def task1():

	# 20 for task 1, 10000 for task 2
	for i in range(10000):
		if i == 1 or i == 20 or i == 1000 or i == 2000:
			print(i)
		doRound()
	
	first = 0
	second = 0

	for monkeyInspects in itemsInspected:
		if monkeyInspects > first:
			second = first
			first = monkeyInspects
		elif monkeyInspects > second:
			second = monkeyInspects

	return first*second

# Task 2
def task2():
	pass


print(task1())

print(task2())
	


		