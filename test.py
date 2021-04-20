from treelib import Node, Tree
tree = Tree()
tree.create_node("Parry", "parry")  # root node
tree.create_node("Jane", "jane", parent="parry")
tree.create_node("Bill", "bill", parent="parry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Mary", "mary", parent="diane")
tree.create_node("Mark", "mark", parent="jane")
tree.show()
nodes = [node for node in tree.expand_tree()]
print(type(nodes[0]))
print(tree.children('parry'))


