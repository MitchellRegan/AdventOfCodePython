def to2DList(inFile_):
    '''Reads each line of an input file and creates a 2D array of each char.
    - param inFile: string for the full file path of the input file to read.
    - return: 2D list of chars.
    '''
    grid = []
    with open(inFile_, 'r') as f:
        for line in f:
            row = list(line)
            if row[-1] == '\n':
                row.pop()
            grid.append(row)
    return grid


def toDict1key1val(inFile_, keyIndex_=0, valIndex_=1, keyType_='s', valType_='s'):
    '''Reads each line of an input file and creates a dictionary.
    - param inFile: string for the full file path of the input file to read.
    - param keyIndex: int for the index of the word in each line of the input to use as dictionary keys.
    - param valIndex: int for the index of the word in each line of the input to use as dictionary values.
    - param keyType: string for what type to cast the key strings to. 's' = string, 'i' = int, 'f' = float.
    - param valType: string for what type to cast the value strings to. 's' = string, 'i' = int, 'f' = float.
    - return: Dictionary where there's one value per key.
    '''
    dict = {}
    with open(inFile_, 'r') as f:
        for line in f:
            #Delineating the line into "words"
            sline = line.split(' ')
            #Getting the key of the key-value pair
            key = sline[keyIndex_]
            if key[-1] == '\n':
                key.pop()
            #Converting the key to the correct type
            if keyType_ is "i":
                key = int(key)
            elif keyType_ is "f":
                key = float(key)

            #Getting the value of the key-value pair
            val = sline[valIndex_]
            if val[-1] == '\n':
                val.pop()
            #Converting the value to the correct type
            if valType_ is "i":
                val = int(val)
            elif valType_ is "f":
                val = float(val)

            #Assinging all of the values to a list for their key
            if key in dict.keys():
                dict[key].append(val)
            else:
                dict[key] = [val]

    return dict