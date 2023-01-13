class BinaryMinHeap:
    '''Binary Heap data structure where the smallest elements are stored at the top.
    '''
    def __init__(self, data=None):
        '''Constructor for the Binary Min Heap.
        - data: The list of initial values to store.
        '''
        self._data = []
        if type(data) is list or type(data) is tuple or type(data) is set:
            for x in data:
                self.insert(x)
            #self.__sort()
        else:
            self._data = [data]


    def __len__(self):
        '''Override for the len function to get the number of elements in this heap.
        '''
        return len(self._data)


    def __getitem__(self, key):
        '''Override for the get index operator 'heap[#]'
        '''
        return self._data[key]


    def __getslice__(self, i, j):
        '''Override for the slice operator '[i:j]'
        '''
        return self._data[i:j]


    def __repr__(self):
        '''Override for how this heap is displayed when printed.
        '''
        return '{}'.format(self._data)


    def getParent(self, index):
        '''Finds the parent index for the given position, or None if there isn't one.
        '''
        if index < 1:
            return None
        return int((index - 1) // 2)


    def getLeftChild(self, index):
        '''Finds the index of the left child of the given position, or None if there isn't one.
        '''
        i = (index * 2) + 1
        if i < len(self._data):
            return i
        return None


    def getRightChild(self, index):
        '''Finds the index of the right child of the given position, or None if there isn't one.
        '''
        i = (index * 2) + 2
        if i < len(self._data):
            return i
        return None


    def heapify(self, index):
        '''Checks the element at the given index to make sure it is greater than its parent and smaller than its children.
        '''
        p = self.getParent(index)
        if p is not None and self._data[index] < self._data[p]:
            placeholder = self._data[index]
            self._data[index] = self._data[p]
            self._data[p] = placeholder
            self.heapify(index)
            self.heapify(p)
            return

        l = self.getLeftChild(index)
        if l is not None and self._data[index] > self._data[l]:
            placeholder = self._data[index]
            self._data[index] = self._data[l]
            self._data[l] = placeholder
            self.heapify(index)
            self.heapify(l)
            return

        r = self.getRightChild(index)
        if r is not None and self._data[index] > self._data[r]:
            placeholder = self._data[index]
            self._data[index] = self._data[r]
            self._data[r] = placeholder
            self.heapify(index)
            self.heapify(r)
            return


    def printDepths(self):
        '''Prints the elements at each depth of the heap.
        '''
        if len(self._data) == 0:
            print('None')
            return

        depth = 0
        depthLists = []
        while len(self._data) >= (2**depth):
            min = (2**depth)-1
            max = (2**(depth+1))-1
            if max > len(self._data) - 1:
                max = len(self._data)

            depthLists.append(self._data[min:max])
            depth += 1

        depthLists[-1] = '  '.join(str(x) for x in depthLists[-1])

        for i in range(depth-1, -1, -1):
            numSpaces = int(len(depthLists[-1]) / ((2**i)+1))
            space = ''

            for s in range(numSpaces):
                space += ' '
            depthLists[i] = space + space.join(str(x) for x in depthLists[i])

        for x in depthLists:
            print(x)


    def insert(self, element):
        '''Inserts a new element into the heap and shifts it into the correct depth.
        '''
        self._data.append(element)
        self.heapify(len(self._data)-1)


    def extend(self, li):
        '''Adds all elements from a list to this heap.
        '''
        for x in li:
            self.insert(x)


    def popFront(self):
        '''Extracts the root element from the heap and returns it.
        '''
        val = self._data[0]
        self._data[0] = self._data.pop()
        self.heapify(0)

        return val


    def index(self, element):
        '''Returns the first index index of the selected element, or None if it doesn't exist.
        '''
        for i in range(0, len(self._data)):
            if self._data[i] == element:
                return i
        return None


    def remove(self, element):
        '''Removes the selected element from this heap and returns it.
        '''
        i = self.index(element)
        if i is None:
            return None

        if i == len(self._data)-1:
            return self._data.pop()

        val = self._data[i]
        self._data[i] = self._data.pop()
        self.heapify(i)

        return val
        


class BinaryMinHeapComplex:
    '''Binary Min Heap for complex objects that require a special "less than" comparitor to sort.
    '''
    def __init__(self, lessThan, data=None):
        '''Constructor for the Binary Min Heap.
        - lessThan: Lambda comparison function. Required for data structures that don't have a built-in method for "less than"
        - data: The list of initial values to store.
        '''
        self.lessThan = lessThan
        self._data = []
        if type(data) is list or type(data) is tuple or type(data) is set:
            for x in data:
                self.insert(x)
            #self.__sort()
        else:
            self._data = [data]


    def __len__(self):
        '''Override for the len function to get the number of elements in this heap.
        '''
        return len(self._data)


    def __getitem__(self, key):
        '''Override for the get index operator 'heap[#]'
        '''
        return self._data[key]


    def __getslice__(self, i, j):
        '''Override for the slice operator '[i:j]'
        '''
        return self._data[i:j]


    def __repr__(self):
        '''Override for how this heap is displayed when printed.
        '''
        return '{}'.format(self._data)


    def getParent(self, index):
        '''Finds the parent index for the given position, or None if there isn't one.
        '''
        if index < 1:
            return None
        return int((index - 1) // 2)


    def getLeftChild(self, index):
        '''Finds the index of the left child of the given position, or None if there isn't one.
        '''
        i = (index * 2) + 1
        if i < len(self._data):
            return i
        return None


    def getRightChild(self, index):
        '''Finds the index of the right child of the given position, or None if there isn't one.
        '''
        i = (index * 2) + 2
        if i < len(self._data):
            return i
        return None


    def heapify(self, index):
        '''Checks the element at the given index to make sure it is greater than its parent and smaller than its children.
        '''
        p = self.getParent(index)
        if p is not None and self.lessThan(self._data[index], self._data[p]):
            placeholder = self._data[index]
            self._data[index] = self._data[p]
            self._data[p] = placeholder
            self.heapify(index)
            self.heapify(p)
            return

        l = self.getLeftChild(index)
        if l is not None and self.lessThan(self._data[l], self._data[index]):
            placeholder = self._data[index]
            self._data[index] = self._data[l]
            self._data[l] = placeholder
            self.heapify(index)
            self.heapify(l)
            return

        r = self.getRightChild(index)
        if r is not None and self.lessThan(self._data[r], self._data[index]):
            placeholder = self._data[index]
            self._data[index] = self._data[r]
            self._data[r] = placeholder
            self.heapify(index)
            self.heapify(r)
            return


    def printDepths(self):
        '''Prints the elements at each depth of the heap.
        '''
        if len(self._data) == 0:
            print('None')
            return

        depth = 0
        depthLists = []
        while len(self._data) >= (2**depth):
            min = (2**depth)-1
            max = (2**(depth+1))-1
            if max > len(self._data) - 1:
                max = len(self._data)

            depthLists.append(self._data[min:max])
            depth += 1

        depthLists[-1] = '  '.join(str(x) for x in depthLists[-1])

        for i in range(depth-1, -1, -1):
            numSpaces = int(len(depthLists[-1]) / ((2**i)+1))
            space = ''

            for s in range(numSpaces):
                space += ' '
            depthLists[i] = space + space.join(str(x) for x in depthLists[i])

        for x in depthLists:
            print(x)


    def insert(self, element):
        '''Inserts a new element into the heap and shifts it into the correct depth.
        '''
        self._data.append(element)
        self.heapify(len(self._data)-1)


    def extend(self, li):
        '''Adds all elements from a list to this heap.
        '''
        for x in li:
            self.insert(x)


    def popFront(self):
        '''Extracts the root element from the heap and returns it.
        '''
        val = self._data[0]
        self._data[0] = self._data.pop()
        self.heapify(0)

        return val


    def index(self, element):
        '''Returns the first index index of the selected element, or None if it doesn't exist.
        '''
        for i in range(0, len(self._data)):
            if self._data[i] == element:
                return i
        return None


    def remove(self, element):
        '''Removes the selected element from this heap and returns it.
        '''
        i = self.index(element)
        if i is None:
            return None

        if i == len(self._data)-1:
            return self._data.pop()

        val = self._data[i]
        self._data[i] = self._data.pop()
        self.heapify(i)

        return val



class BinaryMaxHeap:
    '''Binary Heap data structure where the largest elements are stored at the top.
    '''
    def __init__(self, data=None):
        '''Constructor for the Binary Max Heap.
        - data: The list of initial values to store.
        '''
        self._data = []
        if type(data) is list or type(data) is tuple or type(data) is set:
            for x in data:
                self.insert(x)
        else:
            self._data = [data]


    def __len__(self):
        '''Override for the len function to get the number of elements in this heap.
        '''
        return len(self._data)


    def __getitem__(self, key):
        '''Override for the get index operator 'heap[#]'
        '''
        return self._data[key]


    def __getslice__(self, i, j):
        '''Override for the slice operator '[i:j]'
        '''
        return self._data[i:j]


    def __repr__(self):
        '''Override for how this heap is displayed when printed.
        '''
        return '{}'.format(self._data)


    def getParent(self, index):
        '''Finds the parent index for the given position, or None if there isn't one.
        '''
        if index < 1:
            return None
        return int((index - 1) // 2)


    def getLeftChild(self, index):
        '''Finds the index of the left child of the given position, or None if there isn't one.
        '''
        i = (index * 2) + 1
        if i < len(self._data):
            return i
        return None


    def getRightChild(self, index):
        '''Finds the index of the right child of the given position, or None if there isn't one.
        '''
        i = (index * 2) + 2
        if i < len(self._data):
            return i
        return None


    def heapify(self, index):
        '''Checks the element at the given index to make sure it is smaller than its parent and larger than its children.
        '''
        p = self.getParent(index)
        if p is not None and self._data[index] > self._data[p]:
            placeholder = self._data[index]
            self._data[index] = self._data[p]
            self._data[p] = placeholder
            self.heapify(index)
            self.heapify(p)
            return

        l = self.getLeftChild(index)
        if l is not None and self._data[index] < self._data[l]:
            placeholder = self._data[index]
            self._data[index] = self._data[l]
            self._data[l] = placeholder
            self.heapify(index)
            self.heapify(l)
            return

        r = self.getRightChild(index)
        if r is not None and self._data[index] < self._data[r]:
            placeholder = self._data[index]
            self._data[index] = self._data[r]
            self._data[r] = placeholder
            self.heapify(index)
            self.heapify(r)
            return


    def printDepths(self):
        '''Prints the elements at each depth of the heap.
        '''
        if len(self._data) == 0:
            print('None')
            return

        depth = 0
        depthLists = []
        while len(self._data) >= (2**depth):
            min = (2**depth)-1
            max = (2**(depth+1))-1
            if max > len(self._data) - 1:
                max = len(self._data)

            depthLists.append(self._data[min:max])
            depth += 1

        depthLists[-1] = '  '.join(str(x) for x in depthLists[-1])

        for i in range(depth-1, -1, -1):
            numSpaces = int(len(depthLists[-1]) / ((2**i)+1))
            space = ''

            for s in range(numSpaces):
                space += ' '
            depthLists[i] = space + space.join(str(x) for x in depthLists[i])

        for x in depthLists:
            print(x)


    def insert(self, element):
        '''Inserts a new element into the heap and shifts it into the correct depth.
        '''
        self._data.append(element)
        self.heapify(len(self._data)-1)


    def extend(self, li):
        '''Adds all elements from a list to this heap.
        '''
        for x in li:
            self.insert(x)


    def popFront(self):
        '''Extracts the root element from the heap and returns it.
        '''
        val = self._data[0]
        self._data[0] = self._data.pop()
        self.heapify(0)

        return val


    def index(self, element):
        '''Returns the first index index of the selected element, or None if it doesn't exist.
        '''
        for i in range(0, len(self._data)):
            if self._data[i] == element:
                return i
        return None


    def remove(self, element):
        '''Removes the selected element from this heap and returns it.
        '''
        i = self.index(element)
        if i is None:
            return None

        if i == len(self._data)-1:
            return self._data.pop()

        val = self._data[i]
        self._data[i] = self._data.pop()
        self.heapify(i)

        return val
        


class BinaryMaxHeapComplex:
    '''Binary Max Heap for complex objects that require a special "greater than" comparitor to sort.
    '''
    def __init__(self, greaterThan, data=None):
        '''Constructor for the Binary Min Heap.
        - greaterThan: Lambda comparison function. Required for data structures that don't have a built-in method for "greater than"
        - data: The list of initial values to store.
        '''
        self.greaterThan = greaterThan
        self._data = []
        if type(data) is list or type(data) is tuple or type(data) is set:
            for x in data:
                self.insert(x)
            #self.__sort()
        else:
            self._data = [data]


    def __len__(self):
        '''Override for the len function to get the number of elements in this heap.
        '''
        return len(self._data)


    def __getitem__(self, key):
        '''Override for the get index operator 'heap[#]'
        '''
        return self._data[key]


    def __getslice__(self, i, j):
        '''Override for the slice operator '[i:j]'
        '''
        return self._data[i:j]


    def __repr__(self):
        '''Override for how this heap is displayed when printed.
        '''
        return '{}'.format(self._data)


    def getParent(self, index):
        '''Finds the parent index for the given position, or None if there isn't one.
        '''
        if index < 1:
            return None
        return int((index - 1) // 2)


    def getLeftChild(self, index):
        '''Finds the index of the left child of the given position, or None if there isn't one.
        '''
        i = (index * 2) + 1
        if i < len(self._data):
            return i
        return None


    def getRightChild(self, index):
        '''Finds the index of the right child of the given position, or None if there isn't one.
        '''
        i = (index * 2) + 2
        if i < len(self._data):
            return i
        return None


    def heapify(self, index):
        '''Checks the element at the given index to make sure it is greater than its parent and smaller than its children.
        '''
        p = self.getParent(index)
        if p is not None and self.greaterThan(self._data[index], self._data[p]):
            placeholder = self._data[index]
            self._data[index] = self._data[p]
            self._data[p] = placeholder
            self.heapify(index)
            self.heapify(p)
            return

        l = self.getLeftChild(index)
        if l is not None and self.greaterThan(self._data[l], self._data[index]):
            placeholder = self._data[index]
            self._data[index] = self._data[l]
            self._data[l] = placeholder
            self.heapify(index)
            self.heapify(l)
            return

        r = self.getRightChild(index)
        if r is not None and self.greaterThan(self._data[r], self._data[index]):
            placeholder = self._data[index]
            self._data[index] = self._data[r]
            self._data[r] = placeholder
            self.heapify(index)
            self.heapify(r)
            return


    def printDepths(self):
        '''Prints the elements at each depth of the heap.
        '''
        if len(self._data) == 0:
            print('None')
            return

        depth = 0
        depthLists = []
        while len(self._data) >= (2**depth):
            min = (2**depth)-1
            max = (2**(depth+1))-1
            if max > len(self._data) - 1:
                max = len(self._data)

            depthLists.append(self._data[min:max])
            depth += 1

        depthLists[-1] = '  '.join(str(x) for x in depthLists[-1])

        for i in range(depth-1, -1, -1):
            numSpaces = int(len(depthLists[-1]) / ((2**i)+1))
            space = ''

            for s in range(numSpaces):
                space += ' '
            depthLists[i] = space + space.join(str(x) for x in depthLists[i])

        for x in depthLists:
            print(x)


    def insert(self, element):
        '''Inserts a new element into the heap and shifts it into the correct depth.
        '''
        self._data.append(element)
        self.heapify(len(self._data)-1)


    def extend(self, li):
        '''Adds all elements from a list to this heap.
        '''
        for x in li:
            self.insert(x)


    def popFront(self):
        '''Extracts the root element from the heap and returns it.
        '''
        val = self._data[0]
        self._data[0] = self._data.pop()
        self.heapify(0)

        return val


    def index(self, element):
        '''Returns the first index index of the selected element, or None if it doesn't exist.
        '''
        for i in range(0, len(self._data)):
            if self._data[i] == element:
                return i
        return None


    def remove(self, element):
        '''Removes the selected element from this heap and returns it.
        '''
        i = self.index(element)
        if i is None:
            return None

        if i == len(self._data)-1:
            return self._data.pop()

        val = self._data[i]
        self._data[i] = self._data.pop()
        self.heapify(i)

        return val