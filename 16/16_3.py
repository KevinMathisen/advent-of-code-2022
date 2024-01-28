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
	if current_valve != 'AA':
		path.append([current_valve, minutes_remaning])
	
	
	#if minutes_remaning <= 2 or len(path) == len(valves_map):
	#	paths.append(path[:])

	#	if len(paths)%10000 == 0:
	#		print(len(paths))
	#	return 0
	
	end_of_line = True

	# Try to visist each possible valve which has not been visisted
	for valve in valves_map[current_valve].items():
		next_valve = valve[0]

		if any(next_valve in sublist for sublist in path):
			continue

		distance = valve[1]

		new_min_remaning = minutes_remaning-distance-1

		if new_min_remaning > 2:
			end_of_line = False
			create_possible_paths(next_valve, path[:], new_min_remaning)

	if end_of_line:
		paths.append(path[:])

		if len(paths)%10000 == 0:
			print(len(paths))
		return 0
	else:
		paths.append(path[:])

		if len(paths)%10000 == 0:
			print(len(paths))
		return 0

	#paths.append(path[:])


setup()
create_map()
create_possible_paths('AA', [], 26)
print(len(paths))

def calc_score_path(path):
	score = 0
	for valve in path:
		flow_rate = valves[valve[0]][0]
		minutes_remaning = valve[1]
		score += flow_rate*minutes_remaning

	return score


# Task 2
def task2():
	max_score = 0
	best_path = []
	# Find best possible path
	print('Finding best possible path -----------------------')
	for i in range(len(paths)):
		path = paths[i]
		score = calc_score_path(path)
		if score > max_score:
			max_score = score
			best_path = path
			print('New max score: '+str(max_score))
	
	print('Finding best possible remainder path -----------------------')
	max_elp_score = 0
	remainder_path = []
	# Find the best path elephant can then do
	for i in range(len(paths)):
		path = paths[i]
		# Check if path has no overlap with the best path
		overlap = False
		for valve in path:
			if any(valve[0] in sublist for sublist in best_path):
				overlap = True
		
		if overlap:
			continue

		score = calc_score_path(path)
		if score > max_elp_score:
			max_elp_score = score
			print('New max score remainder: '+str(max_elp_score))

	print('Finding best possible combined paths -----------------------')
	max_combined_score = 0
	# Find paths better than remainder path, and then find best pair, and then find if this is the best overall so far
	for i in range(len(paths)):
		if i%500 == 0:
			print('Calculating score for path number: '+str(i))
		path = paths[i]
		

		# Find if better
		score = calc_score_path(path)
		if score < max_elp_score:
			continue

		max_partner_score = 0
		# Go trough all possible partner paths over treshhold, choose best possible partner
		for j in range(len(paths)):
			path2 = paths[j]
			# Check if path has no overlap with the best path
			overlap = False
			for valve in path2:
				if any(valve[0] in sublist for sublist in path):
					overlap = True
					break
			
			if overlap:
				continue

			score2 = calc_score_path(path2)
			if score2 > max_partner_score:
				max_partner_score = score2


		# Check if this is the best pairing
		score_total = score + max_partner_score
		if score_total > max_combined_score:
			max_combined_score = score_total
			print('New max total score: '+str(max_combined_score))

	return max_combined_score



print(task2())
