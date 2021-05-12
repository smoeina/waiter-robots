import enum
from treelib import *


class ACTIONS(enum.Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)


h, w = 0, 0


# Calculate Heuristic Function of a State!
def calculate_heuristic(state):
    # Define Heuristic Function h(n) = 0
    pmd = 0
    # Define Distance of the Robot and the Nearest Butter!
    min_dist_br = float('inf')
    for b_x, b_y in state['butters']:
        # Calculate Distance of the Robot and the Nearest Butter!
        dist_br = abs(state['bot'][0] - b_x) + abs(state['bot'][1] - b_y)
        if dist_br < min_dist_br:
            min_dist_br = dist_br
        # Define Distance of each Butter and the Nearest Goal!
        min_dist_bg = float('inf')
        # Calculate Distance of each Butter and the Nearest Goal!
        for g_x, g_y in state['goals']:
            dist_bg = abs(g_x - b_x) + abs(g_y - b_y)
            if dist_bg < min_dist_bg:
                min_dist_bg = dist_bg
        # Update Heuristic Function!
        pmd += min_dist_bg
    # Update Heuristic Function!
    pmd += min_dist_br
    # Return h(n)!
    return pmd


# Calculate Cost from Parent g(n)!
def calculate_cost(state, t_map, p_tree: Tree, parent_node: Node):
    # Cost of a State = Cost of Current Cell + Cost of Parent State!
    cost = eval(t_map[state['bot'][1]][state['bot'][0]])
    if parent_node:
        cost += parent_node.data['g_cost']
    return cost


def make_goal_state(t_map, state):
    new_state = state.copy()
    new_state['butters'] = [len(state['butters']) * state['goals'][0]]
    for action in ACTIONS:
        last_bot_pos = (state['goals'][0][0] + action.value[0],
                        state['goals'][0][1] + action.value[1])
        if check_act_validity(t_map, last_bot_pos):
            before_last_bot_pos = (last_bot_pos[0] + action.value[0],
                                   last_bot_pos[1] + action.value[1])
            if check_act_validity(t_map, before_last_bot_pos):
                new_state['bot'] = last_bot_pos
                new_state['done'] = True
                return new_state



def find_some(state: list, some):
    points_list = []
    for y, row in enumerate(state):
        for x, cell in enumerate(row):
            if cell.__contains__(some):
                points_list.append((x, y))
    return points_list


def clear_everything(t_map: list):
    for y, row in enumerate(t_map):
        for x, cell in enumerate(row):
            t_map[y][x] = t_map[y][x][0]
    return t_map


def read_map(map_path):
    map_file = open(map_path)
    global h, w
    h, w = map(int, map_file.readline().split())
    initial_state = []
    for r_n in range(h):
        initial_state.append(map_file.readline().split())
    state = {}
    state['bot'] = find_some(initial_state, 'r')[0]
    state['butters'] = find_some(initial_state, 'b')
    state['goals'] = find_some(initial_state, 'p')
    state['done'] = False
    initial_state = clear_everything(initial_state)
    return initial_state, state


def render_map(t_map):
    for row in t_map:
        for col in row:
            print(col, end='|')
        print()


def check_act_validity(t_map, pos):
    # Invalid Action! (Out of PlayGround)
    if pos[0] == -1 or pos[1] == -1 or \
            pos[0] == w or pos[1] == h:
        return False
    # Invalid Action! (Hit Wall)
    pos_cost = t_map[pos[1]][pos[0]]
    if pos_cost == 'x':
        return False
    # All is Well! :D
    return True

# Check if all of Butters Are on Goals :))!
def check_done(state):
    for butter_point in state['butters']:
        if not butter_point in state['goals']:
            return False
    return True


def act(t_map, state, action):
    # Backup Old State!
    new_state = state.copy()
    new_bot_pos = (new_state['bot'][0] + action.value[0],
                   new_state['bot'][1] + action.value[1])
    # Check if Bot Movement is Valid!
    if not check_act_validity(t_map, new_bot_pos):
        return False
    # Hit Butter! Move it!
    if new_bot_pos in new_state['butters']:
        # Update Butter Position Temporary
        new_butter_pos = (new_bot_pos[0] + action.value[0],
                          new_bot_pos[1] + action.value[1])
        # Check if Butter Movement is Valid!
        if not check_act_validity(t_map, new_butter_pos):
            return False
        # Move Butter! :D
        new_state['butters'].remove(new_bot_pos)
        new_state['butters'].append(new_butter_pos)
    # Move Bot! :D
    new_state['bot'] = new_bot_pos
    new_state['done'] = check_done(state)
    return new_state


def act_back(t_map, state, action):
    # Backup Old State!
    new_state = state.copy()
    old_bot_pos = (new_state['bot'][0] - action.value[0],
                   new_state['bot'][1] - action.value[1])
    new_bot_pos = (new_state['bot'][0] + action.value[0],
                   new_state['bot'][1] + action.value[1])
    # Check if Bot Movement is Valid!
    if not check_act_validity(t_map, old_bot_pos):
        return False
    # Hit Butter! Move it!
    if new_bot_pos in new_state['butters']:
        # Update Butter Position Temporary
        new_butter_pos = (new_bot_pos[0] - action.value[0],
                          new_bot_pos[1] - action.value[1])
        # Check if Butter Movement is Valid!
        if not check_act_validity(t_map, new_butter_pos):
            return False
        # Move Butter! :D
        new_state['butters'].remove(new_bot_pos)
        new_state['butters'].append(new_butter_pos)
    # Move Bot! :D
    new_state['bot'] = old_bot_pos
    # If Still Done or Butters are on Bots( =)) ) State is Invalid!
    if check_done(state) or new_state['bot'] in new_state['butters']:
        return False
    new_state['done'] = False
    return new_state


def move(t_map, state, action, backward):
    if backward:
        return act_back(t_map, state, action)
    return act(t_map, state, action)


if __name__ == '__main__':
    t_map, state = read_map('../input/test3.txt')
    render_map(t_map)

    print(act(t_map, state, ACTIONS.UP))
    t_map, state = read_map('../input/test3.txt')
    print(act(t_map, state, ACTIONS.RIGHT))
    t_map, state = read_map('../input/test3.txt')
    print(act(t_map, state, ACTIONS.DOWN))
    t_map, state = read_map('../input/test3.txt')
    print(act(t_map, state, ACTIONS.LEFT))
