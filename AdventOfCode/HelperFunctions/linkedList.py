import warnings

class LLNode:
    '''Nodes used for linked lists. Stores one data value, and pointers to the next and previous nodes in the list.
    '''
    def __init__(self, data_, prev_=None, next_=None):
        '''Constructor for the Linked List Node.
        - data: The data to be stored in this node.
        - prev: Pointer to the previous node in the linked list.
        - next: Pointer to the next node in the linked list.
        '''
        self.data = data_
        #Making sure the next/prev value given is either None or a valid LLNode
        if next_ is not None and not isinstance(next_, LLNode):
            self._next = None
        else:
            self._next = next_
        if prev_ is not None and not isinstance(prev_, LLNode):
            self._prev = None
        else:
            self._prev = prev_


    def getNext(self):
        '''Reference for the next node in the Linked List.
        '''
        return self._next


    def getPrev(self):
        '''Reference for the previous node in the Linked List.
        '''
        return self._prev


    def setNext(self, next_):
        '''Sets the value of the next node in the list.
        - next_: Reference to the next LLNode.
        - returns: True if the value was able to be set, or False otherwise.
        '''
        if next_ is not None and not isinstance(next_, LLNode):
            warnings.warn("WARNING: LLNode.setNext. Type", type(next_), "isnt of type LLNode.")
            return False
        else:
            self._next = next_
            return True


    def setPrev(self, prev_):
        '''Sets the value of the previous node in the list.
        - prev_: Reference to the previous LLNode.
        - returns: True if the value was able to be set, or False otherwise.
        '''
        if prev_ is not None and not isinstance(prev_, LLNode):
            warnings.warn("WARNING: LLNode.setPrev. Value given isnt of type LLNode.")
            return False
        else:
            self._prev = prev_
            return True


class LinkedList:
    '''Linked List data structure that stores references to the nodes it contains.
    '''
    def __init__(self, data_=None):
        '''Constructor for the Linked List.
        - data_: Value(s) to be stored in this Linked List. If iterable, a node will be created for each value.
        '''
        self._head = None
        self._tail = None
        self._size = 0

        #Creating LLNodes for each data value given
        if data_ != None:
            #Attempting to iterate through the value to create multiple nodes
            try:
                prev = None
                for d in data_:
                    newNode = LLNode(d, prev, None)
                    #Linking the previous node to this new node
                    if prev is not None:
                        prev.setNext(newNode)
                    else:
                        self._head = newNode
                        
                    prev = newNode
                    self._tail = newNode
                    self._size += 1
            #If the data isn't iterable, we just create one node
            except TypeError as e:
                newNode = LLNode(data_)
                self._head = newNode
                self._tail = newNode
                self._size += 1
        return


    def __len__(self):
        #'''Override for the len function to get the number of elements in this Linked List.
        #'''
        return self._size


    def __getitem__(self, key:int):
        '''Override for the get index operator LinkedList[#]
        '''
        #If the key given is positive, we search from the head forward
        if key >= 0:
            p = self._head
            i = 0
            while i < key:
                if p == None:
                    raise Exception("ERROR: LinkedList out of range exception.")
                p = p.getNext()
                i += 1
            if p is None:
                raise Exception("ERROR: LinkedList out of range exception.")
            return p.data
        #If the key given is negative, we search from the tail backward
        else:
            p = self._tail
            i = -1
            while i > key:
                if p is None:
                    raise Exception("ERROR: LinkedList out of range exception.")
                    return
                p = p.getPrev()
                i -= 1
            if p is None:
                raise Exception("ERROR: LinkedList out of range exception.")
            return p.data


    def append(self, data_:any):
        '''Adds a new node to the end of this Linked List with the given data.
        - data_: Value to be stored in the new node.
        '''
        newNode = LLNode(data_, prev_=self._tail)
        
        if self._size > 0:
            self._tail.setNext(newNode)
            if self._head._prev is not None:
                self._head.setPrev(newNode)
                newNode.setPrev(self._head)
        else:
            self._head = newNode
            
        self._tail = newNode
        self._size += 1
        

    def insert(self, index_:int, data_:any):
        '''Adds a new node at the given index.
        - index_: Int for index to insert the new node at.
        - data_: Value for the inserted node to hold.
        '''
        print("---Linked List insert 1, index:", index_, "   data:", data_, "   size:", self._size)
        newNode = LLNode(data_)
        if self._size == 0:
            print("---Linked List insert 2")
            self._head = newNode
            self._tail = newNode
            self._size = 1
            print("---Linked List insert 3")
        elif index_ == self._size:
            print("---Linked List insert 4")
            self.append(data_)
            print("---Linked List insert 5")
        else:
            print("---Linked List insert 6    ", type(index_))
            p = None
            #If the key given is positive, we search from the head forward
            if index_ >= 0:
                p = self._head
                i = 0
                while i < index_:
                    print("\tCurrent index", i)
                    if p == None:
                        raise Exception("ERROR: LinkedList out of range exception.")
                    p = p.getNext()
                    i += 1
                if p is None:
                    raise Exception("ERROR: LinkedList out of range exception.")
            #If the key given is negative, we search from the tail backward
            else:
                p = self._tail
                i = -1
                while i > index_:
                    if p is None:
                        raise Exception("ERROR: LinkedList out of range exception.")
                    p = p.getPrev()
                    i -= 1
                if p is None:
                    raise Exception("ERROR: LinkedList out of range exception.")
            print("---Linked List insert 6.1   ", type(p))
            newNode.setNext(p)
            print("---Linked List insert 6.2")
            newNode.setPrev(p._prev)
            print("---Linked List insert 6.3")
            p.setPrev(newNode)
            print("---Linked List insert 6.4")
            self._size += 1
            print("---Linked List insert 7")


    def reverse(self):
        '''Reverses the order of the nodes in this Linked List.
        '''
        placeholder = self._head
        self._head = self._tail
        self._tail = placeholder
        
        p = self._tail
        while p != None:
            ph = p.getPrev()
            p.setPrev(p.getNext())
            p.setNext(ph)
            p = p.getPrev()
            #Preventing the reversal from looping
            if p is self._tail:
                break


    def toggleLoop(self, loop_:bool=True):
        '''Sets this Linked List to either connect or disconnect the head and tail nodes from each other.
        - loop_: Boolean for if the list should be looped or not.
        '''
        if loop_:
            self._head.setPrev(self._tail)
            self._tail.setNext(self._head)
        else:
            self._head.setPrev(None)
            self._tail.setNext(None)

