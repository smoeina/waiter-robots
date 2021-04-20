from identify_places import identify_places
from move import move
from print_matrix import print_matrix
from read_input import read_input
from state_tree import StateTree
from IDS import *
if __name__ == "__main__":
    matrix = read_input("input/test63.txt")
    state_tree = StateTree(matrix)
    #IDS(state_tree,3)
    pm = IDS(state_tree,5)
    while pm is not None:
        print(pm.tag)
        print("_____________")
        print("_____________")
        pm = state_tree.tree.parent(pm.identifier)

    # for m in pm:
    #     print_matrix(m.data.matrix)
    #     print('PMPMPMPMPMPMPMP')
    #     print('PMPMPMPMPMPMPMP')

    #mat, val = move(matrix,identify_places(matrix),'up',0)
    #print_matrix(mat)

    # state_tree.add_child_move_nodes(state_tree.tree.get_node('initial_node'))
    # for child in state_tree.get_childs('initial_node'):
    #     print_matrix(child.data.matrix)
    #     print()
    #     print()
