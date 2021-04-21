from state_tree import StateTree
from print_matrix import print_matrix
from identify_places import identify_places
from hashlib import sha256




def IDS(state_tree:StateTree, depth):
    stack = [state_tree.tree.get_node(state_tree.tree.root)]
    visited = set()
    while stack:
        node = stack.pop()
        hashed_mat = sha256(str(node.data.matrix).encode('utf-8')).hexdigest()
        if hashed_mat in visited:
            continue
        visited.add(hashed_mat)
        if node.data.success():
            return node
        if state_tree.tree.depth(node) >= depth:
            continue
        state_tree.add_child_move_nodes(node)
        for child in state_tree.get_childs(node.identifier):
            stack.append(child)


def get_path(state_tree, node):
    stack = []
    path = []
    while node is not None:
        stack.append(node.tag)
        node = state_tree.tree.parent(node.identifier)
    for i in range(stack.__len__()):
        path.append(stack.pop())
    return path
