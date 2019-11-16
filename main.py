####################################################
# You may only change the initial board here       #
# Any change other than board may result in crash  #
####################################################

from gui import App
from PyQt5.QtWidgets import QApplication
import sys
import chess

if __name__ == '__main__':
	app = QApplication(sys.argv)
	# board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1") #initial board is created here
	board = chess.Board("8/5K1k/8/8/8/8/8/6Q1 w - - 0 1")
	ex = App(board)
	app.exec_()
