class CoordinateNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = None
        self.right = None
    
    def printTree(self):
        '''Prints all coordinate values in the binary tree from smallest to largest.
        '''
        if self.left is not None:
            self.left.printTree()
        print("(%n, %n)" %(self.x, self.y))
        if self.right is not None:
            self.right.printTree()

    
    def insert(self, x, y):
        '''Inserts a new coordinate value into the binary tree.
        - x: Value for the x-coordinate.
        - y: Value for the y-coordinate.
        Return: Bool for if the insertion was successful.
        '''
        if x < self.x or (x == self.x and y < self.y):
            if self.left is None:
                self.left = CoordinateNode(x,y)
                return True
            else:
                return self.left.insert(x,y)
        else:
            if self.right is None:
                self.right = CoordinateNode(x,y)
                return True
            else:
                return self.right.insert(x,y)

    
    def length(self):
        '''Returns the number of elements in this binary tree.
        '''
        l = 0
        if self.left is not None:
            l = self.left.length()
        r = 0
        if self.right is not None:
            r = self.right.length()

        return 1 + l + r


    def toList(self):
        '''Returns all elements in this binary tree as a sorted list from smallest to largest.
        '''
        l = []
        if self.left is not None:
            l = self.left.toList()

        r = []
        if self.right is not None:
            r = self.right.toList()

        l.append([self.x, self.y])
        binList = l.extend(r)
        return binList