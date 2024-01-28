from collections import Counter

input = open("input.txt")
cont = input.read()


"""
cont = $ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


ls = list(cont.split("\n"))
ls.remove("")

cd = []
filesystem = {}

# Add file to directory 
def addFileToDir(curDir, path, file):

	# Have reached the directory
	if len(path) == 0: 
		
		obj = file.split(' ')
		
		# if file, add to dir
		if obj[0] != 'dir':
			curDir[obj[1]] = int(obj[0])

		# if dir, add empty map
		else:
			curDir[obj[1]] = {}


	# Go one dir deeper: 
	else:
		# Get name of next directory
		nextDir = path[0]
		# Remove next directory
		path.pop(0)

		# Go to next directory and add file
		addFileToDir(curDir[nextDir], path, file)



# Create filesystem
def createFilesystem():
	# Execute each command
	for command in ls:
		
		# check if command cd
		if '$ cd' in command:
			# Change directory based on argument:
			if '..' in command:
				cd.pop()
			elif '/' in command:
				cd.clear()
			else:
				cd.append(command.split(' ')[2])

		# Ignore ls
		elif '$ ls' in command:
			continue

		# File or directory
		else:
			# Add file to current directory
			addFileToDir(filesystem, cd.copy(), command)

createFilesystem()
print(filesystem)

dirSizes = {}

# Calculate size of directory
def calcSizeDir(path, name, dir):
	path.append(name)
	size = 0
	# For each item in the dir
	for key, value in dir.items():
		# If the item is a file
		if isinstance(value, int):
			size += value

		# If it is a directory
		else:
			size += calcSizeDir((path.copy()), key, value)

	# Try to save the dir size 
	if str(path) not in dirSizes:
		dirSizes[str(path)] = size

	# Return the size of the dir
	return size


# Task 1
def task1():

	totalSize = 0

	# Calculate and save the size of all directories 
	calcSizeDir([], '/', filesystem)

	# Calculate sum of all dirs with size at most 100 000
	for value in dirSizes.values():
		if value <= 100000:
			totalSize += value

	return totalSize

# Task 2
def task2():

	# Calculate the space we need to delete
	totalSpace = 70000000
	reqSpace = 30000000
	unused = totalSpace - dirSizes["[\'/\']"]
	needToDelete = reqSpace - unused


	# Initialize smallestDir found
	smallestDirToDelete = 100000000000

	# For all dirs
	for size in dirSizes.values():

		# If the directory is big enough to free up required space, and is the smallest found, save the size
		if size >= needToDelete and size < smallestDirToDelete:
			smallestDirToDelete = size


	return smallestDirToDelete


print(task1())

print(task2())
	


		