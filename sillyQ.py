import AIClass
import copy
import random

class sampleAI(AIClass.AI):
	prevBoard = ""
	def makeMove(self, board):
		if(self.prevBoard == ""):
			self.dropMarker(board,random.randint(0,6))
		else:
			lastMove = self.findLastMove(board)
			if(lastMove == 0 or lastMove == -1):
				self.dropMarker(board, 0)
			else:
				self.dropMarker(board, random.randint(0,6))
		self.prevBoard = copy.deepcopy(board)
	def findLastMove(self, board):
		self.printBoard(board)
		self.printBoard(self.prevBoard)
		i = 0
		while(i<6):
			j = 0
			while(j<7):
				if(board[j][i] != self.prevBoard[j][i]):
					return j
				j += 1
			i += 1
		return -1
	def findWinSpots(self,board):
		checkResult = None
		for column in range (6):
			for row in range(5):
				if board[column][row] != '_':
					checkResult = triSpots(board,board[column][row], 'up',column,row)
					if checkResult != None:
						return checkResult
					checkResult = triSpots(board,board[column][row],'upRight',column,row)
					if checkResult != None:
						return checkResult
					checkResult = triSpots(board,board[column][row],'right',column,row)
					if checkResult != None:
						return checkResult
					checkResult = triSpots(board,board[column][row],'downRight',column,row)
					if checkResult != None:
						return checkResult
					checkResult = triSpots(board,board[column][row],'down',column,row)
					if checkResult != None:
						return checkResult
					checkResult = triSpots(board,board[column][row],'downLeft',column,row)
					if checkResult != None:
						return checkResult
					checkResult = triSpots(board,board[column][row],'left',column,row)
					if checkResult != None:
						return checkResult
					checkResult = triSpots(board,board[column][row],'upLeft',column,row)
					if checkResult != None:
						return checkResult
		return checkResult	
	
	def triSpots(self,board,pos,direction,x,y):
		xMod = 0
		yMod = 0
		distance = 1
		checked = False
		riskFound = False
		risk = None
		if direction == 'up':
			yMod = -1
		elif direction == 'upRight':
			yMod = -1
			xMod = 1
		elif direction == 'right':
			xMod = 1
		elif direction == 'downRight':
			yMod = 1
			xMod = 1
		elif direction == 'down':
			yMod = 1
		elif direction == 'downLeft':
			yMod = 1
			xMod = -1
		elif direction == 'left':
			xMod = -1
		elif direction == 'upLeft':
			yMod = -1
			xMod = -1
		while not checked:
			if y+(yMod*distance) < 0:
				checked = True
			if x+(xMod*distance) < 0:
				checked = True
			if x+(xMod*distance) > 6:
				checked = True
			if y+(yMod*distance) > 5:
				checked = True
			elif board[x+(xMod*distance)][y+(yMod*distance)] != piece:
				checked = True
			elif board[x+(xMod*distance)][y+(yMod*distance)] == piece:
				distance+=1
				if distance == 3:
					riskFound = True
					checked = True
		if winnerFound == True:
			if piece == 'x':
				risk = 'computer'
			elif piece == 'o':
				risk = 'player'
		return risk					