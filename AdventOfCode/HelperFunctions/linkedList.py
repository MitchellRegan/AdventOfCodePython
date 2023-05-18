import warnings

class LLNode:
    '''Nodes used for linked lists. Stores one data value, and pointers to the next and previous nodes in the list.
    '''
    def __init__(self, data_, next_=None, prev_=None):
        '''Constructor for the Linked List Node.
        - data: The data to be stored in this node.
        - next: Pointer to the next node in the linked list.
        - prev: Pointer to the previous node in the linked list.
        '''
        self.data = data
        #Making sure the next/prev value given is either None or a valid LLNode
        if next_ is not None and type(next_) != type(LLNode):
            self._next = None
        else:
            self._next = next_
        if prev_ is not None and type(prev_) != type(LLNode):
            self._prev = None
        else:
            self._prev = prev_

        @property
        def getNext(self):
            '''Reference for the next node in the Linked List.
            '''
            return self._next


        @property
        def getPrev(self):
            '''Reference for the previous node in the Linked List.
            '''
            return self._prev


        def setNext(self, next_):
            '''Sets the value of the next node in the list.
            - next_: Reference to the next LLNode.
            - returns: True if the value was able to be set, or False otherwise.
            '''
            if next_ is not None and type(next_) != type(LLNode):
                warnings.warn("WARNING: LLNode.setNext. Value given isn't of type LLNode.")
                return False
            else:
                self._next = next_
                return True


        def setPrev(self, prev_):
            '''Sets the value of the previous node in the list.
            - prev_: Reference to the previous LLNode.
            - returns: True if the value was able to be set, or False otherwise.
            '''
            if prev_ is not None and type(prev_) != type(LLNode):
                warnings.warn("WARNING: LLNode.setPrev. Value given isn't of type LLNode.")
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
                    newNode = LLNode(d, None, prev)
                    #Linking the previous node to this new node
                    if prev is not None:
                        prev.setNext(newNode)
                    else:
                        self._head = newNode
                    prev = newNode
                    self._tail = newNode
                    self._size += 1
            #If the data isn't iterable, we just create one node
            except TypeError:
                newNode = LLNode(data_)
                self._head = newNode
                self._tail = newNode
                self._size = 1
        return


    def __len__(self):
        '''Override for the len function to get the number of elements in this Linked List.
        '''
        return self._size


    def __getitem__(self, key):
        '''Override for the get index operator 'LinkedList[#]'
        '''
        #If the key given is positive, we search from the head forward
        if key >= 0:
            p = self._head
            i = 0
            while i < key:
                if p is None:
                    raise Exception("ERROR: LinkedList out of range exception.")
                p = p.getNext
                i += 1
            return p
        #If the key given is negative, we search from the tail backward
        else:
            p = self._tail
            i = -1
            while i > key:
                if p is None:
                    raise Exception("ERROR: LinkedList out of range exception.")
                p = p.getPrev
                i -= 1
            return p