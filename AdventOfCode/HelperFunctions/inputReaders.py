def to2DList(inFile_):
    '''Reads each line of an input file and creates a 2D array of each char.
    - param inFile: string for the full file path of the input file to read.
    - return: 2D list of chars.
    '''
    grid = []
    with open(inFile, 'r') as f:
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
    with open(inFile, 'r') as f:
        for line in f:
            sline = line.split(' ')
            key = sline[keyIndex_]
            if key[-1] == '\n':
                key.pop()
            val = sline[valIndex_]
            if val[-1] == '\n':
                val.pop()

    return dict