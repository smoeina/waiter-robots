from game2dboard import Board
import time
from state_tree import StateTree
from move import move
from identify_places import identify_places


class Visualize():

    def __init__(self, matrix, path:list):
        self.matrix = matrix
        self.path = path
        self.start = False
        self.board = Board(len(matrix), len(matrix[0]))
        self.board.on_timer = self.ontimer
        self.board.on_key_press = self.onkey
        self.board.start_timer(630)

    def ontimer(self):
        if len(self.path) == 0 or not self.start:
            return
        self.board.clear()
        #print(self.path)
        turn = self.path[0]
        del self.path[0]
        self.matrix, _ = move(self.matrix, identify_places(self.matrix), turn, 0)

        for y, row in enumerate(self.matrix):
            for x, cell in enumerate(row):
                if 'x' in cell:
                    self.board[y][x] = 'x'
                if 'b' in cell:
                    self.board[y][x] = 'b'
                if 'p' in cell:
                    self.board[y][x] = 'p'
                if 'r' in cell:
                    self.board[y][x] = 'r'

    def onkey(self,key):
        if key == "Return":
            self.start = True

    def render(self):
        self.board.show()
