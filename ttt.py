#calculate the next move so long as the game has valid moves left
def nextMove(board, freespaces):
	for x in range(1, freespaces):
		return 0


#calculate if a winner has been determined at this point
def over(board, freespaces):
	if(freespaces == 0):
		return True
	else:
		x = 0
		for x in range(0,2):
			for y in range(0,2):
				if board[x][y] == 0:
					break
				elif board[x][y] == board[x][y+1]:
					if(board[x][y] == board[x][y+2]):
						return True
				elif board[x][y] == board[x+1][y+1]:
					if board[x][y] == board[x+2][y+2]:
						return True

def main():
	rows, cols = (3, 3) 
	board = [[0]*cols]*rows
	board[2][0] = 1
	board[2][1] = 1
	board[2][2] = 1
	print(over(board,99))

if __name__ == "__main__":
	main()