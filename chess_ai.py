import chess
import random

'''
	Your Code Will Come Here
'''

# this function should always be named as ai_play and
# this function's return value is used as AI's move so it will AI's your final decision.
# You can add as many function as you want to above.
# At each turn you will get a board to ai_play and calculate best move and return it.
# def ai_play(board):
# 	plays = []

# 	for play in board.legal_moves:
# 		plays.append(str(play))

# 	return plays[random.randint(0, len(plays)-1)] # here I only return random legal move to show an example


def ai_play(board):
	print("Thinking...")
	minimax_ai_play(board)
	print("Thinking Finished...")
	return "g1g2"

def get_turn(board):
	if(board.fen().split(" ")[1] == "w"):
		return True
	return False

def minimax_ai_play(board):
	max_val = 0

	for play in board.legal_moves:
		play_move(board, play)
		
		value = minimax(board, 4, get_turn(board))
	
		unmake_last_move(board)
	
def play_move(board, move):
	move_to_play = chess.Move.from_uci(str(move))
	if(board.is_legal(move_to_play)):
		board.push(move_to_play)
	else:
		raise ValueError("Illegal Move")

def unmake_last_move(board):
	return board.pop()

def minimax(board, depth, maximizingPlayer):
	if(depth == 0 or is_terminal_node(board)):
		return heuristic_value(board)
	if(maximizingPlayer):
		value = negative_infinity()
		
		for play in board.legal_moves:
			play_move(board, play) # child board
			value = max(value, minimax(board, depth - 1, get_turn(board)))
			unmake_last_move(board) # parent board
		return value
	else:
		value = positive_infinity()

		for play in board.legal_moves:
			play_move(board, play) # child board
			value = min(value, minimax(board, depth - 1, get_turn(board)))
			unmake_last_move(board) # parent board
		return value
		
def is_terminal_node(board):
	if(board.legal_moves.count() == 0):
		return True
	return False

def heuristic_value(board):
	return random.randint(5, 200)

def positive_infinity():
	return float("inf")

def negative_infinity():
	return float("-inf")
