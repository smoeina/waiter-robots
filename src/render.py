from game2dboard import Board
from src.pre_proc import *


class Visualize():

    def __init__(self, t_map, state, path:list):
        self.t_map = t_map
        self.state = state
        self.path = path[1:]
        self.start = False
        self.depth = len(path)
        self.cost = 0
        self.board = Board(len(t_map), len(t_map[0]))
        self.board.on_timer = self.ontimer
        self.board.on_key_press = self.onkey
        self.board.start_timer(630)

    def ontimer(self):
        if len(self.path) == 0:
            print(f"Answer's Depth: {self.depth}")
            print(f"Answer's Cost: {self.cost}")
            exit(0)
        if  not self.start:
            return
        self.board.clear()
        self.action = self.path[0]
        del self.path[0]
        self.state = act(self.t_map, self.state, self.action)

        # Update Path Cost!
        self.cost += eval(self.t_map[self.state['bot'][1]][self.state['bot'][0]])

        for y, row in enumerate(self.t_map):
            for x, cell in enumerate(row):
                if 'x' in cell:
                    self.board[y][x] = 'x'

        self.board[self.state['bot'][1]][self.state['bot'][0]] = 'r'
        for b_x, b_y in self.state['butters']:
            self.board[b_y][b_x] = 'b'
        for g_x, g_y in self.state['goals']:
            self.board[g_y][g_x] = 'g'

    def onkey(self,key):
        if key == "Return":
            self.start = True

    def render(self):
        self.board.show()
