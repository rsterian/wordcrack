words1 = open('wordlist.txt', 'r')
words2 = open('americanenglish95.txt', 'r')
board = raw_input("Enter the letters left to right, top to bottom: ")

def findpos(char, word):
	return [i for i, letter in enumerate(word) if letter == char]

def test(word, board, oldpos, index, done):
	boardpositions = findpos(word[index], board)
	if done:
		return True
	for x in boardpositions:
		if adjacent(oldpos, x):
			newboard = list(board)
			newboard[x] = '#'
			"".join(newboard)
			if(index + 2 == len(word)):
				done = True

			done = test(word, newboard, x, index + 1, done)
		if done:
			return True
	
	return False;



def adjacent(pos1, pos2):
	#first letter
	if (pos1 == -1):
		return True

	#up/down
	if ((pos2 == pos1 + 4) or (pos2 == pos1 - 4)):
		return True

	#check left and right edges
	if (pos1 % 4) == 0:
		if ((pos2 == pos1 + 1) or (pos2 == pos1 + 5) or (pos2 == pos1 - 3)):
			return True
		else:
			return False
	if (pos1 % 4) == 3:
		if ((pos2 == pos1 - 1) or (pos2 == pos1 - 5) or (pos2 == pos1 + 3)):
			return True
		else:
			return False

	#left/right
	if ((pos2 == pos1 + 1) or (pos2 == pos1 - 1)):
		return True

	#upleft/upright
	if ((pos2 == pos1 - 5) or (pos2 == pos1 - 3)):
		return True

	#downleft/downright
	if ((pos2 == pos1 + 5) or (pos2 == pos1 + 3)):
		return True

	return False

foundwords = []

for word in words1:
	if test(word, board, -1, 0, False):
		foundwords.append(word[:-1])
for word in words2:
	if test(word, board, -1, 0, False):
		foundwords.append(word[:-1])

print sorted(list(set(foundwords)), key=len, reverse=True)