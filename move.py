import numpy as np


def move(matrix, places, turn, robot_number):
    global butter_y_position, butter_x_position
    validity = True
    robot_y_position = places['robots'][robot_number][0]
    robot_x_position = places['robots'][robot_number][1]
    robot_tile = list(matrix[robot_y_position][robot_x_position])
    robot_tile.remove('r')
    robot_tile_str = "".join(robot_tile)
    matrix[robot_y_position][robot_x_position] = robot_tile_str
    turn = turn.lower()
    if turn == 'up':
        matrix[robot_y_position - 1][robot_x_position] = matrix[robot_y_position - 1][robot_x_position] + "r"
        robot_y_position -= 1
    elif turn == 'down':
        matrix[robot_y_position + 1][robot_x_position] = matrix[robot_y_position + 1][robot_x_position] + "r"
        robot_y_position += 1
    elif turn == 'left':
        matrix[robot_y_position][robot_x_position - 1] = matrix[robot_y_position][robot_x_position - 1] + "r"
        robot_x_position -= 1

    elif turn == 'right':
        matrix[robot_y_position][robot_x_position + 1] = matrix[robot_y_position][robot_x_position + 1] + "r"
        robot_x_position += 1

    for i in range(len(places['butters'])):
        if places['butters'][i] == (robot_y_position, robot_x_position):
            butter_y_position = places['butters'][i][0]
            butter_x_position = places['butters'][i][1]

            butter_tile = list(matrix[robot_y_position][robot_x_position])
            butter_tile.remove('b')
            butter_tile_str = "".join(butter_tile)
            matrix[butter_y_position][butter_x_position] = butter_tile_str

            if turn == 'up':
                matrix[butter_y_position - 1][butter_x_position] = matrix[butter_y_position - 1][
                                                                       butter_x_position] + "b"
                butter_y_position -= 1
            elif turn == 'down':
                matrix[butter_y_position + 1][butter_x_position] = matrix[butter_y_position + 1][
                                                                       butter_x_position] + "b"
                butter_y_position += 1
            elif turn == 'left':
                matrix[butter_y_position][butter_x_position - 1] = matrix[butter_y_position][
                                                                       butter_x_position - 1] + "b"
                butter_x_position -= 1

            elif turn == 'right':
                matrix[butter_y_position][butter_x_position + 1] = matrix[butter_y_position][
                                                                       butter_x_position + 1] + "b"
                butter_x_position += 1

    block_places = places['blocks']
    rows = len(matrix)
    cols = len(matrix[0])
    if ((robot_y_position, robot_x_position) in block_places):
        validity = False
    try:
        if (butter_y_position > rows - 1) or (butter_y_position < 0) or (butter_x_position > cols - 1) or (butter_x_position < 0) or ((butter_y_position, butter_x_position) in block_places):
            validity = False
            print(butter_y_position,butter_x_position,cols,rows)
    except:
        pass
    if (robot_x_position > cols - 1) or (robot_y_position > rows - 1) or  (robot_y_position < 0) or (robot_x_position < 0):
        validity = False

    return matrix, validity
