input = open("input.txt")
cont = input.read()


"""
cont = Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""


ls = list(cont.split("\n"))
ls.remove("")
	
def setup():
	global valves
	valves = {}

	for line in ls:
		line = line.split(' has flow rate=')	# Valve AA | 0; tunnels lead to valves DD, II, BB
		id = line[0][6:]

		line = line[1].split('; tunnel')				# 0 | s lead to valves DD, II, BB
		flow_rate = int(line[0])

		line = line[1].split(', ')				# s lead to valves DD|II|BB

		leads_to = []

		for valve in line:
			leads_to.append(valve[-2:])

		valves[id] = [flow_rate, leads_to]

	print(valves)

# ----------------
def calc_shortest_routes_from_valve(valve_id):

	distance_from_start = {
		valve_id: [0, valve_id]
	}
	valves_to_visist = [valve_id]

	# While there are more paths to evaluate
	while len(valves_to_visist) != 0:
		valve_to_visist = valves_to_visist[0]

		# Go trough each neighbour, find if new smallest distance and if so save this as previous step and add this valve to valves_to_visist
		for neighbour in valves[valve_to_visist][1]:
			distance_to_neighbour = distance_from_start[valve_to_visist][0]+1

			# check if new smallest distance
			if neighbour not in distance_from_start or distance_to_neighbour < distance_from_start[neighbour][0]:
				distance_from_start[neighbour] = [distance_to_neighbour, valve_to_visist]

				valves_to_visist.append(neighbour)

		
		# after all neighbours visisted, remove from valves_to_visist
		valves_to_visist.remove(valve_to_visist)

	return distance_from_start

def create_map():
	global valves_map
	valves_map = {}

	for valve in valves.items():
		
		valve_map = {}

		# check if valve is worth looking at aka has flow rate 0
		if valve[1][0] == 0 and valve[0] != 'AA':
			continue

		node_map = calc_shortest_routes_from_valve(valve[0])

		for valve_neighbour in node_map.items():
			# check if valve is worth looking at aka has flow rate 0, and is not the same
			if (valve_neighbour[0] == valve[0] or valves[valve_neighbour[0]][0] == 0):
				continue

			valve_map[valve_neighbour[0]] = valve_neighbour[1][0]
		
		valves_map[valve[0]] = valve_map

	print(valves_map)

paths = []

def create_possible_paths(current_valve, path, minutes_remaning):
	# Save current valve to path
	path.append([current_valve, minutes_remaning])
	
	
	if minutes_remaning <= 2 or len(path) == len(valves_map):
		paths.append(path[:])

		if len(paths)%10000 == 0:
			print(len(paths))
		return 0
	
	

	# Try to visist each possible valve which has not been visisted
	for valve in valves_map[current_valve].items():
		next_valve = valve[0]

		if any(next_valve in sublist for sublist in path):
			continue

		distance = valve[1]
		create_possible_paths(next_valve, path[:], minutes_remaning-distance-1)




setup()
create_map()
create_possible_paths('AA', [], 30)
print(len(paths))

def calc_score_path(path):
	score = 0
	for valve in path:
		flow_rate = valves[valve[0]][0]
		minutes_remaning = valve[1]
		score += flow_rate*minutes_remaning

	return score


# Task 1
def task1():
	max_score = 0
	
	for i in range(len(paths)):
		if i%25000 == 0:
			print(i)
		path = paths[i]
		score = calc_score_path(path)
		if score > max_score:
			max_score = score
			print('New max score: '+str(max_score))
		
	return max_score

# Task 2
def task2():
	pass


print(task1())

print(task2())
	

