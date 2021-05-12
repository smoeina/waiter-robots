from treelib import *
from src.pre_proc import *
from copy import *


def build_tree(initial_state):
    p_tree = Tree()
    p_tree.create_node("Root", "Initial State", None, data=initial_state)
    return p_tree


def expand_node(p_tree: Tree, t_map, parent_node: Node, heuristic=False, backward=False):
    # Do All Actions And Add New States to Tree!
    for aciton in ACTIONS:
        # Make a Copy of Parent Node State for BackUP!
        old_state = deepcopy(parent_node.data)
        new_state = move(t_map, old_state, aciton, backward)
        if new_state:
            # if Its Heuristic Search Estimate Cost ( h(n) + g(n) )!
            if heuristic:
                new_state['g_cost'] = calculate_cost(new_state, t_map, p_tree, parent_node)
            # Create Child Node!
            p_tree.create_node(aciton, p_tree.size(), parent_node.identifier, new_state)


def expand_back(p_tree: Tree, t_map, parent_node: Node):
    # Do All Actions And Add New States to Tree!
    for aciton in ACTIONS:
        # Make a Copy of Parent Node State for BackUP!
        old_state = deepcopy(parent_node.data)
        new_state = act_back(t_map, old_state, aciton)
        if new_state:
            p_tree.create_node(aciton, p_tree.size(), parent_node.identifier, new_state)


if __name__ == '__main__':
    build_tree("63")
