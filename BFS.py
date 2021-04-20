from state_tree import StateTree


def IDS(state_tree,depth):
    for i in range(depth):
        nodes = state_tree.get_node_of_same_depth(i)
        for node in nodes:
            print(node.data.get_validity())
            if node.data.get_validity() ==True:
                state_tree.add_child_move_nodes(node)

    state_tree.show()