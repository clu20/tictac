import unittest
from ttt import over

rows, cols = (3, 3) 
board = [[0]*cols]*rows

class testtic(unittest.TestCase):
	
	#0 moves leftover
	def test_a_gameover(self):
		self.assertTrue(over(board, 0))

	#Top row winner
	# 1|1|1
	# 0|0|0
	# 0|0|0
	def test_b_winner_TR(self):
		bboard = board
		i = 0
		while(i < 3):
			board[0][i] = 1
			i+=1
		self.assertTrue(over(bboard, 99))

	#second row winner
	# 0|0|0
	# 1|1|1
	# 0|0|0
	def test_b_winner_SR(self):
		bboard = board
		i = 0
		while(i < 3):
			board[1][i] = 1
			i+=1
		self.assertTrue(over(bboard, 99))

	#bottom row winner
	# 0|0|0
	# 0|0|0
	# 1|1|1
	def test_b_winner_BR(self):
		bboard = board
		i = 0
		while(i < 3):
			board[2][i] = 1
			i+=1
		self.assertTrue(over(bboard, 99))

	#First columm winner
	# 1|0|0
	# 1|0|0
	# 1|0|0
	def test_c_winner_FC(self):
		bboard = board
		i = 0
		while(i < 3):
			board[i][0] = 1
			i+=1
		self.assertTrue(over(bboard, 99))

	#second columm winner
	# 0|1|0
	# 0|1|0
	# 0|1|0
	def test_c_winner_SC(self):
		bboard = board
		i = 0
		while(i < 3):
			board[i][1] = 1
			i+=1
		self.assertTrue(over(bboard, 99))

	#lasr columm winner
	# 0|0|1
	# 0|0|1
	# 0|0|1
	def test_c_winner_LC(self):
		bboard = board
		i = 0
		while(i < 3):
			board[i][2] = 1
			i+=1
		self.assertTrue(over(bboard, 99))

	#Diagnol(A) winner
	# 1|0|0
	# 0|1|0
	# 0|0|1
	def test_D_winner_DA(self):
		bboard = board
		i = 0
		while(i < 3):
			board[i][i] = 1
			i+=1
		self.assertTrue(over(bboard, 99))

	#Diagnol(A) winner
	# 0|0|1
	# 0|1|0
	# 1|0|0
	def test_D_winner_DB(self):
		bboard = board
		i = 0
		while(i < 3):
			board[2-i][i] = 1
			i+=1
		self.assertTrue(over(bboard, 99))

	#Diagnol(A) winner with other player values
	# 2|0|1
	# 2|1|0
	# 1|0|2
	def test_E_winner_A(self):
		bboard = board
		i = 0
		while(i < 3):
			board[2-i][i] = 1
			i+=1
		board[0][0] == 2
		board[1][0] == 2
		board[2][2] == 2
		self.assertTrue(over(bboard, 99))

	#Diagnol(A) winner with other player values
	# 0|2|1
	# 0|1|0
	# 1|2|0
	def test_E_winner_B(self):
		bboard = board
		i = 0
		while(i < 3):
			board[2-i][i] = 1
			i+=1
		board[0][1] == 2
		board[2][1] == 2
		self.assertTrue(over(bboard, 99))



if __name__ == '__main__':
    unittest.main()