from queue import *
from hashlib import *
from treelib import *
from src.tree_proc import *


# Get Path to Goal Node
def get_path(p_tree: Tree, goal_node: Node):
    # Maybe Node is Null or Some Shit Like That! :D...
    try:
        # Define Path List!
        path = []
        # Define Last Checked Node!
        node = goal_node
        # Go Up on Tree While See the Root!
        while node:
            # Add Action (Node's Tag) to Path List!
            path.append(node.tag)
            # Go Up!
            node = p_tree.parent(node.identifier)
        # Return Reversed Path List (Because of Path List is from Down to Up)!
        return path[::-1]
    # :D...
    except:
        return []


# IDS Searching Algorithm
def IDS(t_map, initial_state, min_cut_off, max_cut_off, ignore_revisit=False):
    # Build Search Tree for Solving Algorithm!
    p_tree = build_tree(initial_state)
    # Start from Min Cutoff Value and Increase Cutoff to Max Cutoff!
    for cut_off in range(min_cut_off, max_cut_off):
        # Create Frontier Stack!
        stack = [p_tree.get_node(p_tree.root)]
        # Create Visited List!
        visited_states = set()
        # Search until Frontier List Going Empty!
        while stack:
            # Pop from Frontier List!
            node = stack.pop()
            print(node)
            # Check the Request for Ignore Visited States or Not!
            if ignore_revisit:
                # Add Hashed Node Data to Revisited List!
                hashed_node = sha256(str(node.data).encode('utf-8')).hexdigest()
                # Ignote Revisited States!
                if hashed_node in visited_states:
                    continue
                visited_states.add(hashed_node)
            # Check if Depth Cutoff Parameter Exceeded!
            if p_tree.depth(node) >= cut_off:
                continue
            # Expand Current Node!
            expand_node(p_tree, t_map, node)
            # Iterate Node's Child List and Add Them to Frontier Stack!
            for child in p_tree.children(node.identifier):
                stack.append(child)
                # Check if We Succeed! ^___^
                if child.data['done']:
                    # print('Pariya')
                    print(f'Pariya || {p_tree.size()}')
                    return p_tree, child
    return p_tree, False


# Bi-Directional Searching Algorithm
def BBFS(t_map, initial_state):
    # Build Search Tree from Initial State!
    p_tree = build_tree(initial_state)
    # Make an Example Goal State!
    goal_state = make_goal_state(t_map, initial_state)
    # Build Search Tree from Goal State!
    m_tree = build_tree(goal_state)
    # Build Frontier Queue (for Forward Tree)!
    queue_forw = Queue()
    # Build Frontier Queue (for Backward Tree)!
    queue_back = Queue()
    # Build Visited List (for Forward Tree)!
    visited_states_forw = set()
    # Build Visited List (for Backward Tree)!
    visited_states_back = set()
    # Add Root of Tree to Frontier (for Forward Tree)!
    queue_forw.put(p_tree.get_node(p_tree.root))
    # Add Root of Tree to Frontier (for Backward Tree)!
    queue_back.put(m_tree.get_node(m_tree.root))
    # Search until Frontier List(s) Going Empty!
    while queue_forw or queue_back:

        # ~~~~~~~~~~~   Forward Tree Expansion!  ~~~~~~~~~~~

        # Check if Forward Frontier Queue is Empty!
        if queue_forw.qsize() == 0:
            return False, False, False, False
        # Get Top of Frontier Queue (Forward Tree)!
        node = queue_forw.get()
        print(node)
        # Check and Ignore Revisited States
        str_data_list = [str(pmd.data) for pmd in visited_states_forw]
        if str(node.data) not in str_data_list:
            # Expand Node and Add to The Visited Set!
            visited_states_forw.add(node)
            expand_node(p_tree, t_map, node)
            # Check and Add Child(s) to the Frontier Queue!
            for child in p_tree.children(node.identifier):
                # Check if We Succeed! ^___^
                if child.data['done']:
                    # print('Pariya')
                    print(f'Pariya || {p_tree.size()}')
                    return p_tree, False, child, False
                queue_forw.put(child)

        # ~~~~~~~~~~~   Backward Tree Expansion!  ~~~~~~~~~~~

        # Check if Backward Frontier Queue is Empty!
        if queue_back.qsize() == 0:
            continue
        # Get Top of Frontier Queue (Backward Tree)!
        node = queue_back.get()
        print(node, 63)
        # Check and Ignore Revisited States!
        str_node = str(node.data)
        str_data_list = [str(pmd.data) for pmd in visited_states_forw]
        # Check if We Succeed! ^___^
        if str_node in str_data_list:
            mid_forw_node = list(visited_states_forw)[str_data_list.index(str_node)]
            mid_back_node = node
            print(f'Pariya || {p_tree.size() + m_tree.size()}')
            return p_tree, m_tree, mid_forw_node, mid_back_node
        # Ignore Revisited States!
        # if str_node in visited_states_back:
        #    continue
        # Expand Node and Add to The Visited Set!
        visited_states_back.add(str_node)
        expand_node(m_tree, t_map, node, backward=True)
        # Check and Add Child(s) to the Frontier Queue!
        for child in m_tree.children(node.identifier):
            queue_back.put(child)

