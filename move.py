import numpy as np


def move(matrix, places, turn, robot_number):
    validity = True
    robot_y_position = places['robots'][robot_number][0]
    robot_x_position = places['robots'][robot_number][1]
    robot_tile = list(matrix[robot_y_position][robot_x_position])
    robot_tile.remove('r')
    robot_tile_str = "".join(robot_tile)
    matrix[robot_y_position][robot_x_position] = robot_tile_str
    turn = turn.lower()
    try:
        if turn == 'up':
            robot_y_position -= 1
            matrix[robot_y_position][robot_x_position] = matrix[robot_y_position][robot_x_position] + "r"
        elif turn == 'down':
            robot_y_position += 1
            matrix[robot_y_position][robot_x_position] = matrix[robot_y_position][robot_x_position] + "r"
        elif turn == 'left':
            robot_x_position -= 1
            matrix[robot_y_position][robot_x_position] = matrix[robot_y_position][robot_x_position] + "r"

        elif turn == 'right':
            robot_x_position += 1
            matrix[robot_y_position][robot_x_position] = matrix[robot_y_position][robot_x_position] + "r"
    except:
        pass


    for i in range(len(places['butters'])):
        if places['butters'][i] == (robot_y_position, robot_x_position):
            butter_y_position = places['butters'][i][0]
            butter_x_position = places['butters'][i][1]

            butter_tile = list(matrix[robot_y_position][robot_x_position])
            butter_tile.remove('b')
            butter_tile_str = "".join(butter_tile)
            matrix[butter_y_position][butter_x_position] = butter_tile_str

            try:
                if turn == 'up':
                    butter_y_position -= 1
                    matrix[butter_y_position][butter_x_position] = matrix[butter_y_position][
                                                                           butter_x_position] + "b"
                elif turn == 'down':
                    butter_y_position += 1
                    matrix[butter_y_position][butter_x_position] = matrix[butter_y_position][
                                                                           butter_x_position] + "b"
                elif turn == 'left':
                    butter_x_position -= 1
                    matrix[butter_y_position][butter_x_position] = matrix[butter_y_position][
                                                                           butter_x_position] + "b"

                elif turn == 'right':
                    butter_x_position += 1
                    matrix[butter_y_position][butter_x_position] = matrix[butter_y_position][
                                                                           butter_x_position] + "b"
            except:
                pass


    block_places = places['blocks']
    rows = len(matrix)
    cols = len(matrix[0])
    if turn == 'down':
        print("Abbase Bu Azaar")
    if ((robot_y_position, robot_x_position) in block_places):
        validity = False
    try:
        if (butter_y_position > rows - 1) or (butter_y_position < 0) or (butter_x_position > cols - 1) or (butter_x_position < 0) or ((butter_y_position, butter_x_position) in block_places):
            validity = False
    except:
        pass
    if (robot_x_position > cols - 1) or (robot_y_position > rows - 1) or  (robot_y_position < 0) or (robot_x_position < 0):
        validity = False

    return matrix, validity
