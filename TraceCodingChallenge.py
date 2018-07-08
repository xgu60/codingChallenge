#Coding Challenge
#By Xiaodong Gu

#QUESTION
#Prompt: Write a function that takes the input, gives the output, and meets the conditions below.
#Input: An N x M matrix of a garden. Each cell contains an integer representing the number of carrots
#in that part of the garden.
#Output: The number of carrots Bunny eats before falling asleep.
#Conditions: Bunny starts in the center of the garden. If there are more than one center cell, 
#Bunny starts in the cell with the largest number of carrots. There will never be a tie for the 
#highest number of carrots in a center cell. Bunny eats all of the carrots in his cell,
#then looks left, right, up, and down for more carrots. 
#Bunny always moves to the adjacent cell with the highest carrot count. 
#If there are no adjacent cells with carrots, Bunny falls asleep.
#Example test case in python: 
#>>> garden1 = [[5, 7, 8, 6, 3],
#               [0, 0, 7, 0, 4],
#               [4, 6, 3, 4, 9],
#               [3, 1, 0, 5, 8]]
#>>> eat(garden1)
#27  # starts at garden[1][2] = 7, eats 7 carrots, looks at the 8, 0, 3, and 0 adjacent, moves to the 8, repeat.


def eat(garden):
	#special case check
	if garden == None or len(garden) == 0 or len(garden[0]) == 0:
		return 0
	#find the center of garden
	centerCell = findCenter(garden)
	#store the number of carrots eaten in each cell
	carrots = []
	#recursively eat carrots in cells
	eatCarrots(garden, centerCell, carrots)
	return sum(carrots)

def findCenter(garden):
	rows = len(garden)
	cols = len(garden[0])	
	#check if rows is a even number
	if (rows % 2 == 0):
		centerRows = [int(rows / 2) - 1, int(rows / 2)]
	else:
		centerRows = [int(rows / 2)]
	#check if cols is a even number
	if (cols % 2 == 0):
		centerCols = [int(cols / 2) - 1, int(cols / 2)]
	else:
		centerCols = [int(cols / 2)]	
	#get all center cells
	#use a tuple to store cell information (row, col)
	centerCells = []
	for i in centerRows:
		for j in centerCols:
			centerCells.append((i, j))
	#find the center cell with max carrots
	return findCellWithMaxCarrots(garden, centerCells)
	
def findCellWithMaxCarrots(garden, cells):
	#find the cell has max carrots in the provided list of cells
	#assume the initial max carrots as 0
	maxCarrots = 0
	#use a tuple (i, j) to store cell information (row, col)
	#if no qualified cell found, set as -1
	maxCell = -1
	for cell in cells:
		#use to handle edge case, assume out side of boundaries carrots nums as 0
		if cell[0] < 0 or cell[0] >= len(garden) or cell[1] < 0 or cell[1] >= len(garden[0]):
			continue
		if (garden[cell[0]][cell[1]] > maxCarrots):
			maxCarrots = garden[cell[0]][cell[1]]
			maxCell = cell	
	return maxCell
				
				
def eatCarrots(garden, cell, carrots):
	#if cannot find a cell to eat carrot	
	if cell == -1:
		return
	#record the nums of carrots eaten, and set the cell to 0
	carrots.append(garden[cell[0]][cell[1]])
	garden[cell[0]][cell[1]] = 0
	#find the next cell to eat
	adjCells = [(cell[0] - 1, cell[1]), 
			    (cell[0], cell[1] - 1),
				(cell[0] + 1, cell[1]),
			    (cell[0], cell[1] + 1)]	
	newCell = findCellWithMaxCarrots(garden, adjCells)	
	eatCarrots(garden, newCell, carrots)
	
           
if __name__ == "__main__":
	garden1 = [[5, 7, 8, 6, 3],
               [0, 0, 7, 0, 4],
               [4, 6, 3, 4, 9],
			   [3, 1, 0, 5, 8]]
	print("Bunny eats {} carrots in garden1".format(eat(garden1)))
	
	garden2 = [[8]]
	print("Bunny eats {} carrots in garden2".format(eat(garden2)))
	
	garden3 = []
	print("Bunny eats {} carrots in garden3".format(eat(garden3)))
	
	garden4 = None
	print("Bunny eats {} carrots in garden4".format(eat(garden4)))
	
	garden5 = [[5, 7],
               [0, 0]]
	print("Bunny eats {} carrots in garden5".format(eat(garden5)))
		   


				
	
	