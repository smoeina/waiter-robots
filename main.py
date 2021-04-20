from identify_places import identify_places
from move import move
from print_matrix import print_matrix
from read_input import read_input
from state_tree import StateTree
from IDS import IDS
if __name__ == "__main__":
    matrix = read_input("input/test1.txt")
    state_tree = StateTree(matrix)
    IDS(state_tree,3)
