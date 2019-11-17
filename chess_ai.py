import chess
import random
from threading import Lock, Thread
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
	# Program works with both minimax_ai_play and alpha_beta_minimax
	
	print("Thinking...")
	# play = minimax_ai_play(board, 5, get_turn(board))
	play = alpha_beta_minimax(board, 5, negative_infinity(), positive_infinity(), get_turn(board))[1]
	print("Thinking Finished...")
	
	print("Played move:" + play)
	return play

def get_turn(board):
	if(board.fen().split(" ")[1] == "w"):
		return True
	return False

def minimax_ai_play(board, depth, maximizingPlayer):
	# This approach prefered because I can easily split work to 
	# different threads

	max_val = negative_infinity()
	min_val = positive_infinity()

	index = 0
	
	candidate_moves = list(board.legal_moves)

	# includes values heuristic values for play0 in 0th index
	moves_calculated = []

	count = 0
	for play in board.legal_moves:
		play_move(board, play)
		# print("---------------------")
		# print(play)
		value = minimax(board, depth - 1, get_turn(board))
		# print(value)
		# print("---------------------")
		unmake_last_move(board)

		if(maximizingPlayer):
			if(value > max_val):
				max_val = value
				index = count
		else:
			if(value < min_val):
				min_val = value
				index = count
			
		moves_calculated.append(value)
				
		count += 1

	# Randomizing the best alternatives
	choosen = []
	for move in range(len(moves_calculated)):
		if(moves_calculated[index] == moves_calculated[move]):
			choosen.append(move)

	index = choosen[random.randint(0, len(choosen) - 1)]

	return str(candidate_moves[index])

def play_move(board, move):
	move_to_play = chess.Move.from_uci(str(move))
	if(board.is_legal(move_to_play)):
		board.push(move_to_play)
		return str(move)
	else:
		raise ValueError("Illegal Move")

def unmake_last_move(board):
	return board.pop()

def alpha_beta_minimax(board, depth, alpha, beta, maximizingPlayer):
	# It can work faster with proper move ordering
	if(depth == 0 or is_terminal_node(board)):
		return heuristic_value(board, depth), -1
	if(maximizingPlayer):
		value = negative_infinity()
		move = 0

		for play in board.legal_moves:
			candidate_move = play_move(board, play) # child board

			candidate_value = alpha_beta_minimax(board, depth - 1, alpha, beta, get_turn(board))[0]
			if(value < candidate_value):
				value = candidate_value
				move = candidate_move
			

			# value = max(value, alpha_beta_minimax(board, depth - 1, alpha, beta, get_turn(board)))
			unmake_last_move(board)

			alpha = max(alpha, value)
			if(alpha >= beta):
				break # beta cut-off
		return value, move
	else:
		value = positive_infinity()
		move = 0

		for play in board.legal_moves:
			candidate_move = play_move(board, play) # child board

			candidate_value = alpha_beta_minimax(board, depth - 1, alpha, beta, get_turn(board))[0]
			if(value > candidate_value):
				value = candidate_value
				move = candidate_move


			# value = min(value, alpha_beta_minimax(board, depth - 1, alpha, beta, get_turn(board)))
			unmake_last_move(board)

			beta = min(beta, value)
			if(alpha >= beta):
				break # alpha cut off
		return value, move

def minimax(board, depth, maximizingPlayer):
	if(depth == 0 or is_terminal_node(board)):
		return heuristic_value(board, depth)
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

def heuristic_value(board, depth):
	board_state = board.fen().split()[0]

	pieces = ["Q", "R", "B", "N", "P"]
	coefficents = [900, 500, 300, 300, 100]
	
	heuristic_result = 0.0

	for piece, coefficent in zip(pieces, coefficents):
		white_count = board_state.count(piece)
		black_count = board_state.count(piece.lower())

		heuristic_result += coefficent * (white_count -  black_count)

	if(board.is_checkmate()):
		if(get_turn(board)):
			heuristic_result -= (20000 + 2 ** depth)
		else:
			heuristic_result += (20000 + 2 ** depth)

	
	heuristic_result += 1 * calculate_mobilility(board)
	return heuristic_result

def calculate_mobilility(board):
	white_mobility = 0
	black_mobility = 0
	if(get_turn(board)):
		# White Turn
		white_mobility = board.legal_moves.count()
		board.turn = chess.BLACK
		black_mobility = board.legal_moves.count()
		board.turn = chess.WHITE
	else:
		# Black Turn
		black_mobility = board.legal_moves.count()
		board.turn = chess.WHITE
		white_mobility = board.legal_moves.count()
		board.turn = chess.BLACK
		
	return white_mobility - black_mobility

def positive_infinity():
	return float("inf")

def negative_infinity():
	return float("-inf")
