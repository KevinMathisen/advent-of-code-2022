input = open("input.txt")
cont = input.read()


"""
cont = Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""


ls = list(cont.split("\n"))
ls.remove("")
	
line_y = 2000000

def distance(x1, y1, x2, y2):
	return abs(x1-x2) + abs(y1-y2) 

def setup():
	global sensors
	global row
	global max_x
	global min_x
	global max_y
	global min_y
	max_x = 0
	min_x = 0
	max_y = 0
	min_y = 0

	sensors = []
	row = []

	for line in ls:
		sensor = []
		
		two = line.split(': closest beacon is at x=')
		two[0] = two[0].split(', y=')
		two[1] = two[1].split(', y=')

		sensor.append([int(two[0][0][12:]), int(two[0][1])])
		sensor.append([int(two[1][0]), int(two[1][1])])

		x1 = sensor[0][0]
		y1 = sensor[0][1]
		x2 = sensor[1][0]
		y2 = sensor[1][1]

		dis = distance(x1, y1, x2, y2)
		sensor.append(dis)

		if x1-dis < min_x:
			min_x = x1-dis
		if x1+dis > max_x:
			max_x = x1+dis
		if x2 < min_x:
			min_x = x2
		if x2 > max_x:
			max_x = x2
		if y1-dis < min_y:
			min_y = y1-dis
		if y1+dis > max_y:
			max_y = y1+dis
		if y2 < min_y:
			min_y = y2
		if y2 > max_y:
			max_y = y2

		

		sensors.append(sensor)

	max_x = 4000000
	min_x = 0
	max_y = 4000000
	min_y = 0

	for x in range(min_x, max_x+1):
		row.append([x, line_y, 0]) # 0 is no info, 1 is beacon, 2 is no possible beacon
	

setup()

# Task 1
def task1():

	for sensor in sensors:
		print("new sensor")

		# if the distance from the line to the sensor if longer than the length
		distance_to_line = distance(sensor[0][0], line_y, sensor[0][0], sensor[0][1])
		
		if distance_to_line > sensor[2]:
			continue

		distance_on_line = sensor[2] - distance_to_line
		min_x = sensor[0][0] - distance_on_line
		max_x = sensor[0][0] + distance_on_line


		for coordinate in row:

			# Check if any point in viewing coordinate
			if coordinate[0] < min_x or coordinate[0] > max_x:
				continue

			# Already marked as beacon
			if coordinate[2] == 1:
				continue

			# Check if there is a beacon at the coordinate
			elif coordinate[0] == sensor[1][0] and coordinate[1] == sensor[1][1]:
				coordinate[2] = 1
			
			# Check if there already has been decided no possible beacon
			elif coordinate[2] == 2:
				continue

			# check if there are no possible beacon based on sensor
			elif distance(sensor[0][0], sensor[0][1], coordinate[0], coordinate[1]) <= sensor[2]: 
				coordinate[2] = 2

	sum = 0
	for coordinate in row:
		if coordinate[2] == 2:
			sum += 1


	return sum



# Task 2
def task2():
	
	# for each line
	for y in range(min_y, max_y):

		if y%10000 == 0:
			print(y)

		ranges = []
		
		for sensor in sensors:

			
			distance_to_line = distance(sensor[0][0], y, sensor[0][0], sensor[0][1])
			
			# if the distance from the line to the sensor if longer than the length
			if distance_to_line > sensor[2]:
				continue

			# Calculate the overlap between the current line and the sensor
			distance_on_line = sensor[2] - distance_to_line
			min_x2 = sensor[0][0] - distance_on_line
			if min_x2 < 0:
				min_x2 = 0
			max_x2 = sensor[0][0] + distance_on_line
			if max_x2 > max_x:
				max_x2 = max_x

			# Save the overlap as a range
			ranges.append([min_x2, max_x2])

		# Check if need to combine
		if len(ranges) == 1:
			continue	

		# sort the ranges
		ranges.sort(key=lambda x: x[0])
		

		# Combine the ranges if they overlap
		i = 0
		while i < len(ranges)-1: 
			
			j = i+1

			while j < len(ranges):

				left1 = ranges[i][0]
				right1 = ranges[i][1]
				left2 = ranges[j][0]
				right2 = ranges[j][1]

				# if 2 inside 1
				if right2 <= right1: 
					ranges.pop(j)
				# if 2 overlaps at right side
				elif right1 >= left2-1:
					new_range = [left1, right2]
					ranges.pop(j)
					ranges.pop(i)

					ranges.insert(i, new_range)
				else:
					j += 1
					

			i += 1

		# More than 2 ranges; aka there is a gap where the beacon can be
		if len(ranges) >= 2:
			print(ranges)
			return ((ranges[0][1]+1)*4000000+y)

	return ranges


#print(task1())



print(task2())
	

