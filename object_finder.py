def object_finder(i,j,places):
    if (i,j) in places['robots']:
        return 'robot'
    elif (i,j) in places['butters']:
        return 'butter'
    elif (i,j) in places['blocks']:
        return 'block'
    elif (i,j) in places['aims']:
        return 'aim'
    else:
        return 'nothing'