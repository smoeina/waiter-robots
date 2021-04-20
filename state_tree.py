from treelib import Tree

from identify_places import identify_places
from move import move


class State(object):
    def __init__(self, matrix, validity):
        self.matrix = matrix
        self.validity = validity

    def set_state(self, matrix):
        self.matrix = matrix
        return True

    def get_state(self):
        return self.matrix

    def get_validity(self):
        return self.validity

    def success(self):
        places = identify_places(self.matrix)
        successful = True
        for butter_place in places['butters']:
            if butter_place not in places['aims']:
                successful = False
        return successful


class StateTree(object):
    def __init__(self, initial_matrix):
        self.tree = Tree()
        self.tree.create_node("initial_node", "initial_node", data=State(initial_matrix, True))

    def add_node_with_parent_tag(self, parent_tag, turn):
        parent_node = self.tree.get_node(parent_tag)
        previous_matrix = parent_node.data.get_state()
        places = identify_places(previous_matrix)
        matrix, validity = move(previous_matrix, places, turn, 0)
        self.tree.create_node(self.tree.size() + 1, self.tree.size() + 1, parent=parent_node,
                              data=State(matrix, validity))

    def add_node(self, parent_node, turn):
        previous_matrix = parent_node.data.get_state()
        places = identify_places(previous_matrix)
        matrix, validity = move(previous_matrix, places, turn, 0)
        print(validity)
        if turn == 'down':
            self.tree.create_node(self.tree.size() + 1, self.tree.size() + 1, parent=parent_node,
                                  data=State(matrix, validity))

    def add_child_move_nodes(self, parent_node):
        self.add_node(parent_node, 'up')
        self.add_node(parent_node, 'down')
        self.add_node(parent_node, 'right')
        self.add_node(parent_node, 'left')
        return True

    def get_node_of_same_depth(self, depth):
        return [node for node in self.tree.filter_nodes(lambda x: self.tree.depth(x) == depth)]

    def show(self):
        self.tree.show()
