"""input = open("input.txt")
cont = input.read()


"""
cont = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
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

		valves[id] = [id, flow_rate, leads_to]

	print(valves)

	global valves_to_open_base
	valves_to_open_base = []

	for valve in valves.values():
		if valve[1] != 0:
			valves_to_open_base.append(valve[0])


# ----------------
def calc_shortest_routes_from_valve(valve_id):

	distance_from_start = {
		valve_id: [valve_id, 0, valve_id]
	}
	valves_to_visist = [valve_id]

	# While there are more paths to evaluate
	while len(valves_to_visist) != 0:
		valve_to_visist = valves_to_visist[0]

		# Go trough each neighbour, find if new smallest distance and if so save this as previous step and add this valve to valves_to_visist
		for neighbour in valves[valve_to_visist][2]:
			distance_to_neighbour = distance_from_start[valve_to_visist][1]+1

			# check if new smallest distance
			if neighbour not in distance_from_start or distance_to_neighbour < distance_from_start[neighbour][1]:
				distance_from_start[neighbour] = [neighbour, distance_to_neighbour, valve_to_visist]

				valves_to_visist.append(neighbour)

		
		# after all neighbours visisted, remove from valves_to_visist
		valves_to_visist.remove(valve_to_visist)

	return distance_from_start

def calc_expected_return(flow_rate, distance, minutes_remaning):
	minutes_remaning = minutes_remaning - distance - 1

	return flow_rate*minutes_remaning

def find_path_to_start_from_valve(distance_from_start, valve_id):
	path = [valve_id]

	while True:
		# If only 1 away from the origin, we have found the path
		if distance_from_start[valve_id][1] == 1:
			return path
		
		next_valve = distance_from_start[valve_id][2]
		path.append(next_valve)
		valve_id = next_valve


# Creates path which short term prioritize flow rate
# For one valve, 
#   open it (if it should be) 
#   then try to go to best valve
# when time has run out, or no more valves to open, finish path
#
# Path structure: [valve, 0/1 (if openend)], [valve, ...] ...
def create_path(valve, time_remaning, valves_to_open, goal, path):

	# If all nodes have been opened or time has run out
	if len(valves_to_open) == 0 or time_remaning <= 0:
		return path

	# If we need to move to new valve
	if len(goal) > 1:
		# remove current valve from path to new valve
		goal.pop(0)
		# save current move to path, and add time elapsed
		path.append([valve[0], 0])
		time_remaning -= 1
		# Go to next valve 
		create_path(valves[goal[0]], time_remaning, valves_to_open, goal, path)

	# If node should be opened
	if valve[0] in valves_to_open:
		path.append([valve[0], 1])
		time_remaning -= 1
		valves_to_open.remove(valve[0])


	# Calculate shortest route to each valve
	distance_from_valve = calc_shortest_routes_from_valve(valve[0])


	max_expected_return = 0
	next_valve = ''
	# Go through each valve, calculate expected return, save highest exprected return if not already opened
	for valve_dis in distance_from_valve.values():

		# Check if valve is already opened
		if valve_dis[0] not in valves_to_open:
			continue

		# calculate expected return if we go to valve and open it
		expected_return = calc_expected_return(valves[valve_dis[0]][1], valve_dis[1], time_remaning)

		# if we find new best return
		if expected_return > max_expected_return:
			max_expected_return = expected_return
			next_valve = valve_dis[0]

	# Find path to reach valve
	goal = find_path_to_start_from_valve(distance_from_valve, next_valve)

	# Go to next valve with destination valve as goal					
	# save current move to path, and add time elapsed
	path.append([valve[0], 0])
	time_remaning -= 1
	# Go to next valve 
	create_path(valves[goal[0]], time_remaning, valves_to_open, goal, path)


setup()

# Task 1
def task1():
	return create_path(valves['AA'], 30, valves_to_open_base, ['AA'], [])	
	

# Task 2
def task2():
	pass


print(task1())

print(task2())
	

