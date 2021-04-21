from identify_places import identify_places
from move import move
from print_matrix import print_matrix
from read_input import read_input
from state_tree import StateTree
from IDS import *
from render_map import Visualize

if __name__ == "__main__":
    matrix = read_input("input/test63.txt")
    state_tree = StateTree(matrix)
    # IDS(state_tree,3)
    path = []
    p = 5
    while len(path) == 0 and p < 64:
        pm = IDS(state_tree, p)
        path = get_path(state_tree, pm)[1:]
        p += 1
    if len(path) > 0:
        print(len(path))
        md = Visualize(matrix, path)
        md.render()
    else:
        print("Nothing Found :(")

    # for m in pm:
    #     print_matrix(m.data.matrix)
    #     print('PMPMPMPMPMPMPMP')
    #     print('PMPMPMPMPMPMPMP')

    # mat, val = move(matrix,identify_places(matrix),'up',0)
    # print_matrix(mat)

    # state_tree.add_child_move_nodes(state_tree.tree.get_node('initial_node'))
    # for child in state_tree.get_childs('initial_node'):
    #     print_matrix(child.data.matrix)
    #     print()
    #     print()
