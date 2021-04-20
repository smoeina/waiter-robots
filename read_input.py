def read_input(input_file_name):
    file = open(input_file_name)
    rows = file.readlines()[1:]
    file.close()
    for i in range(len(rows)):
        rows[i]=rows[i].replace("\t"," ").replace("\n","").split(" ")
    return rows