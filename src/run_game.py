from src.render import *
from src.pre_proc import *
from src.tree_proc import *
from src.search_algos import *
import time

t_map, state = read_map(f'../input/test{input("Please Enter Test Number!    ")}.txt')

algorithm = input("IDS or BBFS or A*?! :D     ")

start_time = time.time()
if algorithm == 'IDS':
    p_tree, goal_node = IDS(t_map, state, 5, 30)
    path = get_path(p_tree, goal_node)
elif algorithm == 'BBFS':
    p_tree, m_tree, mid_forw_node, mid_back_node = BBFS(t_map, state)
    print(63,mid_forw_node)
    print(63,mid_back_node)
    path = get_path(p_tree, mid_forw_node) + get_path(m_tree, mid_back_node)[::-1][:-1]
elif algorithm == 'A*':
    p_tree, goal_node = A_Star(t_map, state)
    path = get_path(p_tree, goal_node)
    print(calculate_heuristic(goal_node.data) + goal_node.data['g_cost'])

if len(path) == 0:
    print("can't pass the butter!")
    exit(0)

for p in path:
    print(p)

end_time = time.time()

print(end_time - start_time)

vis = Visualize(t_map, state, path)
vis.render()
