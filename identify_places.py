def identify_places(matrix):
    places = {'robots':[],'butters':[],'blocks':[],'aims':[]}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if ('r' in matrix[i][j]):
                places['robots'].append((i,j))
            elif ('b' in matrix[i][j]):
                places['butters'].append((i, j))
            elif ('x' in matrix[i][j]):
                places['blocks'].append((i, j))
            elif ('p' in matrix[i][j]):
                places['aims'].append((i, j))
    return places

