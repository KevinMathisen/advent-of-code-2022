input = open("input.txt")
cont = input.read()

ls = list(cont.split("\n\n"))
#ls.remove("")

firstFood = 0
secondFood = 0
thirdFood = 0

for n in range(0,len(ls)):
	ls[n] = ls[n].split("\n")
	print(str(ls[n]))
	totalFood = 0
	for food in ls[n]:
		if food != '':
			totalFood += int(food)

	if totalFood > firstFood:
		firstFood = totalFood
	elif totalFood > secondFood:
		secondFood = totalFood
	elif totalFood > thirdFood:
		thirdFood = totalFood

print(str(firstFood+secondFood+thirdFood))	



input.close()